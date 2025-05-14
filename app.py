import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Visualization Demo")

st.write("### Bar Chart")
data_bar = pd.DataFrame({
    'Fruits': ['Apples', 'Bananas', 'Cherries', 'Dates'],
    'Quantity': [10, 20, 15, 7]
})
st.bar_chart(data_bar.set_index('Fruits'))

st.write("### Histogram")
data_hist = np.random.randn(1000)
st.write("Histogram of 1000 random values")
st.bar_chart(pd.Series(data_hist).value_counts(bins=20).sort_index())

st.write("### Line Chart")
data_line = pd.DataFrame(
    np.random.randn(30, 3),
    columns=['X', 'Y', 'Z']
)
st.line_chart(data_line)
