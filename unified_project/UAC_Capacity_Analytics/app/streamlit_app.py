import streamlit as st
import pandas as pd

st.title("UAC System Capacity & Care Load Dashboard")

df = pd.read_csv(
    "data/HHS_Unaccompanied_Alien_Children_Program.csv"
)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date"])

st.line_chart(df.set_index("Date")["Children in HHS Care"])
