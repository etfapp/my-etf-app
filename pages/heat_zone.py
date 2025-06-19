
import streamlit as st
import pandas as pd
from utils.data_loader import load_etf_summary

st.title("🔥 升溫區 - 建議觀察或減碼的 ETF")

try:
    df = load_etf_summary()
    df = df[df["基本面評分"] >= 60]

    def check_heat_conditions(row):
        reasons = []
        if row["RSI"] > 70:
            reasons.append("RSI 過熱")
        if row.get("MACD_死叉", False):
            reasons.append("MACD 死叉")
        if row["殖利率百分位"] < 20:
            reasons.append("殖利率低")
        if row.get("成交量放大", False):
            reasons.append("成交量放大")
        return reasons

    df["升溫原因"] = df.apply(check_heat_conditions, axis=1)
    df["升溫條件數"] = df["升溫原因"].apply(len)
    df = df[df["升溫條件數"] > 0]
    df["升溫等級"] = df["升溫條件數"].apply(lambda x: "🟥 高" if x >= 3 else ("🟧 中" if x == 2 else "🟨 低"))

    df_show = df[["代碼", "名稱", "價格", "殖利率", "RSI", "升溫等級", "升溫原因"]]
    df_show["升溫原因"] = df_show["升溫原因"].apply(lambda x: "、".join(x))
    st.dataframe(df_show.reset_index(drop=True), use_container_width=True)

except Exception as e:
    st.error(f"資料載入錯誤：{e}")
