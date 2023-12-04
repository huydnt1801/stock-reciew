import os

BINANCE_LICENSE_TOKEN = '20936088-a4c3-4e70-bcfe-t7db977d74575'
BINANCE_API_SECRET = '36b7e177c85f1afc90cb6f621cd799c634b73c282929347c8b650d663f10e023'


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

    SUBCRIBE_CHANNELS = ['depth']  # 'ticker',kline_1m

    TICKER_INFO_EVENT_TYPE = "24hrTicker"
    KLINES_EVENT_TYPE = "kline"
    TICKER_INFO_KAFKA_TOPIC = "ticker.24h-info"
    KLINES_KAFKA_TOPIC = "klines"

    BINANCE_INFO_URL = "https://www.binance.com/bapi/composite/v1/public/marketing/symbol/list?nocache"
