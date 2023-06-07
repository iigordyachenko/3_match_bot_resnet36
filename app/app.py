from fastapi import FastAPI
import sys
sys.path.append('/workdir/')

from model.model import load_model

model = None
app = FastAPI()

# create a route
@app.get("/")
def index():
    return {"text": "3_match≈"}


# Register the function to run during startup
@app.on_event("startup")
def startup_event():
    global model
    model = load_model()


# Your FastAPI route handlers go here
@app.post("/predict")
def predict_sentiment(matrix: dict):
    angle = model(matrix)
    return angle