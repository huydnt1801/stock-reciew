import os
import json


class Config:
    LOG_FILE = f'{os.path.dirname(os.path.realpath(__file__))}/logs/assessment.log'
    FAUST_NAME = "data_loader"
    THRESH_HOLD = 1.01

    SYMBOL_LEN = 1

    KAFKA_BROKERS = json.loads(os.getenv("KAFKA_BROKERS"))
    DB_URL = os.getenv("DB_URL")

    OPENAI_KEY = "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"
