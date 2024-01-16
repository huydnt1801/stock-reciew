from flask import Flask, request, json
from flask.json import jsonify
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
json.provider.DefaultJSONProvider.ensure_ascii = False
CORS(app)
client = MongoClient(
    "mongodb://admin:admin@localhost:27017/crypto_assessment", authSource="admin")
db = client['crypto_assessment']

@app.route("/api/v1/news")
def home_page():
    try:
        args = request.args.to_dict()
        limit = int(args.get("pageSize", 8))
        skip = (int(args.get("page", 1)) - 1)*limit
        cursor = db.news.find().skip(skip).sort({"_id": -1}).limit(limit)
        res = []
        for x in cursor:
            x["_id"] = str(x["_id"])
            res.append(x)
        return jsonify(res), 200
    except:
        return "invalid param", 400


@app.route("/api/v1/news/<new_id>")
def new(new_id):
    try:
        res = db.news.find_one({"_id": ObjectId(new_id)})
        res["_id"] = str(res["_id"])
        return jsonify(res), 200
    except:
        return "", 404


@app.route("/health/check")
def health():
    return "", 200


@app.route("/health/ready")
def ready():
    return "", 200


if __name__ == '__main__':
    app.run()
