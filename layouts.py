import streamlit as st

#Sidebar layout
st.sidebar.title("This is the sidebar")
st.sidebar.write("You can place elements like sliders, buttons and text here")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

#tabs layout
tab1, tab2, tab3 = st.tabs(["Tab 1","Tab 2", "Tab3"])

with tab1:
    st.write("This is tab 1")

with tab2:    
    st.write("This is tab 2")
    
with tab3:
    st.write("This is tab 3")
    
#columns layout
col1, col2 = st.columns(2)   
with col1:
    st.header("Column 1")
    st.write("This is column 1")
    
with col2:
    st.header("Column 2")
    st.write("This is column 2")
    
#Containers
with st.container(border=True):
    st.write("This is inside a container")
    st.write("Containers help group elements")    
    st.write("Containers manage sections of a page")
    
placeholder = st.empty()
st.write("Empty placeholder")    

if st.button("Update Placeholder"):
    placeholder.write("This placeholder has been updated")
    
    
#Expander    
with st.expander("Click to expand"):
    st.write("This is an expander")
    st.write("You can place any content inside an expander")
    
    
#sidebar input
if sidebar_input:
    st.write(f"You entered in the sidebar: {sidebar_input}")