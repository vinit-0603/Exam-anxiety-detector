from fastapi import FastAPI
from transformers import BertTokenizer, BertForSequenceClassification
import torch

app = FastAPI()

model_path = "../models/checkpoint-8000"

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained(model_path)

@app.get("/")
def home():
    return {"message": "Exam Anxiety Detector API"}

@app.post("/predict")
def predict(text: str):

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    outputs = model(**inputs)

    prediction = torch.argmax(outputs.logits).item()

    return {"anxiety_level": prediction}