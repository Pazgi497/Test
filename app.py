import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("Basic Streamlit Demo")

# Sidebar with options
st.sidebar.header("Select Chart Type")
chart_type = st.sidebar.selectbox("Choose chart", ["Histogram", "Bar Chart"])

# Generate some random data for demo
data = np.random.randn(1000)

# Display histogram
if chart_type == "Histogram":
    st.subheader("Histogram")
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, edgecolor='black')
    ax.set_title("Histogram of Random Data")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

# Display bar chart
elif chart_type == "Bar Chart":
    st.subheader("Bar Chart")
    
    # Create some sample categorical data
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 33]
    
    fig, ax = plt.subplots()
    ax.bar(categories, values, color='skyblue')
    ax.set_title("Bar Chart of Sample Categories")
    ax.set_xlabel("Category")
    ax.set_ylabel("Value")
    st.pyplot(fig)
