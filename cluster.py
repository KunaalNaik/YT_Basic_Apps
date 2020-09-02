# Import Libraries
import streamlit as st
import pandas as pd
#import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


# Import Data
df = pd.read_csv('Mall_Customers.csv')
df_Short = df[['Spending_Score', 'Income']]

# Add App Titles and Add a Sidebar

st.title('Cluster Analysis')
st.sidebar.title('K Means Parameters')

# Sidebar Controls
st.sidebar.number_input('Input K', min_value=1, max_value=12)

# Plot Scatter Plot using Income and Spending Score
st.header('Income and Spending Score Plot')
fig = px.scatter(df_Short, x='Spending_Score', y='Income')
st.plotly_chart(fig)

st.header('Cluster Data')
if st.checkbox('Show dataframe'):
    st.write(df)
    #st.dataframe(df)



