import streamlit as st
import pandas as pd
import numpy as np

#Title
st.title("Streamlit Charts Demo")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['A','B','C']
)

#Area chart
st.subheader("Area chart")
st.area_chart(chart_data)

#bar chart
st.subheader("Bar chart")
st.bar_chart(chart_data)

#line chart
st.subheader("Line chart")
st.line_chart(chart_data)

#scatter chart
st.subheader("Scatter chart")
scatter_data = pd.DataFrame({
    'x' : np.random.randn(100),
    'y' : np.random.randn(100),
})
st.scatter_chart(scatter_data)

#map section
st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100,2) / [50,50] + [37.76, -122.4],
    columns = ['lat', 'lon']
)
st.map(map_data)
