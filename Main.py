import streamlit as st
import pandas as pd

# Load data and cache it
@st.cache_data
def load_data():
    import os
    st.write("📁 Files in working directory:", os.listdir("."))

    try:
        df = pd.read_excel("Forecasting_Dashboard_Data.xlsx")
        df["Date"] = pd.to_datetime(df["Date"])
        st.success("✅ Excel file loaded successfully!")
        return df
    except Exception as e:
        st.error(f"❌ Failed to load Excel file: {e}")
        return pd.DataFrame()


# Load the data
df = load_data()
st.write("Loaded rows:", len(df))
st.write("Date range:", df['Date'].min(), "to", df['Date'].max())

st.title("📊 Forecasting Dashboard Demo")
st.markdown("Use the slider and filters to explore company and sector-level risk over time.")

# Slider setup
min_date = df["Date"].min()
max_date = df["Date"].max()
selected_date = st.slider("Select date", min_value=min_date, max_value=max_date)

# Normalize to just date (not timestamp)
selected_date = pd.to_datetime(selected_date).date()
df["DateOnly"] = df["Date"].dt.date

# Filter by selected date
filtered
