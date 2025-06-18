
import streamlit as st
import pandas as pd

def app():
    st.title("📋 ETF 總表")
    try:
        df = pd.read_csv("data/etf_summary.csv")
        st.dataframe(df)
    except Exception as e:
        st.error(f"載入 ETF 資料時發生錯誤: {e}")
