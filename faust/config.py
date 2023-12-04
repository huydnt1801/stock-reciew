import os


class Config:
    FAUST_NAME = "data_loader"
    TICKER_INFO_KAFKA_TOPIC = "ticker.24h-info"
    KLINES_KAFKA_TOPIC = "klines"

    KLINES_INTERVAL = ["1m", "1h", "1d", "1w", "1M"]

    KAFKA_CONFIG = {
        "bootstrap.servers": "localhost:9092",
        "group.id": "data_loader",
        "auto.offset.reset": "earliest",
        "enable.auto.commit": False
    }

    DB_URL = "mongodb+srv://tienhuy1801:nt030201@cluster0.b2zl2.mongodb.net/"