import datetime
import faust
from config import Config
from normalizer import normalize_data
import pymongo
from assessment import Assessment
from indicator import Indicator
from gpt import generate_new

app = faust.App(
    Config.FAUST_NAME,
    broker=['kafka://localhost:19092',
            'kafka://localhost:29092', 'kafka://localhost:39092'],
    value_serializer='raw',
    consumer_reconnect_max_retries=10,
)
min_topic = app.topic("klinemin")
hour_topic = app.topic("klinehour")
mon_topic = app.topic("klinemon")
client = pymongo.MongoClient(Config.DB_URL)
db = client["crypto_assessment"]
metadata = {}


@app.agent(min_topic)
async def greet_min(payloads):
    async for payload in payloads:
        data = normalize_data(payload)
        if metadata.get(data["symbol"], None) is not None:
            metadata[data["symbol"]].append(data)
        else:
            metadata[data["symbol"]] = [data]


@app.agent(hour_topic)
async def greet_hour(payloads):
    async for payload in payloads:
        data = normalize_data(payload)
        collection = db[data["symbol"]]
        res = collection.insert_one({
            "event_time": data["open_time"],
            "open": data["open"],
            "high": data["high"],
            "low": data["low"],
            "close": data["close"],
            "volume": data["volume"],
        })
        print(res.inserted_id)


@app.agent(mon_topic)
async def greet_mon(payloads):
    msg_summary = ""
    symbol_list = set()
    async for payload in payloads:
        data = normalize_data(payload)
        collection = db[data["symbol"]]
        hour_data = list(collection.find().sort({"_id": -1}).limit(15))
        min_data = metadata.get(data["symbol"], [])
        assessment = Assessment(
            data["symbol"], collection, min_data, hour_data, data)
        metadata[data["symbol"]] = []
        msg = await assessment.start()

        # indicator
        indicator = Indicator(data["symbol"], hour_data)
        msg += indicator.indicator_msg()

        msg_summary += msg
        symbol_list.add(data["symbol"])
        if len(symbol_list) == Config.SYMBOL_LEN:
            try:
                message = generate_new(msg_summary)
                new = db["news"].insert_one({
                    "event_time": hour_data[0]["event_time"],
                    "message": message,
                })
                print("news_id: " + str(new.inserted_id))
            except Exception as e:
                print(e)
            symbol_list = set()

if __name__ == '__main__':
    app.main()
