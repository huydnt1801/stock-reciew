from config import Config
from utils.helper import *
from utils.logger import get_logger
import pandas as pd
import math
import pymongo


class Assessment():
    def __init__(self, symbol, data):
        self.logger = get_logger("Assessment", Config.LOG_FILE)
        client = pymongo.MongoClient(Config.DB_URL)
        self.database = client["crypto_assessment"]
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

    def _price(self, idx_max_price, idx_min_price):
        max = self.data.iloc[idx_max_price].loc
        min = self.data.iloc[idx_min_price].loc
        msg = f"""Trong {self.type} qua, giá {self.symbol} cao nhất là: {max["high"]} lúc {convert_to_date(max["open_time"])} và thấp nhất là: {min["low"]} lúc {convert_to_date(min["open_time"])}"""
        self.res.update({"price": {"max": max["high"],
                                   "min": min["low"],
                                   "max_time": max["open_time"],
                                   "min_time": min["open_time"]}})
        return msg

    def _daily_price(self, start_price, end_price):
        if end_price > start_price:
            type = 1
            percent = (end_price/start_price - 1) * 100
            if percent >= 0.01:
                msg = f"""Trong {self.type} qua, giá {self.symbol} tăng {convert_percent(percent)}%"""
            else:
                msg = f"""Trong {self.type} qua, giá {self.symbol} tăng {percent}%"""
        elif end_price < start_price:
            type = -1
            percent = 1 - end_price/start_price
            if percent >= 0.01:
                msg = f"""Trong {self.type} qua, giá {self.symbol} giảm {convert_percent(percent)}%"""
            else:
                msg = f"""Trong {self.type} qua, giá {self.symbol} giảm {percent}%"""
        self.res.update({"daily_price": {"type": type, "percent": percent}})
        return msg

    def _change_number(self, cnt_change):
        if cnt_change > 10:
            msg = f"""Giá {self.symbol} trong {self.type} qua có nhiều biến động"""
            change_type = 1.5
        elif cnt_change > 7:
            msg = f"""Giá {self.symbol} trong {self.type} qua có khá nhiều biến động"""
            change_type = 1
        else:
            msg = f"""Giá {self.symbol} trong {self.type} qua không có quá nhiều thay đổi"""
            change_type = 0.5
        self.res.update({"change_number": cnt_change})
        return msg

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
        msg = f"""Từ {convert_to_date(max_volume_high_start["open_time"])} đến {convert_to_date(max_volume_high_end["open_time"])} {self.symbol} tăng {convert_percent(max_volume_high_percent)}% với volume trung bình cao nhất {max_volume_high['volume_arg']}/phút"""
        self.res.update({"volume_increase": {"start_time": max_volume_high_start["open_time"], "end_time": max_volume_high_end[
                        "open_time"], "percent": max_volume_high_percent, "value": max_volume_high['volume_arg']}})

        max_volume_low_start = self.data.iloc[max_volume_low['start_idx']].loc
        max_volume_low_end = self.data.iloc[max_volume_low['end_idx']].loc
        max_volume_low_percent = (
            1 - max_volume_low_end["low"] / max_volume_low_start["high"]) * 100
        msg += f"""\nTừ {convert_to_date(max_volume_low_start["open_time"])} đến {convert_to_date(max_volume_low_end["open_time"])} {self.symbol} giảm {convert_percent(max_volume_low_percent)}% với volume trung bình cao nhất {max_volume_low['volume_arg']}/phút"""
        self.res.update({"volume_reduce": {"start_time": max_volume_low_start["open_time"], "end_time": max_volume_low_end[
            "open_time"], "percent": max_volume_low_percent, "value": max_volume_low['volume_arg']}})
        return msg

    def analysis(self):
        high, low, cnt_change = self.process()
        idx_max_price = self.data["high"].idxmax()
        idx_min_price = self.data["low"].idxmin()

        close_price = self.data["close"]
        start_price = close_price[0]
        end_price = close_price[len(close_price) - 1]

        msg = self._daily_price(start_price, end_price)
        msg += "\n" + self._price(idx_max_price, idx_min_price)
        msg += "\n" + self._change_number(cnt_change)
        msg += "\n" + self._volume_analysis(high, low)
        return msg

    async def start(self):
        self.logger.info("Start Assessment")
        try:
            msg = ""
            msg += self.analysis()
            await self.logger.info(msg)
            self.stop()
        except Exception as e:
            self.logger.error(f"{e}")
            self.stop()

    def stop(self) -> None:
        self.logger.info("Stop Assessment")
