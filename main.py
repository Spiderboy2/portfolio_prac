import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
df = pd.read_csv("data.csv", sep=";")
# print(df)

with col1:
    st.image("images/photo.png")

with col2:
    st.header("Spider_boy")
    content = """summa lamma dumma lamma you assumming i am a human what i gotta do to get it 
    throuht to get it that i am super human innovative and i made of rubber so that any thing 
    you say i will glur it to you huhhh.. i am devastating more than ever demondtrating how to
    give a m**********g odience feeling like a levestating never fading and i know the haters 
    forever waiting for the day i fell of they will be celebrating cause i know the way to get 
    them motivated i made elevate music"""
    st.write(content)

content2 = "Below you can find some of the apps that a made while praticing. Feel free to contact"

st.write(content2)

col3, space, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for i, row in df[:10].iterrows():
        # print(i) i is the index number of rows
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source_code]({row['url']})")

with col4:
    for i, row in df[10:].iterrows():
        # print(i) i is the index number of rows
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source_code]({row['url']})")
