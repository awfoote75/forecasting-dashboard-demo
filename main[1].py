import streamlit as st
import pandas as pd
import datetime

# Load the forecasting data
@st.cache_data
def load_data():
    try:
        return pd.read_excel("Forecasting_Dashboard_Data.xlsx")
    except FileNotFoundError as e:
        st.error("Excel file not found: Ensure the file is uploaded correctly.")
        return pd.DataFrame()  # Return an empty dataframe to avoid crashing the app


df = load_data()
df['Date'] = pd.to_datetime(df['Date'])

# Timeline slider
start_date = df['Date'].min().date()
end_date = df['Date'].max().date()
selected_date = st.slider(
    "📅 Select a date to view forecast data:",
    min_value=start_date,
    max_value=end_date,
    value=start_date,
    format="MMM DD, YYYY"
)

# Filter by date
filtered_df = df[df['Date'].dt.date == selected_date]

# Dropdowns for sector and company
sectors = filtered_df['Sector'].unique()
selected_sectors = st.multiselect("📂 Filter by sector:", sectors, default=list(sectors))

filtered_df = filtered_df[filtered_df['Sector'].isin(selected_sectors)]

companies = filtered_df['Company'].unique()
selected_companies = st.multiselect("🏢 Filter by company:", companies, default=list(companies))

filtered_df = filtered_df[filtered_df['Company'].isin(selected_companies)]

# Highlight high-risk rows
def highlight_risk(val):
    return 'background-color: #ffcccc' if val > 0.7 else ''

# Display filtered table
st.markdown("### 📊 Forecast Snapshot (Filtered)")
st.dataframe(
    filtered_df.sort_values(by='RiskScore', ascending=False)
               .style.applymap(highlight_risk, subset=['RiskScore']),
    use_container_width=True
)

# Sector risk bar chart
avg_risk = filtered_df.groupby('Sector')['RiskScore'].mean().sort_values(ascending=False)
st.markdown("### 📉 Average Risk Score by Sector (Filtered)")
st.bar_chart(avg_risk)

# Trigger rebuild
# Trigger rebuild to install openpyxl



