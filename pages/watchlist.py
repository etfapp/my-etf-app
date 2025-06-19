import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from utils.data_loader import load_watchlist, save_watchlist
from utils.data_loader import load_watchlist
import pandas as pd

def app():
    st.title("⭐ 自選清單")
    try:
        df = load_watchlist()
        st.dataframe(df)

    for i, row in df.iterrows():
        code = row["代碼"]
        if st.button(f"🗑️ 移除 - {code}", key=f"del_{code}"):
            df = df[df["代碼"] != code].reset_index(drop=True)
            save_watchlist(df)
            st.success(f"{code} 已從自選清單中移除。請重新整理查看更新結果。")
    except Exception as e:
        st.warning("尚未建立自選清單或資料遺失。")
