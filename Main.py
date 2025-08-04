import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_excel("Forecasting_Dashboard_Data.xlsx")
    df["Date"] = pd.to_datetime(df["Date"])
    return df


# Load and preview the data
df = load_data()

# Sidebar filters
st.sidebar.title("Filter Options")
selected_sector = st.sidebar.selectbox("Select Sector", options=["All"] + sorted(df["Sector"].unique().tolist()))
selected_company = st.sidebar.selectbox("Select Company", options=["All"] + sorted(df["Company"].unique().tolist()))

# Timeline slider
min_date = df["Date"].min()
max_date = df["Date"].max()
selected_date = st.slider("Select date", min_value=min_date, max_value=max_date)

# Apply filters
filtered_df = df[df["Date"] == selected_date]

if selected_sector != "All":
    filtered_df = filtered_df[filtered_df["Sector"] == selected_sector]

if selected_company != "All":
    filtered_df = filtered_df[filtered_df["Company"] == selected_company]

# Display table
st.subheader("Filtered Risk Scores")
if not filtered_df.empty:
    styled_df = filtered_df.style.applymap(
        lambda val: "background-color: red" if val > 0.7 else "", subset=["RiskScore"]
    )
    st.dataframe(styled_df)
else:
    st.write("No data found for the selected filters.")

# Visualization
st.subheader("Average Sector Risk on Selected Date")
sector_risk = filtered_df.groupby("Sector")["RiskScore"].mean().sort_values()
if not sector_risk.empty:
    fig, ax = plt.subplots()
    sector_risk.plot(kind="barh", ax=ax)
    ax.set_xlabel("Average Risk Score")
    ax.set_title(f"Sector Risk Scores on {selected_date.strftime('%Y-%m-%d')}")
    st.pyplot(fig)
else:
    st.write("No sector data available to plot.")

# Force rebuild

