#every single time something changes, streamlit will rerun the entire python file

import streamlit as st

pressed = st.button("Press me")
print(pressed)

click1 = st.button("Click me 1")
print('first: ' ,click1)

click2=st.button("Click me 2")
print('Second: ',click2)
