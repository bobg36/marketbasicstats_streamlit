import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Load the CSV file
file_path = "market_overview.csv"
df = pd.read_csv(file_path)

# Combine the "Date" column into a single datetime column
df['Datetime'] = pd.to_datetime(df['Date'])

# Sidebar filters
st.sidebar.title("Data Filters")
start_date = st.sidebar.date_input("Start Date", min(df['Datetime']).date())
end_date = st.sidebar.date_input("End Date", max(df['Datetime']).date())

# Filter the DataFrame based on the selected date range
filtered_df = df[(df['Datetime'] >= pd.to_datetime(start_date)) & (df['Datetime'] <= pd.to_datetime(end_date))]

# Line chart for selected cryptocurrencies over time
st.header("breeding costs over time")

# Select the cryptocurrencies you want to plot (e.g., 'ETH', 'AXS', 'SLP', 'All Axies')
available_cryptos = df.columns[17:24]  # Assuming the crypto columns start from the 4th column
default_selection = [crypto for crypto in available_cryptos] # Set default selection to include all cryptocurrencies
selected_cryptos = st.multiselect("Select breed count from dropdown", available_cryptos, default=default_selection)
if selected_cryptos: # Check if at least one cryptocurrency is selected
    fig = px.line(filtered_df, x='Datetime', y=selected_cryptos, title="breed 1 to 7 cost")
    st.plotly_chart(fig)
else:
    st.write("Please select at least one cryptocurrency to plot.")








# Select the cryptocurrencies you want to plot (e.g., 'ETH', 'AXS', 'SLP', 'All Axies')
# Assuming you have already imported the necessary libraries and created the 'filtered_df'

# Define the available cryptocurrencies
available_cryptos = df.columns[2:5]  # Assuming the crypto columns start from the 4th column

default_selection = [crypto for crypto in available_cryptos] # Set default selection to include all cryptocurrencies

# Create a dropdown to select cryptocurrencies
selected_cryptos = st.multiselect("Select cryptocurrencies from the dropdown", available_cryptos, default=default_selection)

if selected_cryptos: # Check if at least one cryptocurrency is selected
    # Calculate the percentage values for each selected cryptocurrency
    for crypto in selected_cryptos:
        filtered_df[crypto] = (filtered_df[crypto] - filtered_df[crypto].min()) / (filtered_df[crypto].max() - filtered_df[crypto].min()) * 100

    fig = px.line(filtered_df, x='Datetime', y=selected_cryptos, title="Token Values to USD")

    # Set the y-axis range to 0-100%
    fig.update_layout(yaxis_range=[0, 100])

    st.plotly_chart(fig)
else:
    st.write("Please select at least one cryptocurrency to plot.")







# Define the available cryptocurrencies
available_cryptos = df.columns[2:5]  # Assuming the crypto columns start from the 4th column

# Add the division options for AXS/ETH and SLP/ETH
division_options = [f"{crypto}/ ETH" for crypto in available_cryptos]

# Remove "ETH/ETH" from the division options
division_options = [option for option in division_options if option != "ETH/ETH"]

default_selection = division_options[0]  # Set the default selection to the first option in the filtered list

# Create a dropdown to select cryptocurrencies for division
selected_division = st.selectbox("Select the division option", division_options, index=0)

# Extract the selected cryptocurrency and divide it by ETH
selected_crypto, base_crypto = selected_division.split('/')
result_column = f"{selected_crypto}/{base_crypto}"
filtered_df[result_column] = filtered_df[selected_crypto] / filtered_df[base_crypto]

# Define the percentage of data to keep (adjust as needed)
data_percentile = 95  # You can adjust this value

# Remove outliers using the IQR method
Q1 = filtered_df[result_column].quantile(0.25)
Q3 = filtered_df[result_column].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

filtered_df = filtered_df[(filtered_df[result_column] >= lower_bound) & (filtered_df[result_column] <= upper_bound)]

fig = px.line(filtered_df, x='Datetime', y=result_column, title="Token Values to ETH")

st.plotly_chart(fig)




