
import streamlit as st
import pandas as pd
import os

st.title("⭐ 自選清單 + 水位計算機 + 存股模擬器")

watchlist_path = os.path.join("data", "watchlist.csv")
etf_path = os.path.join("data", "etf_summary.csv")

if os.path.exists(watchlist_path) and os.path.exists(etf_path):
    df_watchlist = pd.read_csv(watchlist_path)
    df_all = pd.read_csv(etf_path)

    # 篩出自選資料
    df_watch = df_all[df_all["代碼"].isin(df_watchlist["代碼"])]
    df_watch["技術圖表"] = df_watch["代碼"].apply(lambda x: f"[📊 查看](/chart?symbol={x})")

    st.markdown("### 📋 自選清單")
    st.dataframe(df_watch[["代碼", "名稱", "殖利率", "價格", "技術圖表"]], use_container_width=True)

    # 加入／刪除自選
    st.markdown("### ➕ 加入 / 移除 ETF")
    new_code = st.text_input("輸入 ETF 代碼加入自選清單")
    if st.button("加入自選清單") and new_code:
        if new_code not in df_watchlist["代碼"].values:
            df_watchlist.loc[len(df_watchlist)] = [new_code]
            df_watchlist.to_csv(watchlist_path, index=False)
            st.success(f"已加入 {new_code} 至自選清單，請重新整理畫面")
        else:
            st.warning("該代碼已存在自選清單中")

    if st.button("刪除選擇項目"):
        selected = st.multiselect("選擇要刪除的 ETF 代碼", df_watchlist["代碼"].tolist())
        df_watchlist = df_watchlist[~df_watchlist["代碼"].isin(selected)]
        df_watchlist.to_csv(watchlist_path, index=False)
        st.success("已刪除選定項目，請重新整理畫面")
else:
    st.warning("找不到必要資料檔案（watchlist 或 etf_summary）")
