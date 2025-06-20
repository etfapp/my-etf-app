import streamlit as st

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "utils"))
try:
    import data_updater
    data_updater.update_etf_data()
except Exception as e:
    import streamlit as st
    st.error("ETF 資料更新失敗，請稍後再試")
st.set_page_config(page_title="ETF 助手首頁", layout="wide")
st.title("📊 ETF 智慧投資助理")
st.markdown("歡迎使用！請從左側選單選擇功能模組開始使用。")