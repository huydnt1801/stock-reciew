
import pymongo
from datetime import datetime
from assessment import Assessment
from config import Config
from gpt import generate_new


def convert_percent(percent):
    return round(percent, 2)


def convert_to_date(timestamp):
    dt_object = datetime.fromtimestamp(timestamp/1000)
    return dt_object


def main():
    client = pymongo.MongoClient(Config.DB_URL)
    db = client["crypto_assessment"]

    msg = ""
    for symbol in Config.SYMBOLS:
        collection = db[symbol]
        cursor = collection.find().limit(1).sort([('$natural', -1)])
        data = dict(cursor[0])
        current = data["current"]
        medium = data["medium"]

        if current["daily_price"]["percent"] > 0.01 and current["daily_price"]["percent"] > medium["daily_price"]:
            if current["daily_price"]["type"] == 1:
                msg += f"""\nTrong giờ qua, giá {symbol} tăng {convert_percent(current["daily_price"]["percent"])}%"""
            else:
                msg += f"""\nTrong giờ qua, giá {symbol} giảm {convert_percent(current["daily_price"]["percent"])}%"""

        if current["price"]["max"] > medium["price"]["max"] or current["price"]["min"] < medium["price"]["min"]:
            msg += f"""\nTrong giờ qua, giá {symbol} cao nhất là: {current["price"]["max"]} lúc {convert_to_date(current["price"]["max_time"])} và thấp nhất là: {current["price"]["min"]} lúc {convert_to_date(current["price"]["min_time"])}"""

        if current["change_number"] > 20:
            msg += f"""\nGiá {symbol} trong giờ qua có rất nhiều biến động"""
        # elif current["change_number"] > 15:
        #     msg += f"""\nGiá {symbol} trong giờ qua có khá nhiều biến động"""

        if current["volume_increase"]["value"] > medium["volume_increase"] * 1.1:
            msg += f"""\nTừ {convert_to_date(current["volume_increase"]["start_time"])} đến {convert_to_date(current["volume_increase"]["end_time"])} {symbol} tăng {convert_percent(current["volume_increase"]["percent"])}% với volume trung bình cao nhất {current["volume_increase"]["value"]}/phút"""

        if current["volume_reduce"]["value"] > medium["volume_reduce"] * 1.1:
            msg += f"""\nTừ {convert_to_date(current["volume_reduce"]["start_time"])} đến {convert_to_date(current["volume_reduce"]["end_time"])} {symbol} giảm {convert_percent(current["volume_reduce"]["percent"])}% với volume trung bình cao nhất {current["volume_reduce"]["value"]}/phút"""
    content = generate_new(msg)
    print(content)


if __name__ == '__main__':
    main()
