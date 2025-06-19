
import pandas as pd
import os

def load_data(filename):
    filepath = os.path.join("data", filename)
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        return pd.DataFrame()

def get_today_strategy():
    # 範例：根據市場條件返回保守/平衡/積極（簡化版）
    return "平衡型"

def format_update_time():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_etf_data():
    return load_data("etf_summary.csv")

def get_dynamic_etfs(df):
    return df[df.get("技術燈號") == "低"]
