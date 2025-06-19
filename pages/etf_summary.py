import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from utils.data_loader import load_watchlist, save_watchlist
from utils.data_loader import load_summary_data
import pandas as pd

def app():
    st.title("📋 ETF 總表")
    try:
        df = load_summary_data()
        st.dataframe(df)

    watchlist_df = load_watchlist()
    codes_in_watchlist = watchlist_df["代碼"].tolist()

    for i, row in df.iterrows():
        code = row["代碼"]
        name = row.get("名稱", "")
        if code not in codes_in_watchlist:
            if st.button(f"➕ 加入自選 - {code}", key=f"add_{code}"):
                new_row = pd.DataFrame([row])
                updated_df = pd.concat([watchlist_df, new_row], ignore_index=True).drop_duplicates(subset=["代碼"])
                save_watchlist(updated_df)
                st.success(f"已將 {code} 加入自選清單。請重新整理頁面查看更新結果。")
    except Exception as e:
        st.error(f"載入 ETF 資料時發生錯誤: {e}")
