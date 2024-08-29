import time
import requests

url = "https://api.binance.com/api/v3/ticker/price"
params = {
    "symbol": "BTCUSDT"
}

while True:
    response = requests.get(url, params=params)

    data = response.json()
    print(f"Price of BTC/USDT: {data['price']}")
    time.sleep(1)