import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
import pandas as pd
import os
from utils.etf_utils import load_etf_data, get_dynamic_etfs

st.title("📈 動態清單（可佈局）")

# 載入 ETF 資料
etf_data = load_etf_data()

if etf_data is None or etf_data.empty:
    st.warning("尚未成功載入 ETF 資料。請先確認資料更新狀態。")
else:
    # 篩選動態清單 ETF
    dynamic_df = get_dynamic_etfs(etf_data)

    st.markdown(f"目前可佈局標的共 **{len(dynamic_df)} 檔**")
    st.dataframe(dynamic_df, use_container_width=True)
