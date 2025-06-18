
import streamlit as st
import pandas as pd
import os

# 避免欄位錯誤
try:
    df = pd.read_csv("data/watchlist.csv")
    required_columns = ['代碼', '名稱', '價格', '殖利率', '技術燈號']
    for col in required_columns:
        if col not in df.columns:
            df[col] = None
except Exception as e:
    st.error(f"讀取自選清單失敗：{e}")

st.title("📂 我的自選清單")
