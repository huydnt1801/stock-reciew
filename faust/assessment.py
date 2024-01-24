from config import Config
from utils.helper import *
from utils.logger import get_logger
import pandas as pd


class Assessment():
    def __init__(self, symbol, collection, data, hour_data, month_data):
        self.logger = get_logger("Assessment", Config.LOG_FILE)
        print(len(data))
        print(len(hour_data))
        self.collection = collection
        self.symbol = symbol
        self.data = pd.json_normalize(data)
        self.hour_data = hour_data[0]
        self.hour_data_indicator = hour_data
        self.month_data = month_data
        self.res = {}

    def price_indexes_change(self, data):
        increase_indexes = []
        reduce_indexes = []

        for index, row in data.iterrows():
            if index == 0:
                current_change = row
                continue
            if row['high'] > current_change['high']:
                increase_indexes.append(index)
                current_change = row
                continue
            if current_change['low'] > row['low']:
                reduce_indexes.append(index)
                current_change = row
                continue
        return increase_indexes, reduce_indexes

    def process(self):
        increase_indexes, reduce_indexes = self.price_indexes_change(
            self.data)
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

    def _price(self):
        max = self.hour_data["high"]
        min = self.hour_data["low"]
        msg = ""
        if self.month_data["high"] / max < 1.01 or min/self.month_data["low"] < 1.01: 
            max_time = min_time = ""
            try:
                max_time = "lúc " + convert_to_hour(self.data.iloc[7]["open_time"])
                min_time = "lúc " + convert_to_hour(self.data.iloc[45]["open_time"])
            except Exception as e:
                self.logger.error(e)
            msg = f"""\nTrong giờ qua, giá {self.symbol} cao nhất là: {max} {max_time} và thấp nhất là: {min} {min_time}"""

        return msg

    def _hour_price(self):
        percent = 0
        inc = red = 0
        end_price= self.hour_data["close"]
        start_price= self.hour_data["open"]
        for dat in self.hour_data_indicator:
            if dat["close"] > dat["open"]:
                inc += 1
            else:
                red += 1
        percent = (end_price/start_price - 1) * 100
        msg = ""
        if percent > 0:
            if percent >= 0.01:
                msg = f"""\nTrong giờ qua, giá {self.symbol} tăng {convert_percent(percent)}% từ {start_price} lên {end_price}"""
            # if red != 0 and inc/red > 1/3:
            #     msg = ""
        elif percent < 0:
            percent = -percent
            if percent >= 0.01:
                msg = f"""\nTrong giờ qua, giá {self.symbol} giảm {convert_percent(percent)}% từ {start_price} xuống {end_price}"""
            # if inc != 0 and red/inc > 1/3:
            #     msg = ""

        return msg

    def _change_number(self, cnt_change):
        if cnt_change > 40:
            msg = f"""\nGiá {self.symbol} trong giờ qua có nhiều biến động"""
        else:
            msg = ""

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
        msg = f"""\nTừ {convert_to_hour(max_volume_high_start["open_time"])} đến {convert_to_hour(max_volume_high_end["open_time"])} {self.symbol} tăng {convert_percent(max_volume_high_percent)}% với volume trung bình cao nhất {convert_percent(max_volume_high['volume_arg'])}/phút"""

        self.res.update({"volume_increase": {"start_time": int(max_volume_high_start["open_time"]), "end_time": int(max_volume_high_end[
                        "open_time"]), "percent": float(max_volume_high_percent), "value": float(max_volume_high['volume_arg'])}})
        # compare
        max_volume_low_start = self.data.iloc[max_volume_low['start_idx']].loc
        max_volume_low_end = self.data.iloc[max_volume_low['end_idx']].loc
        max_volume_low_percent = (
            1 - max_volume_low_end["low"] / max_volume_low_start["high"]) * 100
        msg += f"""\nTừ {convert_to_hour(max_volume_low_start["open_time"])} đến {convert_to_hour(max_volume_low_end["open_time"])} {self.symbol} giảm {convert_percent(max_volume_low_percent)}% với volume trung bình cao nhất {convert_percent(max_volume_low['volume_arg'])}/phút"""
        self.res.update({"volume_reduce": {"start_time": int(max_volume_low_start["open_time"]), "end_time": int(max_volume_low_end[
            "open_time"]), "percent": float(max_volume_low_percent), "value": float(max_volume_low['volume_arg'])}})
        return msg

    def analysis(self):
        msg = self._hour_price()
        msg += self._price()
        try:
            high, low, cnt_change = self.process()

            msg += self._change_number(cnt_change)
            msg += self._volume_analysis(high, low)
        except Exception as e:
            self.logger.info(e)
        return msg

    async def start(self):
        self.logger.info("Start Assessment")
        try:
            msg = self.analysis()
            self.logger.info(msg)
            # self.collection.insert_one({})
            self.stop()
            return msg
        except Exception as e:
            self.logger.error(f"{e}")
            self.stop()

    def stop(self) -> None:
        self.logger.info("Stop Assessment")
