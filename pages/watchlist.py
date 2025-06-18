
import streamlit as st
import pandas as pd

def app():
    st.title("⭐ 自選清單")
    try:
        df = pd.read_csv("data/watchlist.csv")
        st.dataframe(df)
    except Exception as e:
        st.warning("尚未建立自選清單或資料遺失。")
