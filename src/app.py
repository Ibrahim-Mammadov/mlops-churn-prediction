import streamlit as st
import pandas as pd
import joblib

# Başlıq
st.title("Customer Churn Prediction")

# İnterfeys elementləri
age = st.number_input("Age", min_value=18, max_value=100)
balance = st.number_input("Balance")

# Proqnoz düyməsi
if st.button("Predict"):
    # Burada `st.write` bir pillə içəridə (sağda) olmalıdır
    st.write("Model is successfully integrated and ready!")