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

    return load_data("etf_summary.csv")

    return df[df.get("技術燈號") == "低"]

def load_etf_data():
    """
    讀取 ETF 資料並處理欄位格式與缺漏值
    """
    df = load_data("etf_summary.csv")
    if df.empty:
        return df

    # 確保必要欄位存在
    required_columns = ["技術燈號", "RSI百分位", "殖利率百分位", "基本面總分"]
    for col in required_columns:
        if col not in df.columns:
            df[col] = None

    # 將數值欄位轉為 float（若無法轉換則為 NaN）
    for col in ["RSI百分位", "殖利率百分位", "基本面總分"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

def get_dynamic_etfs(df):
    """
    從 ETF 總表中挑出目前「位階低且基本面佳」的標的
    """
    df = df.copy()
    conditions = (
        (df["技術燈號"] == "低") &
        (df["RSI百分位"] < 30) &
        (df["殖利率百分位"] > 70) &
        (df["基本面總分"] >= 70)
    )
    return df[conditions].reset_index(drop=True)