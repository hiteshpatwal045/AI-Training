from fastapi import FastAPI

from model.training_model import (
  TrainingRequest,
  TrainingResponse
)
from service.training_service import llm_analyze
app = FastAPI(
  title="Coforge AI Training Mentor",
  version="1.1"
)


@app.get("/")
def home():
  return {
    "message":"Coforge AI Training Mentor"
  }

@app.get("/api/training/health")
def health():
  return {
    "status":"working",
    "message":"Coforge AI Training Mentor"
  }

@app.get("/api/training/role")
def role():
  return {
    "role":"Senior Corporate IT Trainer"
  }

@app.post("/api/ai/analyse",response_model=TrainingResponse)
def llm_response(data : TrainingRequest):
  result = llm_analyze(data)
  print(result)
  return result