import os

BINANCE_LICENSE_TOKEN = 'd7bdb376-7cc7-4948-b835-t770d1cdc4a98'
BINANCE_API_SECRET = '15cd20176434f5188135d0ae4487621e7a900fc7d2e3e47c3e36ab07f36e7f35'


class Config:
    LOG_FILE = f'{os.path.dirname(os.path.realpath(__file__))}/logs/data_collector.log'
    SYMBOL_LIST = [
        "btcusdt", "ethusdt", "dogeusdt", "bnbusdt",
        "xrpusdt", "adausdt", "shibusdt",  "solusdt"
    ]

    SUBCRIBE_CHANNELS = ['kline_1m', 'kline_1h', 'kline_1M']

    KLINE_MINUTES_TOPIC = "klinemin"
    KLINE_HOUR_TOPIC = "klinehour"
    KLINE_MONTH_TOPIC = "klinemon"

    DB_URL = "mongodb://admin:admin@localhost:27017/"
