
import streamlit as st
import datetime

# --- Timeline slider range
start_date = datetime.date(2025, 8, 1)
end_date = datetime.date(2026, 1, 1)

# --- Key markers
election_date = datetime.date(2025, 11, 4)
taiwan_drill = datetime.date(2025, 10, 22)
shipping_alert = datetime.date(2025, 9, 15)

# --- Simulated timeline slider
selected_date = st.slider(
    "📅 Select a date to view scenario context:",
    min_value=start_date,
    max_value=end_date,
    value=start_date,
    format="MMM DD, YYYY"
)

# --- Dynamic Side Panel Output
st.sidebar.markdown("## 📊 Scenario Snapshot")

if selected_date == taiwan_drill:
    st.sidebar.markdown(f"**📅 Date:** {selected_date.strftime('%b %d, %Y')}")
    st.sidebar.markdown("**🎯 Scenario:** Taiwan Leadership Transition")
    st.sidebar.markdown("**🔁 Triggered By:** PLA naval drills + U.S. visit")

    st.sidebar.markdown("### 🔍 Sector Risk Profile")
    st.sidebar.markdown("- Semiconductors: 🔴 High (TSMC flagged)")
    st.sidebar.markdown("- Defense: 🟠 Elevated (Raytheon contracts)")
    st.sidebar.markdown("- Shipping: 🟡 Moderate (Kaohsiung reroutes)")

    st.sidebar.markdown("### 🏢 Watchlist Companies")
    st.sidebar.markdown("- TSMC (Sharp drop in forecasted output)")
    st.sidebar.markdown("- Evergreen Marine (Alert: rerouting costs)")
    st.sidebar.markdown("- Lockheed Martin (Boost in procurement)")

    st.sidebar.markdown("### ⚠️ Alerts")
    st.sidebar.markdown("- 📈 Volatility spike detected (Semiconductors)")
    st.sidebar.markdown("- 🗳️ Election < 30 days – Scenario shift zone")
    st.sidebar.markdown("- 🛑 Market threshold breached (Shipping index)")

elif selected_date == election_date:
    st.sidebar.markdown(f"**📅 Date:** {selected_date.strftime('%b %d, %Y')}")
    st.sidebar.markdown("**🎯 Scenario:** U.S. Presidential Election")
    st.sidebar.markdown("**🔁 Triggered By:** Domestic policy shift expectations")

    st.sidebar.markdown("### 🔍 Sector Risk Profile")
    st.sidebar.markdown("- AI: 🔴 High uncertainty")
    st.sidebar.markdown("- Defense: 🟠 Budget signals diverging")
    st.sidebar.markdown("- Construction: 🟡 Stimulus-dependent")

    st.sidebar.markdown("### 🏢 Watchlist Companies")
    st.sidebar.markdown("- Palantir (Model drift warning)")
    st.sidebar.markdown("- Caterpillar (Forecast sensitive to policy)")

    st.sidebar.markdown("### ⚠️ Alerts")
    st.sidebar.markdown("- 🚨 Model instability: AI sector")
    st.sidebar.markdown("- 🗳️ Realignment of probabilities underway")

elif selected_date == shipping_alert:
    st.sidebar.markdown(f"**📅 Date:** {selected_date.strftime('%b %d, %Y')}")
    st.sidebar.markdown("**🎯 Scenario:** South China Sea Disruption")
    st.sidebar.markdown("**🔁 Triggered By:** Naval blockade threats")

    st.sidebar.markdown("### 🔍 Sector Risk Profile")
    st.sidebar.markdown("- Shipping: 🔴 Major reroutes")
    st.sidebar.markdown("- Oil: 🟠 Pricing shock observed")

    st.sidebar.markdown("### 🏢 Watchlist Companies")
    st.sidebar.markdown("- Evergreen Marine (Port congestion)")
    st.sidebar.markdown("- COSCO (Flagged for exposure risk)")

    st.sidebar.markdown("### ⚠️ Alerts")
    st.sidebar.markdown("- ⛔ Supply Chain Alert Active")
    st.sidebar.markdown("- 📉 Oil index dip warning")

else:
    st.sidebar.markdown(f"**📅 Date:** {selected_date.strftime('%b %d, %Y')}")
    st.sidebar.markdown("No major scenario detected.")
    st.sidebar.markdown("Monitor upcoming geopolitical or market triggers.")

# --- Timeline Visual Placeholder
st.markdown("### 🧭 Timeline Event Markers")
st.markdown("- ⚠️ **Sep 15, 2025**: South China Sea Tension (Shipping Alert)")
st.markdown("- 🛥️ **Oct 22, 2025**: Taiwan Leadership Drill")
st.markdown("- 🗳️ **Nov 4, 2025**: U.S. Election")
