import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Page config
st.set_page_config(
    page_title="Lead Management Dashboard",
    page_icon="💼",
    layout="wide"
)

# Title
st.title("💼 AI Lead Management Dashboard")
st.subheader("Real-time lead tracking powered by AI")
st.divider()

# Read from Google Sheets
import requests
import json

# Google Sheets ID
SHEET_ID = "1V0QlvMJdPhzElLBiyYZEPYtgsJdDMpWLG78R0L7v648"

url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"
df = pd.read_csv(url)

# Stats
col1, col2, col3 = st.columns(3)
col1.metric("Total Leads", len(df))
col2.metric("High Priority", len(df[df['AI Analysis'].str.contains('High', na=False)]))
col3.metric("Today's Leads", len(df[df['Date'] == pd.Timestamp.now().strftime('%d/%m/%Y')]))

st.divider()

# Table
st.subheader("📊 All Leads")
st.dataframe(df, use_container_width=True)