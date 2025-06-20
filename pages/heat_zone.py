import streamlit as st
import pandas as pd
from utils.data_loader import load_etf_summary

st.title("🔥 升溫區 - 建議觀察或減碼的 ETF")

try:
    df = load_etf_summary()
    if "基本面評分" in df.columns:
        df = df[df["基本面評分"] >= 60]

    def check_heat_conditions(row):
        reasons = []
        if "RSI" in row and pd.notna(row["RSI"]) and row["RSI"] > 70:
            reasons.append("RSI 過熱")
        if "MACD_死叉" in row and row["MACD_死叉"]:
            reasons.append("MACD 死叉")
        if "殖利率百分位" in row and pd.notna(row["殖利率百分位"]) and row["殖利率百分位"] < 20:
            reasons.append("殖利率低")
        if "成交量放大" in row and row["成交量放大"]:
            reasons.append("成交量放大")
        return reasons

    df["升溫原因"] = df.apply(check_heat_conditions, axis=1)
    df["升溫條件數"] = df["升溫原因"].apply(len)
    df = df[df["升溫條件數"] > 0]
    df["升溫等級"] = df["升溫條件數"].apply(lambda x: "🟥 高" if x >= 3 else ("🟧 中" if x == 2 else "🟨 低"))

    # 容錯顯示欄位處理
    columns_to_show = ["代碼", "名稱", "價格", "殖利率", "RSI", "升溫等級", "升溫原因"]
    columns_to_show = [col for col in columns_to_show if col in df.columns or col in ["升溫等級", "升溫原因"]]
    df_show = df[columns_to_show].copy()
    df_show["技術圖表"] = df_show["代碼"].apply(lambda x: f"[📊 查看](/chart?symbol={x})")
    df_show["升溫原因"] = df_show["升溫原因"].apply(lambda x: "、".join(x))
    st.dataframe(df_show[["代碼", "名稱", "殖利率", "價格", "技術圖表"]], use_container_width=True)

except Exception as e:
    st.error(f"資料載入錯誤：{e}")

st.markdown('---')
st.markdown('### 🔍 技術圖表快速查看')
for i, row in df.iterrows():
    st.markdown(f"📊 [{row['代碼']}]({{st.get_url()}}?symbol={row['代碼']})")
