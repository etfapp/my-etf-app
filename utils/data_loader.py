import streamlit as st
import pandas as pd
import os

def load_summary_data():
    """
    載入 ETF 總表資料，並標準化必要欄位格式
    """
    filepath = os.path.join("data", "etf_summary.csv")
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        return pd.DataFrame()

    # 確保重要欄位存在
    required_columns = [
        "代碼", "名稱", "技術燈號",
        "殖利率百分位", "RSI百分位", "基本面總分"
    ]
    for col in required_columns:
        if col not in df.columns:
            df[col] = None

    # 數值欄位轉換
    for col in ["殖利率百分位", "RSI百分位", "基本面總分"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

def load_watchlist():
    """
    載入自選清單資料，並確保欄位一致性
    """
    filepath = os.path.join("data", "watchlist.csv")
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        return pd.DataFrame()

    # 確保常用欄位
    required_columns = ["代碼", "名稱", "目前價格", "殖利率", "技術燈號", "建議股數"]
    for col in required_columns:
        if col not in df.columns:
            df[col] = None

    return df

def load_heat_zone():
    """
    載入升溫區資料，並確保關鍵欄位存在
    """
    filepath = os.path.join("data", "heat_zone.csv")
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        return pd.DataFrame()

    # 確保欄位標準化
    required_columns = ["代碼", "名稱", "技術燈號", "RSI百分位", "殖利率百分位", "升溫原因"]
    for col in required_columns:
        if col not in df.columns:
            df[col] = None

    # 數值欄位轉換
    for col in ["RSI百分位", "殖利率百分位"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

def save_watchlist(df):
    """儲存自選清單資料到 CSV"""
    filepath = os.path.join("data", "watchlist.csv")
    df.to_csv(filepath, index=False)


__all__ = ['load_watchlist', 'save_watchlist', 'load_etf_summary', 'load_heat_zone']
