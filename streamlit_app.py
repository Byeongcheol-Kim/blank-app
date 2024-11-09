import streamlit as st
import pandas as pd

# Load the CSV data
data_file = 'movies_2024.csv'
df = pd.read_csv(data_file)

# Filter the relevant columns for budget and revenue
budget_revenue_df = df[['title', 'budget', 'revenue']]

# Create Streamlit app
st.title('Movie Budget vs Revenue')

# Show data in a table
st.write("## Budget and Revenue Table")
st.dataframe(budget_revenue_df)

# Add additional information
st.write("### Insights")
st.write("This table shows the budget and revenue of each movie, which helps in understanding their financial performance.")
