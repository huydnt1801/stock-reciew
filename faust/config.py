import os
import json


class Config:
    LOG_FILE = f'{os.path.dirname(os.path.realpath(__file__))}/logs/assessment.log'
    FAUST_NAME = "data_loader"
    THRESH_HOLD = 1.01

    SYMBOL_LEN = int(os.getenv("SYMBOL_LEN"))

    KAFKA_BROKERS = json.loads(os.getenv("KAFKA_BROKERS"))
    DB_URL = os.getenv("DB_URL")

    OPENAI_KEY = os.getenv("OPENAI_KEY")
