import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load("xgb_diabetes_model.pkl")

st.title("🩺 Diabetes Risk Prediction")

st.markdown("Enter the following health information to predict the likelihood of having diabetes:")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=30)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=60.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
hba1c = st.number_input("HbA1c Level (%)", min_value=3.0, max_value=15.0, value=5.5)
glucose = st.number_input("Blood Glucose Level (mg/dL)", min_value=50, max_value=400, value=100)
gender = st.selectbox("Gender", ["Male", "Female"])
hypertension = st.selectbox("Do you have hypertension?", ["No", "Yes"])

# Calculate BMI
bmi = weight / (height ** 2)  

# Convert categorical inputs
gender_encoded = 0 if gender == "Male" else 1
hypertension_encoded = 1 if hypertension == "Yes" else 0

# Prepare input for prediction
input_data = np.array([[age, bmi, hba1c, glucose, gender_encoded, hypertension_encoded]])

# Predict
if st.button("🔍 Predict Diabetes Risk"):
    prediction = model.predict_proba(input_data)[0][1]
    percent = round(prediction * 100, 2)

    st.subheader(f"🧠 Estimated Diabetes Probability: **{percent:.1f}%**")

    if percent > 70:
        st.error("⚠️ High risk of diabetes. Consider consulting a doctor.")
    elif percent > 30:
        st.warning("⚠️ Moderate risk. Stay cautious and monitor your health.")
    else:
        st.success("✅ Low risk. Keep maintaining a healthy lifestyle!")
