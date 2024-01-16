import os


class Config:
    LOG_FILE = f'{os.path.dirname(os.path.realpath(__file__))}/logs/assessment.log'
    FAUST_NAME = "data_loader"
    THRESH_HOLD = 1.000001

    SYMBOL_LEN = 1

    DB_URL = "mongodb://admin:admin@localhost:27017/"

    OPENAI_KEY = "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"
