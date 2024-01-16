from utils.helper import *


class Indicator():
    def __init__(self, symbol, data):
        self.data = data
        self.symbol = symbol

    def MFI(self):
        if len(self.data) < 15:
            return 0
        positive = 0
        negative = 0
        prev = None
        for dat in self.data:
            typicalPrice = (dat["high"] + dat["low"] + dat["close"]) / 3
            if prev is None:
                prev = typicalPrice
                continue
            if typicalPrice > prev:
                positive += typicalPrice * dat["volume"]
            elif typicalPrice < prev:
                negative += typicalPrice * dat["volume"]
            prev = typicalPrice

        if positive + negative == 0:
            return 0
        return 100 - (100 * negative / (positive + negative))

    def RSI(self):
        if len(self.data) < 15:
            return 0
        positive = []
        negative = []
        prev = None
        for dat in self.data:
            typicalPrice = dat["close"]
            if prev is None:
                prev = typicalPrice
                continue
            if typicalPrice > prev:
                positive.append(typicalPrice - prev)
            elif typicalPrice < prev:
                negative.append(prev - typicalPrice)
            prev = typicalPrice

        averagePositive = sum(positive) / len(positive)
        averageNegative = sum(negative) / len(negative)
        if averagePositive + averageNegative == 0:
            return 0
        return 100 - (100 * averageNegative / (averagePositive + averageNegative))

    def indicator_msg(self):
        rsi = convert_percent(self.RSI())
        mfi = convert_percent(self.MFI())
        time = convert_to_hour(self.data[0]['event_time'] + 3600000)
        msg = ""
        if rsi != 0 and mfi != 0:
            msg += f"{self.symbol} có chỉ báo RSI đạt {rsi} và MFI đạt {mfi} lúc {time}"
        elif rsi != 0:
            msg += f"{self.symbol} có chỉ báo RSI đạt {rsi} lúc {time}"
        elif mfi != 0:
            msg += f"{self.symbol} có chỉ báo MFI đạt {mfi} lúc {time}"
        return msg
