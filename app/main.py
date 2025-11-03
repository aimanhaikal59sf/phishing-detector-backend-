from fastapi import FastAPI
from app.schemas import URLInput
from app.model import predict_url
app = FastAPI(title="Phishing Detection API")
@app.get("/")
def home():
    return {"message": "Phishing Detection API is running!"}
@app.post("/predict")
def predict(input_data: URLInput):
    result = predict_url(input_data.url)
    return {"url": input_data.url, "prediction": result}
