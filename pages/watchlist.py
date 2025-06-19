import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from utils.data_loader import load_watchlist
import pandas as pd

def app():
    st.title("⭐ 自選清單")
    try:
        df = load_watchlist()
        st.dataframe(df)
    except Exception as e:
        st.warning("尚未建立自選清單或資料遺失。")
