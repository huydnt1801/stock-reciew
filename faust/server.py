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
topic = app.topic("klines")
client = pymongo.MongoClient(Config.DB_URL)
db = client["crypto_assessment"]
metadata = {}


@app.agent(topic)
async def greet(payloads):
    async for payload in payloads:
        data = normalize_data(payload)
        if metadata.get(data["symbol"], None) is not None:
            metadata[data["symbol"]].append(data)
        else:
            metadata[data["symbol"]] = [data]
        print(len(metadata[data["symbol"]]))
        if len(metadata[data["symbol"]]) > 10:
            assessment = Assessment(data["symbol"], metadata[data["symbol"]])
            metadata[data["symbol"]] = []
            await assessment.start()

if __name__ == '__main__':
    print(client.list_database_names())
    app.main()
