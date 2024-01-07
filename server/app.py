from datetime import datetime
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://admin:admin@localhost:27017/crypto_assessment",authSource="admin")
db = client['crypto_assessment']

@app.route("/api/v1/news")
def home_page():
    x = db.test.find_one()
    return x, 200