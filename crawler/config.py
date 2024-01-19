import os
import json

BINANCE_LICENSE_TOKEN = os.getenv("BINANCE_LICENSE_TOKEN")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")


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

    DB_URL = os.getenv("DB_URL")
    KAFKA_BROKERS = json.loads(os.getenv("KAFKA_BROKERS"))