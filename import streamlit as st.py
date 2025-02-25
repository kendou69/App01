import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import plotly.express as px
from src.fetch_data import fetch_data, build_url
from src.process_data import col_date, col_donnees, cols, fic_export_data, main_process
import logging
import os
logging.basicConfig(level=logging.INFO)


# * INIT REPO FOR DATA
os.makedirs("data/raw/", exist_ok=True)
os.makedirs("data/interim/", exist_ok=True)

# Title for your app
st.title('Data Visualization App')

# Load data from CSV
@st.cache_data  # This decorator caches the data to prevent reloading on every interaction.
def load_data(file_path):
    # à remplir ....



# Assuming your CSV is named 'data.csv' and is in the same directory as your app.py
df = load_data(fic_export_data)

# Creating a line chart
st.subheader('Line Chart of Numerical Data Over Time')

# Select the numerical column to plot
# This lets the user select a column if there are multiple numerical columns available
# numerical_column = st.selectbox('Select the column to visualize:', df.select_dtypes(include=['float', 'int']).columns)
numerical_column = col_donnees

# ! Matplotlib - Create the plot
# fig, ax = plt.subplots()
# ax.plot(df[col_date], df[numerical_column])  # Adjust 'DateColumn' to your date column name
# ax.set_xlabel('Time')
# ax.set_ylabel(numerical_column)
# ax.set_title(f'Time Series Plot of {numerical_column}')
# # Display the plot
# st.pyplot(fig)

# ! Plotly
# Create interactive line chart using Plotly
fig = px.line(df, x=col_date, y=col_donnees, title='Consommation en fonction du temps')
st.plotly_chart(fig)