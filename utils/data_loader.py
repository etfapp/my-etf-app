import pandas as pd
import os

def load_summary_data():
    try:
        path = os.path.join("data", "etf_data.csv")
        df = pd.read_csv(path)
        return df
    except Exception as e:
        return pd.DataFrame()
