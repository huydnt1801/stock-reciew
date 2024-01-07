import datetime
import faust
from config import Config
from normalizer import normalize_data
import pymongo
from assessment import Assessment

app = faust.App(
    Config.FAUST_NAME,
    broker=['kafka://localhost:19092',
            'kafka://localhost:29092', 'kafka://localhost:39092'],
    value_serializer='raw',
    topic_partitions=1,
    consumer_reconnect_max_retries=10,
)
min_topic = app.topic("klinemin")
hour_topic = app.topic("klinehour")
mon_topic = app.topic("klinemon")
client = pymongo.MongoClient(Config.DB_URL)
db = client["crypto_assessment"]
metadata = {}
hour_data = {}


@app.agent(min_topic)
async def greet(payloads):
    async for payload in payloads:
        data = normalize_data(payload)
        if metadata.get(data["symbol"], None) is not None:
            metadata[data["symbol"]].append(data)
        else:
            metadata[data["symbol"]] = [data]

# save data for indicator


@app.agent(hour_topic)
async def greet(payloads):
    async for payload in payloads:
        data = normalize_data(payload)
        if hour_data.get(data["symbol"], None) is not None:
            hour_data[data["symbol"]].append(data)
        else:
            hour_data[data["symbol"]] = [data]


@app.agent(mon_topic)
async def greet(payloads):
    async for payload in payloads:
        data = normalize_data(payload)
        start = datetime.now()
        assessment = Assessment(
            db[data["symbol"]],  metadata[data["symbol"]], hour_data[data["symbol"]], data)
        metadata[data["symbol"]] = []
        metadata[data["symbol"]] = {}
        await assessment.start()
        end = datetime.now()
        print((end-start).total_seconds() * 1000)

if __name__ == '__main__':
    app.main()
