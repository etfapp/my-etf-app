import pandas as pd
import os

def load_etf_summary():
    path = os.path.join("data", "etf_summary.csv")
    try:
        return pd.read_csv(path)
    except Exception as e:
        return pd.DataFrame(columns=["代碼", "名稱", "殖利率", "價格", "技術燈號"])

def load_watchlist():
    path = os.path.join("data", "watchlist.csv")
    try:
        return pd.read_csv(path)
    except:
        return pd.DataFrame(columns=["代碼"])

def save_watchlist(df):
    path = os.path.join("data", "watchlist.csv")
    df.to_csv(path, index=False)