import streamlit as st
import pandas as pd

# Title and subheader
st.title("Sales Summary App")
st.subheader("Simple app to filter sales by category")

# Hardcoded data
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones", "Camera"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics"],
    "Sales": [50000, 30000, 20000, 10000, 40000]
}

df = pd.DataFrame(data)

# Sidebar filter
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter data
filtered_df = df[df["Category"] == category]

# Show table
st.dataframe(filtered_df)

# Line chart
st.line_chart(filtered_df["Sales"])