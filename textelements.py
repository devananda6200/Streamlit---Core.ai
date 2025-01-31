import streamlit as st

 #similar to html tage like you'hv got h1,h2 tags
 
st.title("Simple title")
st.header("This is a header") #slightly smaller text
st.subheader("Subheader")
st.markdown("This is **Markdown** ")
st.markdown("This is _Markdown_ ")
st.caption("Small text")

code_example = """
def greet(name):
    print('hello', name)
    """
st.code(code_example, language = 'python')
st.divider()

#image 
import os
st.image(os.path.join(os.getcwd(),"static","BG.jpeg"),width = 500)