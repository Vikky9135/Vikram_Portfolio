import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns([1.5, 1.5])

with col1:
    st.image("Images/photo.png", width=350)
with col2:
    st.title("Vikram's")
    content1 = """ 
    Hi... I am Vikram ... Programmer, web developer and a Blockchain Engineer.\n
    I am a student in Reva University with B.Tech degree in CSE-Artificial Engineering and Machine Learning .\n
    I have worked on many minor projects on web development and Blockchain Technology.  \n
    """
    st.info(content1)
content2 = """  ...
\n\tBelow You can find some of the apps I built in Python.
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")


