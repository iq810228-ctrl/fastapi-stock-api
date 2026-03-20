from database import SessionLocal
from models import Stock
from config import TRACKED_TICKERS
from datetime import datetime, timezone

def init_stocks():
    db = SessionLocal()
    try:
        for ticker in TRACKED_TICKERS:
            stock = db.query(Stock).filter(Stock.ticker == ticker).first()
            if not stock:
                new_stock = Stock(
                    ticker=ticker,
                    price=None,  # 初始化先沒價格
                    timestamp=datetime.now(timezone.utc)
                )
                db.add(new_stock)
        db.commit()
        print("初始化股票完成！")
    finally:
        db.close()

if __name__ == "__main__":
    init_stocks()