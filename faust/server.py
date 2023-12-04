import faust
from config import Config
from normalizer import normalize_data
import pymongo
app = faust.App(
    Config.FAUST_NAME,
    broker='kafka://localhost:9092',
    value_serializer='raw',
    topic_partitions=1,
    consumer_reconnect_max_retries=10,
)
topic = app.topic("klines")
client = pymongo.MongoClient(Config.DB_URL)
db = client["crypto_assessment"]


@app.agent(topic)
async def greet(payloads):
    async for payload in payloads:
        data = normalize_data(payload)
        collection = db[data["symbol"] + "_" + data["interval"]]
        print(collection.insert_one(data).inserted_id)

if __name__ == '__main__':
    print(client.list_database_names())
    app.main()
