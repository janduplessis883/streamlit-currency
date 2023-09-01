import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.title("JP's Currency Tracker")
st.markdown('Crafted with ♥️ by your favourite **Data Scientist**.')



# Correctly parse the Timestamp column with dayfirst=True
data = pd.read_csv('https://gist.githubusercontent.com/janduplessis883/e7b834c8293745ddc92b7a1fc57af9c0/raw/currency_rates.csv', parse_dates=['Timestamp'], dayfirst=True)

option = st.slider('Display no of rows', 1, 10, 1)
st.write(data.tail(option))

metric = data.tail(1)

col1, col2 = st.columns(2)
col1.metric("Euro - GBP", metric['GBP'])
col2.metric("Euro - USD", metric['USD'])


# Dropdown for selecting time range
time_options = {
    "Last Day": 1,
    "Last 2 Day": 2,
    "Last 3 Day": 3,
    "Last 4 Day": 4,
    "Last 5 Day": 5,
    "Last Week": 7,
    "Last 2 Weeks": 14,
    "Last 3 Weeks": 21,
    "Last 4 Weeks": 28,
    "Last 6 Weeks": 42,
    "All": None
}


selected_time = st.selectbox("Select Time Range", list(time_options.keys()))

# Filter data based on the selected time range
if selected_time != "All":
    end_date = data["Timestamp"].max()  # Latest date in the data
    start_date = end_date - timedelta(days=time_options[selected_time])
    filtered_data = data[data["Timestamp"].between(start_date, end_date)]
else:
    filtered_data = data

# Create the Seaborn line plot for GBP
fig1, ax1 = plt.subplots(figsize=(15, 3))
sns.lineplot(data=filtered_data, x='Timestamp', y='GBP', ax=ax1, color='#1d4878')
ax1.set_title('GBP Exchange Rate for ' + selected_time)
ax1.set_xlabel('Date')
ax1.set_ylabel('Rate (GBP)')
ax1.xaxis.grid(False)  # Remove vertical grid lines
ax1.yaxis.grid(True)   # Add horizontal grid lines
st.pyplot(fig1)  # Display the GBP plot in Streamlit

# Create the Seaborn line plot for USD
fig2, ax2 = plt.subplots(figsize=(15, 3))
sns.lineplot(data=filtered_data, x='Timestamp', y='USD', ax=ax2, color='#a54b49')
ax2.set_title('USD Exchange Rate for ' + selected_time)
ax2.set_xlabel('Date')
ax2.set_ylabel('Rate (USD)')
ax2.xaxis.grid(False)  # Remove vertical grid lines
ax2.yaxis.grid(True)   # Add horizontal grid lines
st.pyplot(fig2)  # Display the USD plot in Streamlit

