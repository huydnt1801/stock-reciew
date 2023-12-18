from config import Config
from utils.helper import *
from utils.logger import get_logger
import pandas as pd
import math
import pymongo


class Assessment():
    def __init__(self, collection, symbol, data):
        self.logger = get_logger("Assessment", Config.LOG_FILE)
        self.collection = collection
        self.init_score = 1
        self.interval = "1m"
        self.type = "giờ"
        self.symbol = symbol
        self.data = pd.json_normalize(data)
        self.res = {}

    def price_indexes_change(self, data, thresh_hold):
        increase_indexes = []
        reduce_indexes = []

        for index, row in data.iterrows():
            if index == 0:
                current_change = row
                continue
            if row['high'] / current_change['high'] > thresh_hold:
                increase_indexes.append(index)
                current_change = row
                continue
            if current_change['low'] / row['low'] > thresh_hold:
                reduce_indexes.append(index)
                current_change = row
                continue
        return increase_indexes, reduce_indexes

    def process(self):
        increase_indexes, reduce_indexes = self.price_indexes_change(
            self.data, Config.THRESH_HOLD)
        current_index = 0
        data = self.data.iloc[current_index]
        high = []
        low = []

        increase_index_count = len(increase_indexes)
        reduce_index_count = len(reduce_indexes)
        increase_ite = reduce_ite = 0
        cnt_change = 0
        while increase_ite < increase_index_count and reduce_ite < reduce_index_count:
            increase_index = increase_indexes[increase_ite]
            reduce_index = reduce_indexes[reduce_ite]
            if increase_index < reduce_index:
                while increase_ite < increase_index_count - 1 and increase_indexes[increase_ite + 1] < reduce_index:
                    increase_index = increase_indexes[increase_ite + 1]
                    increase_ite = increase_ite + 1
                increase_ite = increase_ite + 1
                volume = self.data.iloc[current_index:increase_index].sum()[
                    'volume']
                if self.type == "ngày":
                    volume = volume / 60
                data = self.data.iloc[increase_index]
                duration = get_minute(
                    self.data.iloc[current_index].loc['open_time'], data.loc['open_time'])
                high.append({'start_idx': current_index,
                             'end_idx': increase_index,
                             'volume_arg': volume/duration})
                current_index = increase_index
                cnt_change = cnt_change + 1
            else:
                while reduce_ite < reduce_index_count - 1 and increase_index > reduce_indexes[reduce_ite + 1]:
                    reduce_index = reduce_indexes[reduce_ite]
                    reduce_ite = reduce_ite + 1
                reduce_ite = reduce_ite + 1
                volume = self.data.iloc[current_index:reduce_index].sum()[
                    'volume']
                if self.type == "ngày":
                    volume = volume / 60
                data = self.data.iloc[reduce_index]
                duration = get_minute(
                    self.data.iloc[current_index].loc['open_time'], data.loc['open_time'])
                low.append({'start_idx': current_index,
                           'end_idx': increase_index,
                            'volume_arg': volume/duration})
                current_index = reduce_index
                cnt_change = cnt_change + 1

        return high, low, cnt_change

    def _cal_medium(self, old, new):
        return float((old * self.medium["idx"] + new) / (self.medium["idx"] + 1))

    def _price(self, idx_max_price, idx_min_price):
        max = self.data.iloc[idx_max_price].loc
        min = self.data.iloc[idx_min_price].loc
        msg = f"""\nTrong {self.type} qua, giá {self.symbol} cao nhất là: {max["high"]} lúc {convert_to_date(max["open_time"])} và thấp nhất là: {min["low"]} lúc {convert_to_date(min["open_time"])}"""

        self.res.update({"price": {"max": float(max["high"]),
                                   "min": float(min["low"]),
                                   "max_time": int(max["open_time"]),
                                   "min_time": int(min["open_time"])}})
        self.medium["price"]["max"] = self._cal_medium(
            self.medium["price"]["max"], max["high"])
        self.medium["price"]["min"] = self._cal_medium(
            self.medium["price"]["min"], min["low"])
        if max["high"] > self.medium["price"]["max"] * 1.01 or min["low"] * 1.01 < self.medium["price"]["min"]:
            return msg
        return ""

    def _daily_price(self, start_price, end_price):
        type = 0
        percent = 0
        if end_price > start_price:
            type = 1
            percent = (end_price/start_price - 1) * 100
            if percent >= 0.01:
                msg = f"""\nTrong {self.type} qua, giá {self.symbol} tăng {convert_percent(percent)}%"""
            else:
                msg = f"""\nTrong {self.type} qua, giá {self.symbol} tăng {percent}%"""
        elif end_price < start_price:
            type = -1
            percent = 1 - end_price/start_price
            if percent >= 0.01:
                msg = f"""\nTrong {self.type} qua, giá {self.symbol} giảm {convert_percent(percent)}%"""
            else:
                msg = f"""\nTrong {self.type} qua, giá {self.symbol} giảm {percent}%"""

        self.res.update(
            {"daily_price": {"type": type, "percent": float(percent)}})
        self.medium["daily_price"] = float(self._cal_medium(
            self.medium["daily_price"], percent))
        if percent > self.medium["daily_price"]:
            return msg
        return ""

    def _change_number(self, cnt_change):
        if cnt_change > 10:
            msg = f"""\nGiá {self.symbol} trong {self.type} qua có nhiều biến động"""
        elif cnt_change > 5:
            msg = f"""\nGiá {self.symbol} trong {self.type} qua có khá nhiều biến động"""
        else:
            msg = ""

        self.res.update({"change_number": int(cnt_change)})
        self.medium['change_number'] = int(self._cal_medium(
            self.medium['change_number'], cnt_change))
        if cnt_change > self.medium['change_number']:
            return msg
        return ""

    def _volume_analysis(self, high, low):
        max_volume_high = min_volume_high = high[0]
        for val in high:
            if val['volume_arg'] > max_volume_high['volume_arg']:
                max_volume_high = val
            if val['volume_arg'] < min_volume_high['volume_arg']:
                min_volume_high = val
        max_volume_low = min_volume_low = low[0]
        for val in low:
            if val['volume_arg'] > max_volume_low['volume_arg']:
                max_volume_low = val
            if val['volume_arg'] < min_volume_low['volume_arg']:
                min_volume_low = val

        max_volume_high_start = self.data.iloc[max_volume_high['start_idx']].loc
        max_volume_high_end = self.data.iloc[max_volume_high['end_idx']].loc
        max_volume_high_percent = (
            max_volume_high_end["high"] / max_volume_high_start["low"] - 1) * 100
        msg = f"""\nTừ {convert_to_date(max_volume_high_start["open_time"])} đến {convert_to_date(max_volume_high_end["open_time"])} {self.symbol} tăng {convert_percent(max_volume_high_percent)}% với volume trung bình cao nhất {max_volume_high['volume_arg']}/phút"""

        self.res.update({"volume_increase": {"start_time": int(max_volume_high_start["open_time"]), "end_time": int(max_volume_high_end[
                        "open_time"]), "percent": float(max_volume_high_percent), "value": float(max_volume_high['volume_arg'])}})
        if max_volume_high['volume_arg'] < self.medium["volume_increase"]:
            msg = ""
        self.medium["volume_increase"] = self._cal_medium(
            self.medium["volume_increase"], max_volume_high['volume_arg'])

        max_volume_low_start = self.data.iloc[max_volume_low['start_idx']].loc
        max_volume_low_end = self.data.iloc[max_volume_low['end_idx']].loc
        max_volume_low_percent = (
            1 - max_volume_low_end["low"] / max_volume_low_start["high"]) * 100
        if max_volume_low['volume_arg'] > self.medium["volume_reduce"]:
            msg += f"""\nTừ {convert_to_date(max_volume_low_start["open_time"])} đến {convert_to_date(max_volume_low_end["open_time"])} {self.symbol} giảm {convert_percent(max_volume_low_percent)}% với volume trung bình cao nhất {max_volume_low['volume_arg']}/phút"""
        self.res.update({"volume_reduce": {"start_time": int(max_volume_low_start["open_time"]), "end_time": int(max_volume_low_end[
            "open_time"]), "percent": float(max_volume_low_percent), "value": float(max_volume_low['volume_arg'])}})
        self.medium["volume_reduce"] = self._cal_medium(
            self.medium["volume_reduce"], max_volume_low['volume_arg'])
        return msg

    def analysis(self):
        high, low, cnt_change = self.process()
        idx_max_price = self.data["high"].idxmax()
        idx_min_price = self.data["low"].idxmin()

        close_price = self.data["close"]
        start_price = close_price[0]
        end_price = close_price[len(close_price) - 1]

        msg = self._daily_price(start_price, end_price)
        msg += self._price(idx_max_price, idx_min_price)
        msg += self._change_number(cnt_change)
        msg += self._volume_analysis(high, low)
        return msg

    async def start(self):
        self.logger.info("Start Assessment")
        try:
            cursor = self.collection.find_one()
            self.medium = {
                "idx": 0,
                "daily_price": 0,
                "price": {
                    "max": 0,
                    "min": 0,
                },
                "change_number": 0,
                "volume_increase": 0,
                "volume_reduce": 0,
            }
            if cursor is not None:
                arg = dict(cursor)
                if arg.get('medium', None) is not None:
                    self.medium = arg["medium"]
            msg = self.analysis()
            self.logger.info(msg)
            self.medium["idx"] += 1
            self.collection.insert_one(
                {"current": self.res, "medium": self.medium})
            self.stop()
        except Exception as e:
            self.logger.error(f"{e}")
            self.stop()

    def stop(self) -> None:
        self.logger.info("Stop Assessment")
