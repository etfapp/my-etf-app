import streamlit as st
import pandas as pd
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.data_loader import load_etf_summary

st.title("📉 動態清單（位階偏低推薦）")

try:
    df = load_etf_summary()
    df = df.copy()
    filtered = df[(df["殖利率"] > 4) | (df["價格"] < 25)]
    st.dataframe(filtered, use_container_width=True)
except Exception as e:
    st.error(f"載入失敗：{e}")

st.markdown('---')
st.markdown('### 🔍 技術圖表快速查看')
for i, row in df.iterrows():
    st.markdown(f"📊 [{row['代碼']}]({{st.get_url()}}?symbol={row['代碼']})")
