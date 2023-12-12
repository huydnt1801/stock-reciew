import os

BINANCE_LICENSE_TOKEN = 'f639bb70-977e-41a5-a420-t7f52c1fe9f42'
BINANCE_API_SECRET = '339495bcd9a13b3434d847a9863fa155720cd914711d7fc53ce326f6adca799e'


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

    SUBCRIBE_CHANNELS = ['kline_1m']

    TICKER_INFO_EVENT_TYPE = "24hrTicker"
    KLINES_EVENT_TYPE = "kline"
    TICKER_INFO_KAFKA_TOPIC = "ticker.24h-info"
    KLINES_KAFKA_TOPIC = "klines"

    BINANCE_INFO_URL = "https://www.binance.com/bapi/composite/v1/public/marketing/symbol/list?nocache"
