from datetime import datetime


def convert_to_date(timestamp):
    dt_object = datetime.fromtimestamp(timestamp/1000)
    return dt_object


def convert_to_hour(timestamp):
    dt_object = datetime.fromtimestamp(timestamp/1000)
    return f"{dt_object.hour}:{dt_object.minute}"


def get_second(start, end):
    duration = end - start
    return duration / 1000


def get_minute(start, end):
    duration = end - start
    return duration / 1000 / 60


def convert_percent(percent):
    return round(percent, 2)
