from fastapi import FastAPI
from services import fetch_and_save
from database import SessionLocal
from models import Stock
from datetime import datetime, timezone
from crawler import get_stock_price
import scheduler  # 啟動排程

app = FastAPI(
    title="TW Stock Price API",
    description="即時股價與歷史股價查詢 API",
    version="1.0.0"
)

@app.get("/stock-price")
def stock_price(ticker: str):
    data = get_stock_price(ticker)
    if not data:
        return {"error": "查無資料或 API 異常"}

    # 同步更新資料庫
    db = SessionLocal()
    try:
        stock = db.query(Stock).filter(Stock.ticker == ticker).first()
        if stock:
            stock.price = data["price"]
            stock.timestamp = datetime.now(timezone.utc)  # type: ignore
        else:
            stock = Stock(
                ticker=data["ticker"],
                price=data["price"],
                timestamp=datetime.now(timezone.utc)
            )
            db.add(stock)
        db.commit()
    finally:
        db.close()

    return {
        "ticker": data["ticker"],
        "price": data["price"],
        "time": data["time"]
    }

# ==============================
# 新增：查資料庫所有股票紀錄
# ==============================
@app.get("/stocks")
def get_stocks():
    db = SessionLocal()
    try:
        stocks = db.query(Stock).all()
        return [
            {
                "ticker": s.ticker,
                "price": s.price,
                "timestamp": s.timestamp
            }
            for s in stocks
        ]
    finally:
        db.close()