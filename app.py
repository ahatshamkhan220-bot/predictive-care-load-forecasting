import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Predictive Forecasting of HHS Care Load")

df = pd.read_csv("forecast_output.csv")

st.subheader("Care Load Trend")

plt.figure(figsize=(10,4))
plt.plot(df['Children in HHS Care'])
st.pyplot(plt)

st.subheader("Capacity Risk Distribution")
st.bar_chart(df['Capacity_Risk'].value_counts())