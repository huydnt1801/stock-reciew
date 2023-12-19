import os

BINANCE_LICENSE_TOKEN = '00508345-8bd5-4c58-88db-t7813ac54794a'
BINANCE_API_SECRET = '45409974daefb4f9f62d08f1a06b56cdaf23bbea691a367a3bfa0ffe7234a184'


class Config:
    LOG_FILE = f'{os.path.dirname(os.path.realpath(__file__))}/logs/data_collector.log'
    KAFKA_CONFIG = {
        "bootstrap.servers": "localhost:9092",
        # "client.id": "data_collector"
    }
    SYMBOL_LIST = [
        "btcusdt", "lunausdt", "ethusdt", "bnbusdt", "xrpusdt",
        "dogeusdt", "ethbtc", "bnbbtc", "dogebtc", "solbtc",
        "shibusdt", "trxbtc", "solusdt"
    ]

    SUBCRIBE_CHANNELS = ['kline_1m', 'kline_1M']

    KLINE_MINUTES_TOPIC = "klinemin"
    KLINE_MONTH_TOPIC = "klinemon"
