import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from utils.data_loader import load_watchlist, save_watchlist
import pandas as pd
import os
from utils.etf_utils import load_etf_data, get_dynamic_etfs

st.title("📈 動態清單（可佈局）")
strategy_mode = st.sidebar.selectbox("📌 請選擇策略模式", ["保守型", "平衡型", "積極型"])

# 載入 ETF 資料
etf_data = load_etf_data()

if etf_data is None or etf_data.empty:
    st.warning("尚未成功載入 ETF 資料。請先確認資料更新狀態。")
else:
    # 篩選動態清單 ETF
    dynamic_df = get_dynamic_etfs(etf_data, mode=strategy_mode)

    st.markdown(f"目前可佈局標的共 **{len(dynamic_df)} 檔**")
    st.dataframe(dynamic_df, use_container_width=True)

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
