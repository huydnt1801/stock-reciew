import os


class Config:
    LOG_FILE = f'{os.path.dirname(os.path.realpath(__file__))}/logs/assessment.log'
    FAUST_NAME = "data_loader"
    KLINES_KAFKA_TOPIC = "klines"
    THRESH_HOLD = 1.000001

    KAFKA_CONFIG = {
        "bootstrap.servers": "localhost:9092",
        "group.id": "data_loader",
        "auto.offset.reset": "earliest",
        "enable.auto.commit": False
    }

    DB_URL = "mongodb+srv://tienhuy1801:nt030201@cluster0.b2zl2.mongodb.net/"
