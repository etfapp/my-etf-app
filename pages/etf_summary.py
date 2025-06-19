import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from utils.data_loader import load_summary_data
import pandas as pd

def app():
    st.title("📋 ETF 總表")
    try:
        df = load_summary_data()
        st.dataframe(df)
    except Exception as e:
        st.error(f"載入 ETF 資料時發生錯誤: {e}")
