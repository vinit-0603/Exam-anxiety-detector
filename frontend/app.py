import streamlit as st

st.title("AI Exam Anxiety Detector")

text = st.text_area("Enter your exam thoughts")

if st.button("Analyze Anxiety"):

    if "nervous" in text or "scared" in text or "fail" in text:
        st.error("High Anxiety 😟")

    elif "worried" in text or "stress" in text:
        st.warning("Moderate Anxiety 😐")

    else:
        st.success("Low Anxiety 😊")
