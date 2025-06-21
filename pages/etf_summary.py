import streamlit as st
import pandas as pd
import os
st.title("📈 ETF 總表")

# 資料路徑
csv_path = os.path.join("data", "etf_summary.csv")
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    df["技術圖表"] = df["代碼"].apply(lambda x: f"[📊 查看](/chart?symbol={x})")
    st.dataframe(df[["代碼", "名稱", "殖利率", "價格", "技術圖表"]], use_container_width=True)
else:
    st.warning("找不到 etf_summary.csv")
