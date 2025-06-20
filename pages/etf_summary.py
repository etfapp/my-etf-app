import streamlit as st
import pandas as pd
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.data_loader import load_etf_summary

st.title("📈 ETF 總表")
df = load_etf_summary()
    df["技術圖表"] = df["代碼"].apply(lambda x: f"[📊 查看](/chart?symbol={x})")
    st.dataframe(df[["代碼", "名稱", "殖利率", "價格", "技術圖表"]], use_container_width=True)

st.markdown('---')
st.markdown('### 🔍 技術圖表快速查看')
for i, row in df.iterrows():
    st.markdown(f"📊 [{row['代碼']}]({{st.get_url()}}?symbol={row['代碼']})")
