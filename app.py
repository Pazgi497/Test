import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Title of the app
st.title("Streamlit + Plotly Demo")

# Sidebar for selecting chart type
st.sidebar.header("Select Chart Type")
chart_type = st.sidebar.selectbox("Choose chart", ["Histogram", "Bar Chart"])

# Generate random data
data = np.random.randn(1000)

# Display Histogram using Plotly
if chart_type == "Histogram":
    st.subheader("Histogram with Plotly")
    fig = px.histogram(data_frame=data, nbins=30, title="Histogram of Random Data")
    fig.update_layout(
        xaxis_title="Value",
        yaxis_title="Frequency"
    )
    st.plotly_chart(fig)

# Display Bar Chart using Plotly
elif chart_type == "Bar Chart":
    st.subheader("Bar Chart with Plotly")

    # Create categorical data
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 33]

    fig = go.Figure(data=[go.Bar(x=categories, y=values)])
    fig.update_layout(
        title="Bar Chart of Sample Categories",
        xaxis_title="Category",
        yaxis_title="Value"
    )
    st.plotly_chart(fig)
