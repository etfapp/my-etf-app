import pandas as pd
import os

def load_etf_summary():
    path = os.path.join("data", "etf_summary.csv")
    try:
        return pd.read_csv(path)
    except Exception as e:
        return pd.DataFrame(columns=["代碼", "名稱", "殖利率", "價格", "技術燈號"])