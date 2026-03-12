# Exam Anxiety Detector

## Overview

The **Exam Anxiety Detector** is an AI-based application that analyzes text related to exam experiences and predicts the anxiety level of a student.
It uses a **BERT (Bidirectional Encoder Representations from Transformers)** model trained on mental health text data.

The system allows users to type their thoughts about exams and receive a prediction of their anxiety level.

---

## Technologies Used

* Python
* BERT Transformer Model
* FastAPI (Backend API)
* Streamlit (Frontend Interface)
* HuggingFace Transformers
* PyTorch

---

## How the System Works

1. The user types text describing their feelings about exams.
2. The Streamlit interface sends the text to the FastAPI backend.
3. The trained BERT model processes the text.
4. The system predicts the anxiety level.
5. The result is displayed to the user.

---

## Project Structure

Exam Anxiety Detector
│
├── backend
│   └── main.py (FastAPI backend)
│
├── frontend
│   └── app.py (Streamlit interface)
│
├── models
│   └── checkpoint-8000 (trained BERT model)
│
├── requirements.txt
└── README.md

---

## How to Run the Project

### Step 1: Install Required Libraries

pip install -r requirements.txt

### Step 2: Start Backend Server

cd backend
uvicorn main:app --reload

### Step 3: Start Frontend Interface

cd frontend
streamlit run app.py

---

## Output

The system predicts three anxiety levels:

* Low Anxiety
* Moderate Anxiety
* High Anxiety

---

## Author

Sujal
