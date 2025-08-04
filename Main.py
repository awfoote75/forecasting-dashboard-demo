import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data and cache it
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("Forecasting_Dashboard_Data.xlsx")
        df["Date"] = pd.to_datetime(df["Date"])
        return df
    except Exception as e:
        st.error(f"Failed to load Excel file: {e}")
        return pd.DataFrame()

# Load the data
df = load_data()

# Show some quick info
if not df.empty:
    st.title("📊 Forecasting Dashboard Demo")
    st.markdown("Explore risk signals across sectors and companies.")

    st.write("Loaded rows:", len(df))
    st.write("Date range:", df["Date"].min().date(), "to", df["Date"].max().date())

    # Show a basic plot
    st.subheader("Risk Trend Over Time")
    if "Date" in df.columns and "Total Risk Score" in df.columns:
        trend = df.groupby("Date")["Total Risk Score"].mean()
        fig, ax = plt.subplots()
        trend.plot(ax=ax, title="Average Total Risk Score Over Time")
        st.pyplot(fig)

    # Show sector-level breakdown
    st.subheader("Sector Breakdown")
    if "Sector" in df.columns:
        sector_avg = df.groupby("Sector")["Total Risk Score"].mean().sort_values(ascending=False)
        st.bar_chart(sector_avg)

    # Show company-level data
    st.subheader("Company-Level Snapshot")
    company_table = df[["Date", "Company", "Sector", "Total Risk Score"]].sort_values("Date", ascending=False).head(10)
    st.dataframe(company_table)
else:
    st.warning("No data loaded. Please make sure 'Forecasting_Dashboard_Data.xlsx' is in the repo root.")
