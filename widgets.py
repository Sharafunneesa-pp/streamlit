import streamlit as st
import pandas as pd


st.title("Streamlit Text Input")
name=st.text_input("Enter your name : ")
age=st.slider("Select your age",0,100,25)
st.write(f"Your age is {age}")


options=["python","java","c++","javascript"]
choice=st.selectbox("Choose your favourite Language",options)
st.write(f"You selected {choice}")
if name:
    st.write(f"Hello {name}")


data={
    "Name":["nisha","rafeek","nilu","ammu"],
    "course":["bca","mca","mba","school"],
    "city":["Dubai","kerala","bangalore","punjab"]

}
df=pd.DataFrame(data)
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV File",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)