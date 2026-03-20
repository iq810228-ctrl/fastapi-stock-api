import requests
from config import STOCK_API_URL

def get_stock_price(ticker: str):
    url = STOCK_API_URL.format(ticker=ticker)
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
        data = response.json()
        msg_array = data.get("msgArray")
        if not msg_array:
            return None

        stock = msg_array[0]
        price_str = stock.get("z")
        time_str = stock.get("t")

        if not price_str or price_str == "-":
            return None

        return {
            "ticker": ticker,
            "price": float(price_str),
            "time": time_str
        }
    except Exception as e:
        print(f"抓 {ticker} 股價錯誤:", e)
        return None