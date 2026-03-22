# TW Stock Price API

使用 FastAPI 開發的台股股價查詢系統，包含即時資料抓取、資料庫儲存與定時更新功能。

---

## 專案簡介

此專案提供台股即時股價查詢 API，並將資料儲存於資料庫中，方便後續查詢。

除了手動查詢外，也透過排程機制自動更新股價。

---

## 使用技術

- Python
- FastAPI
- SQLAlchemy
- SQLite
- APScheduler
- Requests

---

## 功能

### 1. 即時股價查詢


GET /stock-price?ticker=2330


- 抓取即時股價
- 同時寫入資料庫

---

### 2. 查詢資料庫紀錄


GET /stocks


- 回傳所有已儲存的股價資料

---

### 3. 自動更新股價

- 使用 APScheduler
- 每 5 分鐘自動抓取股價
- 寫入資料庫

---
## 專案結構

```
fastapi-stock-api/
├─ main.py          # FastAPI app 主程式
├─ config.py        # 設定自動抓股的股票清單
├─ models.py        # 資料庫 ORM 定義
├─ database.py      # 資料庫連線
├─ crawler.py       # 抓即時股價程式
├─ services.py      # 處理業務邏輯
├─ scheduler.py     # APScheduler 排程
├─ init_db.py       # 初始化資料庫
├─ add_stock.py     # 新增初始股票
├─ requirements.txt
└─ README.md
```

安裝與使用

Clone 專案：

git clone https://github.com/iq810228-ctrl/fastapi-stock-api.git
cd fastapi-stock-api

安裝依賴套件：

pip install -r requirements.txt

建立資料表：

python init_db.py

新增初始股票：

python add_stock.py

啟動 FastAPI：

uvicorn main:app --reload

Swagger UI: http://127.0.0.1:8000/docs
