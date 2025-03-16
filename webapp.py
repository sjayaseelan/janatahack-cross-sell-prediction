import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("cross_sell_pred_model.pkl")

st.title('Vehicle Insurance Interest Prediction')

# User Input Features
gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.number_input('Age', min_value=18, max_value=100, value=30)
driving_license = st.selectbox('Driving License', [0, 1])
region_code = st.number_input('Region Code', min_value=0.0, max_value=100.0, value=28.0)
previously_insured = st.selectbox('Previously Insured', [0, 1])
vehicle_age = st.selectbox('Vehicle Age', ['< 1 Year', '1-2 Year', '> 2 Years'])
vehicle_damage = st.selectbox('Vehicle Damage', ['Yes', 'No'])
annual_premium = st.number_input('Annual Premium', min_value=0.0, value=30000.0)
policy_sales_channel = st.number_input('Policy Sales Channel', min_value=0.0, max_value=200.0, value=26.0)
vintage = st.number_input('Vintage (Days with Company)', min_value=0, max_value=500, value=200)

# Convert categorical inputs to match trained model encoding
input_data = {
    "Gender": [1 if gender == 'Male' else 0],
    "Age": [age],
    "Driving_License": [driving_license],
    "Region_Code": [region_code],
    "Previously_Insured": [previously_insured],
    "Vehicle_Age": [2 if vehicle_age == '> 2 Years' else (1 if vehicle_age == '1-2 Year' else 0)],
    "Vehicle_Damage": [1 if vehicle_damage == 'Yes' else 0],
    "Annual_Premium": [annual_premium],
    "Policy_Sales_Channel": [policy_sales_channel],
    "Vintage": [vintage]
}

# Convert input to DataFrame
X_input = pd.DataFrame(input_data)

# Predict button
if st.button("Predict"):
    prediction = model.predict(X_input)[0]
    result = "Interested" if prediction == 1 else "Not Interested"
    st.write(f"Prediction: **{result}**")