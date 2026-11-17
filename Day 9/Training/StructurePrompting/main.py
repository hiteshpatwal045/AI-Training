from fastapi import FastAPI
from model.structure_models import (LearnerRequest, LearnerResponse)
from service.structure_service import analyze_learner

app = FastAPI(
    title="Learner Performance Analysis AI Assistant",
    version="1.1"
)


@app.get("/")
def home():
    return {
        "message": "Learner Performance Analysis AI Assistant"
    }


@app.post("/api/v1/analyze", response_model=LearnerResponse)
def analyze(data: LearnerRequest):
    return analyze_learner(data)
