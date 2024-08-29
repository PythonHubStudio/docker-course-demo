import time
from datetime import datetime
import requests
from pymongo import MongoClient


# client = MongoClient("mongodb://localhost:27017")
client = MongoClient("mongodb://root:example@mymongo:27017")

db = client['crypto_database']

collection = db['btc_usdt_prices']

url = "https://api.binance.com/api/v3/ticker/price"
params = {"symbol": "BTCUSDT"}

while True:
    response = requests.get(url, params=params)
    data = response.json()
    
    timestamp = datetime.now().isoformat()
    price_data = {
        "symbol": params["symbol"],
        "price": data['price'],
        "timestamp": timestamp
    }
    print(f"Price of BTC/USDT: {data['price']} at {timestamp}")

    collection.insert_one(price_data)

    time.sleep(5)
