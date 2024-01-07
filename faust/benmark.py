import pymongo
from datetime import datetime
from config import Config
client = pymongo.MongoClient(Config.DB_URL)
db = client["crypto_assessment"]
collection = db["test"]

start = datetime.now()
print(collection.find_one())
end = datetime.now()
print((end-start).total_seconds() * 1000)