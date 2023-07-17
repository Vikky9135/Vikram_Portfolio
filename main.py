import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Images/photo.png")
with col2:
    st.title("Vikram's")
    content1 = """ 
    Hi... I am Vikram ... Programmer, web developer and Blockchain Engineer.
    I am a student at Reva University with B.Tech degree in CSE-Artificial Engineering and Machine Learning .
    I have worked on many minor projects on web development and Blockchain Technology.  
    """
    st.info(content1)
content2 = """
Below You can find some of the apps I built in Python.
"""
st.write(content2)

