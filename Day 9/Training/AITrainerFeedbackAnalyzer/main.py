from fastapi import FastAPI

from model.trainer_feedback_model import (
    TrainerFeedbackResponse,
    TrainerFeedbackRequest
)
from service.llm_service import analyze_feedback

app = FastAPI(
    title="AI trainer Feedback Analyzer",
    version="1.1"
)


@app.get("/")
def home():
    return {
        "MESSAGE": "AI Trainer Feedback Analyzer"
    }


@app.post("/v1/api/analyze", response_model=TrainerFeedbackResponse)
def analyze(data: TrainerFeedbackRequest):
    return analyze_feedback(data)
