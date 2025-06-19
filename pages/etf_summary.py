import streamlit as st
import pandas as pd
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.data_loader import load_etf_summary

st.title("📈 ETF 總表")
df = load_etf_summary()
st.dataframe(df, use_container_width=True)