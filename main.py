import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns([1.5, 1.5])

with col1:
    st.image("Images/photo.png", width=350)
with col2:
    st.title("Vikram's")
    content1 = """ 
    An AIML undergraduate with a passion for technology,
    this individual has mastered machine learning, deep learning,
    and web app development. Proficient in Python, C, and C++,
    with a solid understanding of Java, R, and JavaScript. \n
    I have explored frameworks like Streamlit, LangChain, Flask, and Django.
    Their expertise extends to database management with MySQL and DB-Browser,
    as well as AI and ML technologies, including Neural Networks,
    TensorFlow, and Computer Vision. \n
    Driven by innovation, they explore 
    large language models, web app development, and blockchain, all with the aim of solving real-world challenges through technology."""
    st.info(content1)
content2 = """  ...
\n\tBelow You can find some of the apps I built.
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:8].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
with col4:
    for index, row in df[8:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")


