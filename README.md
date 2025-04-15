# 🏥 Hospital Readmission Prediction App

This Streamlit app uses a machine learning model to predict the likelihood of a diabetic patient being readmitted to the hospital. It is designed to help healthcare professionals make data-driven decisions and identify high-risk patients.

## 🚀 App Link

👉 [Launch the App](
https://francisbright1-readmission-app-app-muqxfb.streamlit.app/
)

## 📊 Problem Statement

Hospital readmissions among diabetic patients can result in increased healthcare costs and patient burden. This app analyzes patient data and predicts the chances of readmission using a trained machine learning model.

## 🧠 Model Overview

- **Model Type**: Logistic Regression / Random Forest / (Specify your model)
- **Target Variable**: Readmitted (Yes / No)
- **Features Used**:
  - Age
  - Number of previous visits
  - Glucose level
  - A1C test result
  - Number of medications
  - Days spent in hospital
    

## 🛠 How to Use

1. Open the app using the link above.
2. Enter the patient details in the sidebar.
3. Click "Predict Readmission".
4. View the prediction and risk level.

## 🧪 Technologies Used

- Python
- Streamlit
- scikit-learn
- pandas
- matplotlib / seaborn
- pickle (for model serialization)

## 🗃️ Project Structure
readmission_app/
├── app.py                 # Streamlit application code
├── model.pkl              # Trained machine learning model (serialized with pickle)
├── X_columns.pkl          # Pickled list of feature columns used during model training
├── requirements.txt       # List of required Python packages for the app to run
├── README.md              # Documentation and usage guide (optional but recommended)
├── .gitignore             # (Optional) Files/folders to ignore in Git

