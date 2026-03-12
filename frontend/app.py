import streamlit as st
import requests

st.title("Exam Anxiety Detector")

text = st.text_area("Enter your thoughts about exams")

if st.button("Predict Anxiety Level"):

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        params={"text": text}
    )

    result = response.json()

    level = result["anxiety_level"]

    if level == 0:
        st.success("Low Anxiety — You seem calm about exams.")
    elif level == 1:
        st.warning("Moderate Anxiety — Some exam stress detected.")
    else:
        st.error("High Anxiety — Strong exam anxiety detected.")