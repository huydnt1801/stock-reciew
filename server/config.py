import os


class Config:
    LOG_FILE = f'{os.path.dirname(os.path.realpath(__file__))}/logs/assessment.log'
    TYPE = ['giờ']
    SYMBOLS = ["BTCUSDT", "LUNAUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT",
               "DOGEUSDT", "ETHBTC", "BNBBTC",  "SOLBTC",
               "SHIBUSDT", "TRXBTC", "SOLUSDT"]
    # SYMBOLS = ["BTCUSDT", "ETHUSDT"]"DOGEBTC"
    THRESH_HOLD = 1.000001
    THRESH_HOLD_SECOND = 1.0001
    DB_URL = "mongodb+srv://tienhuy1801:nt030201@cluster0.b2zl2.mongodb.net/"
