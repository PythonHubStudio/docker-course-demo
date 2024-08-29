from flask import Flask, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mymongo:27017")
db = client['crypto_database']
collection = db['btc_usdt_prices']

@app.route('/data')
def get_data():
    data = collection.find().sort("timestamp", -1).limit(50)
    data = [{"timestamp": item["timestamp"], "price": float(item["price"])} for item in data]
    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
