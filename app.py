import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load the model's input features
with open("X_columns.pkl", "rb") as f:
    feature_columns = pickle.load(f)

# Streamlit app UI
st.set_page_config(page_title="Readmission Risk Predictor", layout="centered")
st.title("🏥 Diabetes Readmission Risk Predictor")
st.write("Enter patient details to predict if they are likely to be readmitted.")

# Input fields for the user
num_medications = st.slider("Number of Medications", 0, 50, 10)
time_in_hospital = st.slider("Time in Hospit    al (days)", 1, 20, 5)
age_group = st.selectbox("Age Group", [
    '[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)', 
    '[50-60)', '[60-70)', '[70-80)', '[80-90)', '[90-100)'
])

# Build input dictionary
input_data = {
    'num_medications': num_medications,
    'time_in_hospital': time_in_hospital,
    # One-hot encode the selected age group
    'age_[0-10)': 0, 'age_[10-20)': 0, 'age_[20-30)': 0, 'age_[30-40)': 0,
    'age_[40-50)': 0, 'age_[50-60)': 0, 'age_[60-70)': 0, 'age_[70-80)': 0,
    'age_[80-90)': 0, 'age_[90-100)': 0
}
input_data[f'age_{age_group}'] = 1

# Fill in any other missing columns with zero
for col in feature_columns:
    if col not in input_data:
        input_data[col] = 0

# Convert to DataFrame with correct column order
input_df = pd.DataFrame([input_data])[feature_columns]

# Predict when button is clicked
if st.button("Predict Readmission Risk"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("⚠️ The patient is likely to be readmitted.")
    else:
        st.success("✅ The patient is not likely to be readmitted.")


