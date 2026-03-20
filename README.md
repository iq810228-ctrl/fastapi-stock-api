# TW Stock Price API

 即時台股股價查詢與歷史紀錄 API，使用 FastAPI + SQLite + APScheduler 實作

## 專案簡介

TW Stock Price API 是一個 FastAPI 後端專案，提供台灣股票即時價格查詢與資料庫紀錄功能。  
核心功能包括：

- 抓取台股即時股價並更新資料庫
- 提供資料庫內股票紀錄查詢 API
- 背景定時抓取股票價格（每 5 分鐘一次）
- Swagger UI 自動生成 API 文件，方便測試

專案涵蓋 Python 後端開發、RESTful API 設計、資料庫操作與排程管理的實務應用。

## 技術堆疊

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- APScheduler
- Requests

## 專案結構


fastapi-stock-api/
├─ main.py
├─ config.py
├─ models.py
├─ database.py
├─ crawler.py
├─ services.py
├─ scheduler.py
├─ init_db.py
├─ add_stock.py
├─ requirements.txt
└─ README.md


## 主要功能

### 1. 抓取即時股價
- Endpoint: `GET /stock-price?ticker=<股票代碼>`
- 功能：抓即時股價，並同步更新資料庫
- 範例回傳：
```json
{
  "ticker": "2330",
  "price": 599.0,
  "time": "15:12:34"
}

2. 查資料庫股票紀錄

Endpoint: GET /stocks

功能：查詢資料庫內的股票紀錄

範例回傳：

[
  {"ticker": "2330", "price": 599.0, "timestamp": "2026-03-20T15:12:34"},
  {"ticker": "2317", "price": 95.5, "timestamp": "2026-03-20T15:12:35"}
]

3. 背景定時抓股價

使用 APScheduler，每 5 分鐘自動抓 config.py 中設定的股票

抓取到的股價會寫入資料庫

無需人工操作

安裝與使用

Clone 專案：

git clone https://github.com/iq810228-ctrl/fastapi-stock-api.git
cd fastapi-stock-api

建議使用 virtualenv：

python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

安裝依賴套件：

pip install -r requirements.txt

建立資料表：

python init_db.py

（可選）新增初始股票：

python add_stock.py

啟動 FastAPI：

uvicorn main:app --reload

Swagger UI: http://127.0.0.1:8000/docs

配置

config.py：

TRACKED_TICKERS = ["2330", "2317"]  # 自動抓取的股票清單
資料庫結構

SQLite 檔案： stocks.db

Table: stocks

欄位：

id：自動遞增

ticker：股票代碼

price：最新股價

timestamp：最後更新時間

查看資料庫：

sqlite3 stocks.db
.tables
SELECT * FROM stocks;
.exit