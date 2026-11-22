from fastapi import FastAPI

from fastapi import FastAPI
from model.models import TrainingResponse,TrainingRequest
from service.services import recommend_meal


app = FastAPI(
  title="AI EMployee Training",
  version="1.0"
)


@app.get("/")
def home():
  return {
    "message":"AI Employee Training"
  }

@app.post("/api/v1",response_model=TrainingResponse)
def analyze_(req : TrainingRequest):
  result = recommend_meal(req)
  return result