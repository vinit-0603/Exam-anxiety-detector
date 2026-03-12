# AI Based Exam Anxiety Detector

## Overview

The **AI Based Exam Anxiety Detector** is a Natural Language Processing (NLP) application that analyzes students’ written thoughts or feelings about upcoming exams and classifies their anxiety level. The system uses a **BERT-based language model** to understand emotional patterns in text and categorize anxiety into three levels:

* **Low Anxiety**
* **Moderate Anxiety**
* **High Anxiety**

The purpose of the system is to help students become aware of their emotional state and to assist educational institutions in identifying periods of heightened academic stress. This tool is designed strictly for **supportive and educational purposes**, not for clinical diagnosis.

---

## Problem Statement

Students often experience exam stress but may not openly communicate their anxiety. Traditional methods like surveys or manual observation are slow and subjective. An automated system that analyzes text inputs can provide **real-time insights into students’ emotional states** and help institutions offer timely support.

---

## Key Features

* Text-based **exam anxiety analysis**
* Classification into **Low, Moderate, and High anxiety**
* **BERT-based NLP model** for contextual understanding
* Interactive **web interface**
* Real-time prediction and feedback
* Visual indicators and supportive tips
* Ethical handling of user input (anonymous and non-diagnostic)

---

## Technology Stack

### Programming Language

* Python

### AI / Machine Learning

* BERT Transformer Model
* Natural Language Processing (NLP)

### Frameworks

* FastAPI – backend API
* Streamlit – frontend user interface

### Libraries

* transformers
* torch
* pandas
* numpy
* scikit-learn

### Development Tools

* VS Code
* Git and GitHub

---

## System Architecture

The project follows a **full-stack AI architecture** consisting of three main components:

1. **Data Processing Layer**

   * Collect and preprocess student text input
   * Clean and normalize text data

2. **AI Model Layer**

   * BERT model analyzes emotional context
   * Classifies text into anxiety levels

3. **Application Layer**

   * FastAPI backend processes requests
   * Streamlit frontend provides an interactive interface

---

## Project Workflow

1. Dataset collection related to exam stress and anxiety
2. Data preprocessing and text cleaning
3. Label mapping for anxiety categories
4. Training or using a pretrained BERT model
5. Model evaluation and performance analysis
6. Backend API creation using FastAPI
7. Frontend interface development using Streamlit
8. Integration and deployment of the system

---

## Example User Scenario

**Scenario: Pre-Exam Student Reflection**

A student writes:
“I feel very nervous about my exams and I’m afraid I might forget everything during the test.”

The system processes the text and predicts:

**Anxiety Level: High Anxiety**

It then displays calming suggestions or tips to help manage exam stress.

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/exam-anxiety-detector.git
```

### 2. Navigate to the Project Directory

```
cd exam-anxiety-detector
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Backend Server

```
uvicorn main:app --reload
```

### 5. Run Frontend

```
streamlit run app.py
```

---

## Ethical Considerations

* The system does **not diagnose mental health conditions**
* All user input should be **anonymous**
* Predictions are used only for **awareness and support**

---

## Future Improvements

* Improve dataset size and diversity
* Fine-tune BERT with domain-specific anxiety datasets
* Add multilingual support
* Integrate voice-based emotion detection
* Provide personalized stress-management recommendations

---

## Author

Vinit Kumar

---

## License

This project is intended for educational and research purposes.
