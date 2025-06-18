# 📊 MyETF 助手系統

這是一套智慧化的台股 ETF 投資助理 App，整合技術與基本面分析、動態推薦、位階評估與提醒機制，適合個人長期投資使用。

---

## 🚀 如何安裝與啟動

### 1️⃣ 安裝 Python 環境（建議 Python 3.10 以上）
建議使用 [Anaconda](https://www.anaconda.com/) 或手動安裝 Python。

### 2️⃣ 安裝依賴套件
打開終端機（Terminal 或 CMD），切換到資料夾後執行：

```
pip install -r requirements.txt
```

### 3️⃣ 執行 App
```
streamlit run app/main.py
```

---

## 📁 專案結構說明

```
MyETF助手/
├── app/                   # 主應用程式
│   └── main.py
├── updater/               # 每日資料更新模組
│   └── data_updater.py
├── pages/                 # 各分頁模組（預留）
├── utils/                 # 工具程式模組（預留）
├── data/                  # CSV 原始資料
│   ├── etf_data.csv
│   └── watchlist.csv
├── logs/                  # 更新紀錄 Log
│   └── update.log
├── .streamlit/            # Streamlit 執行設定
│   └── config.toml
├── requirements.txt       # 依賴套件
└── README.md              # 使用說明（本檔）
```

---

## 🔧 自動資料更新

請執行：

```
python updater/data_updater.py
```

若成功更新，會寫入 `logs/update.log`，失敗也會記錄錯誤原因。

---

## 📸 預期畫面說明

主畫面包含：
- 今日市場溫度與建議佈局
- ETF 總表（殖利率、位階等）
- 動態清單推薦
- 自選清單與水位／存股計算機
- 升溫區警示提示

📌 若需畫面圖檔可聯繫作者補充。

---

## 📬 聯絡與建議

如有功能建議、Bug 回報，請透過 GitHub 或訊息聯繫開發者。
