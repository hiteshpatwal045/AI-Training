from fastapi import FastAPI
from model.request_model import LearnerProgressRequest
from model.response import LearnerProgressResponse
from service.ai_service import llm_reponse

app = FastAPI(
  title="TrainingProgress AI",
  version="1.1"
)

@app.get("/")
def home():
  return {
    "message": "TrainignProgress AI"
  }


@app.get("/api/training/health", tags=["Training Progress"])
def health():
  return {
    "status": "Working-UP"
  }

@app.post("/api/training/analyze-progress", response_model=LearnerProgressResponse, tags=["Training Progress"])
def analyze(request: LearnerProgressRequest):
  return llm_reponse(request)