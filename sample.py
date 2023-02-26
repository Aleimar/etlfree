from pyspark.sql import SparkSession
import os


file_path  = os.getcwd() + "/dailycheckins.csv"

print(file_path)

spark = SparkSession.builder.appName("sparkTest").getOrCreate()

df = spark.read.option("header",True).csv(file_path)

from pyspark.sql.functions import col, date_format
df2 = df.withColumn(
  "date_column_formatted",  
  date_format(col("timestamp"), "yyyy-MM-dd HH:mm:ss")
).drop(col("timestamp"))

df2.select("user","hours","project", "date_column_formatted").write.format("jdbc")\
    .option("url", "jdbc:postgres://aleimar:VyDTDFFrpLvN8Sql9iOSuI2Ys28KFAM4@dpg-cftnk7p4reb6ks10pjf0-a.singapore-postgres.render.com/posttestdb") \
    .option("driver", "org.postgresql.Driver").option("dbtable", "test") \
    .option("user", "aleimar").option("password", "VyDTDFFrpLvN8Sql9iOSuI2Ys28KFAM4").save()

import streamlit as st
import pandas as pd

st.title("A Simple Streamlit Web App")
name = st.text_input("Enter your name", '')
st.write(f"Hello {name}!")
x = st.slider("Select an integer x", 0, 10, 1)
y = st.slider("Select an integer y", 0, 10, 1)
df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
st.write(df)