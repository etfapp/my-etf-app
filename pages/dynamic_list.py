
import streamlit as st
import pandas as pd
import os

st.title("📉 動態清單（位階偏低推薦）")

csv_path = os.path.join("data", "etf_summary.csv")
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)

    # 篩選邏輯（範例：殖利率大於 4）
    filtered = df[df["殖利率"] > 4]
    filtered["技術圖表"] = filtered["代碼"].apply(lambda x: f"[📊 查看](/chart?symbol={x})")

    st.dataframe(filtered[["代碼", "名稱", "殖利率", "價格", "技術圖表"]], use_container_width=True)

    st.markdown("### 🔍 技術圖表快速查看")
    for code in filtered["代碼"]:
        st.markdown(f"- 📊 [{code}](/chart?symbol={code})")
else:
    st.warning("找不到 etf_summary.csv")
