import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("student_model.pkl")

st.title("Student Pass/Fail Predictor")

st.write("Enter student details")

study_hours = st.number_input("Study Hours", 0, 12)
attendance = st.number_input("Attendance (%)", 0, 100)
assignments = st.number_input("Assignment Score", 0, 100)

if st.button("Predict"):
    
    input_data = np.array([[study_hours, attendance, assignments]])
    # Machine learning models expect data in array format.
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success("Student will PASS")
    else:
        st.error("Student will FAIL")