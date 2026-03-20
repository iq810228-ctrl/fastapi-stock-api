from database import SessionLocal
from models import Stock
from crawler import get_stock_price
from datetime import datetime, timezone

def fetch_and_save(ticker: str):
    data = get_stock_price(ticker)
    if not data:
        return
    db = SessionLocal()
    try:
        stock = db.query(Stock).filter(Stock.ticker == ticker).first()
        if stock:
            stock.price = data["price"]
            stock.timestamp = datetime.now(timezone.utc)
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