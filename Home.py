import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streamlit BI x Claude Code Starter", layout="wide")

st.title("Streamlit BI x Claude Code Starter")

@st.cache_data
def load_data():
    orders_df = pd.read_csv("sample_data/orders.csv")
    users_df = pd.read_csv("sample_data/users.csv")
    return orders_df, users_df

orders_df, users_df = load_data()

st.header("Orders Data (Top 10 rows)")
st.dataframe(orders_df.head(10))

st.header("Users Data (Top 10 rows)")
st.dataframe(users_df.head(10))