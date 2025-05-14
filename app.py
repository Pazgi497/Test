import streamlit as st
import pandas as pd
import numpy as np

st.title("Simple Data Visualization Demo")

st.write("This demo shows a random dataframe and a line chart.")

# Generate random data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.write("Here's the data:")
st.dataframe(data)

st.line_chart(data)
