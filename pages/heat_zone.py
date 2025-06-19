import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
import pandas as pd

def app():
    st.title("🔥 升溫區")
    try:
        df = pd.read_csv("data/heat_zone.csv")
        st.dataframe(df)
    except Exception as e:
        st.error("讀取升溫區資料失敗。")
