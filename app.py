import streamlit as st
import numpy as np
import joblib
import requests
import base64

# Load the pre-trained model
model = joblib.load("xgb_diabetes_model.pkl")

# OpenRouter API key
with open("secret.key", "r") as f:
    encoded_key = f.read().strip()

OPENROUTER_API_KEY = base64.b64decode(encoded_key.encode()).decode()

def generate_health_advice(probability, age, bmi, glucose, hba1c, hypertension):
    prompt = (
        f"The user is {age} years old, has a BMI of {bmi:.1f}, a blood glucose level of {glucose} mg/dL, "
        f"HbA1c level of {hba1c}%, and {'has' if hypertension else 'does not have'} hypertension. "
        f"The predicted probability of having diabetes is {probability:.1f}%. "
        f"Generate a clear, friendly paragraph explaining this person's potential health situation, risks, and suggest lifestyle or medical advice for the user."
    )

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are a helpful medical assistant that provides diabetes-related advice."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Failed to generate advice: {e}"

# Streamlit UI
st.title("🩺 Diabetes Risk Prediction")
st.markdown("Enter your health details to assess diabetes risk and receive AI-generated health advice.")

age = st.number_input("Age", min_value=1, max_value=120, value=30)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=60.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
hba1c = st.number_input("HbA1c Level (%)", min_value=3.0, max_value=15.0, value=5.5)
glucose = st.number_input("Blood Glucose Level (mg/dL)", min_value=50, max_value=400, value=100)
gender = st.selectbox("Gender", ["Male", "Female"])
hypertension = st.selectbox("Do you have hypertension?", ["No", "Yes"])

# Calculate BMI
bmi = weight / (height ** 2)
gender_encoded = 0 if gender == "Male" else 1
hypertension_encoded = 1 if hypertension == "Yes" else 0

input_data = np.array([[age, bmi, hba1c, glucose, gender_encoded, hypertension_encoded]])

if st.button("🔍 Predict"):
    prediction = model.predict_proba(input_data)[0][1]
    percent = round(prediction * 100, 2)

    st.subheader(f"🧠 Estimated Diabetes Probability: **{percent:.1f}%**")
    with st.spinner("Generating personalized health advice..."):
        advice = generate_health_advice(percent, age, bmi, glucose, hba1c, hypertension_encoded)
        st.markdown(f"💬 **AI Advice:**\n\n{advice}")
