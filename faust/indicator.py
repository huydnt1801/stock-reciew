class Indicator():
    def __init__(self, data):
        self.data = data
        # data 15 giai doan
        # typicalPrice = (max + min + close) / 3
        # typicalPrice and volume

    def MFI(self):
        positive = 0
        negative = 0
        prev = None
        for dat in self.data:
            typicalPrice = (dat["max"] + dat["min"] + dat["close"]) / 3
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
