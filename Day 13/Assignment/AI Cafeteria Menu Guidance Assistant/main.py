from fastapi import FastAPI, HTTPException

from model.models import CafeteriaRequest, CafeteriaResponse
from service.services import recommend_meal

app = FastAPI(
  title="AI Cafeteria Menu Guidance Assistant",
  version="1.0"
)


@app.get("/")
def home():
  return {
    "message": "Welcome to AI Cafeteria Menu Guidance Assistant"
  }


@app.get("/health")
def health():
  return {
    "status": "ok"
  }


@app.post("/cafeteria/recommend", response_model=CafeteriaResponse)
def recommend(request: CafeteriaRequest):
  return recommend_meal(request)
