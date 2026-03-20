from apscheduler.schedulers.background import BackgroundScheduler
from config import TRACKED_TICKERS, FETCH_INTERVAL_MINUTES
from services import fetch_and_save

scheduler = BackgroundScheduler()

def fetch_all():
    for ticker in TRACKED_TICKERS:
        fetch_and_save(ticker)

scheduler.add_job(fetch_all, "interval", minutes=FETCH_INTERVAL_MINUTES)
scheduler.start()
print("排程啟動，每", FETCH_INTERVAL_MINUTES, "分鐘抓股價")