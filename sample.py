import streamlit as st
import pandas as pd
import os

file_path  = os.getcwd() + "/dailycheckins.csv"

df =pd.read_csv(file_path)

df['timestamp']= pd.to_datetime(df['timestamp'])

st.title("A Simple Streamlit Web App")
name = st.text_input("Enter your name", '')
st.write(f"Hello {name}!")
x = st.slider("Select an integer x", 0, 10, 1)
y = st.slider("Select an integer y", 0, 10, 1)
# df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
st.write(df)

# postgres://aleimar:VyDTDFFrpLvN8Sql9iOSuI2Ys28KFAM4@dpg-cftnk7p4reb6ks10pjf0-a/posttestdb
# postgres://aleimar:VyDTDFFrpLvN8Sql9iOSuI2Ys28KFAM4@dpg-cftnk7p4reb6ks10pjf0-a.singapore-postgres.render.com/posttestdb