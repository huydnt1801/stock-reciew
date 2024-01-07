import os


class Config:
    LOG_FILE = f'{os.path.dirname(os.path.realpath(__file__))}/logs/assessment.log'
    FAUST_NAME = "data_loader"
    THRESH_HOLD = 1.000001

    DB_URL = "mongodb://admin:admin@localhost:27017/"
