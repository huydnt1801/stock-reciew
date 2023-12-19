import faust
from config import Config
from normalizer import normalize_data
import pymongo
from assessment import Assessment

app = faust.App(
    Config.FAUST_NAME,
    broker='kafka://localhost:9092',
    value_serializer='raw',
    topic_partitions=1,
    consumer_reconnect_max_retries=10,
)
min_topic = app.topic("klinemin")
mon_topic = app.topic("klinemon")
client = pymongo.MongoClient(Config.DB_URL)
db = client["crypto_assessment"]
metadata = {}


@app.agent(min_topic)
async def greet(payloads):
    async for payload in payloads:
        data = normalize_data(payload)
        if metadata.get(data["symbol"], None) is not None:
            metadata[data["symbol"]].append(data)
        else:
            metadata[data["symbol"]] = [data]


@app.agent(mon_topic)
async def greet(payloads):
    async for payload in payloads:
        data = normalize_data(payload)
        assessment = Assessment(
            db[data["symbol"]], data["symbol"], metadata[data["symbol"]])
        metadata[data["symbol"]] = []
        await assessment.start()

if __name__ == '__main__':
    app.main()
