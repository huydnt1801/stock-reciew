import os
from flask import Flask, request, json
from flask.json import jsonify
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

try:
    client = MongoClient(
        f"{os.getenv('DB_URL', 'mongodb+srv://tienhuy1801:nt030201@cluster0.b2zl2.mongodb.net/')}", authSource="admin")
    db = client['crypto_assessment']
except:
    print(os.getenv('DB_URL'))
    print("failed to connect DB")
app = Flask(__name__)
json.provider.DefaultJSONProvider.ensure_ascii = False
CORS(app)

@app.route("/api/v1/news")
def home_page():
    try:
        args = request.args.to_dict()
        limit = int(args.get("pageSize", 8))
        skip = (int(args.get("page", 1)) - 1)*limit
        cursor = db.news.find().skip(skip).sort({"_id": -1}).limit(limit)
        res = []
        if cursor is not None:
            for x in cursor:
                x["_id"] = str(x["_id"])
                msg = x["message"].split("\n\n")[1:]
                x["message"] = "\n\n".join(msg)
                x["event_time"] = x["event_time"] + 3600000
                res.append(x)
        return jsonify(res), 200
    except Exception as e:
        print(e)
        return "invalid param", 400


@app.route("/api/v1/news/<new_id>")
def new(new_id):
    try:
        res = db.news.find_one({"_id": ObjectId(new_id)})
        print(res)
        res["_id"] = str(res["_id"])
        msg = res["message"].split("\n\n")[1:]
        res["message"] = "\n\n".join(msg)
        return jsonify(res), 200
    except Exception as e:
        print(e)
        return "", 404


@app.route("/health/check")
def health():
    return "", 200


@app.route("/health/ready")
def ready():
    return "", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
