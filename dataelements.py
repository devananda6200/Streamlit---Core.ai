import streamlit as st

import pandas as pd

 #Title
st.title("Streamlit Elements Demo")
#Dataframe Section
st.subheader("Dataframe")
df = pd.DataFrame({ #pandas dataframe
    'Name': ['Alice', 'Bob', 'Charlie', 'David'], 
    'Age': [25, 32, 37, 45], 
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Chef']
})
st.dataframe(df) #passing dataframe to st.dataframe
#enlarge,search,download 

#Data Editor Section (Editable dataframe)
st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df)

 #Static Table Section
st.subheader("Static Table")
st.table(df)

#JSON and Dict section
st.subheader("JSON and Dictionary")
sample_dict = {
    "name": "John",
    "age": 25,
    "skills": ["Python", "Data Science", "Machine learning"]
}
st.json(sample_dict)

#to show as dictionary:
st.write("Dictionary view:", sample_dict)