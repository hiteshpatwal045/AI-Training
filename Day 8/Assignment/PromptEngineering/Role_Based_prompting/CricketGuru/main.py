from fastapi import FastAPI

from model.cricket_model import (CricketRequest,CricketResponse)
from service.cricket_service import analyse_cricket_request

app = FastAPI(
  title="CricketGuru Role Based Prompting API"
)

@app.get("/")
def home():
  return {
    "message":"Hello Welcome to FastAPI"
  }

@app.get("/api/cricket/health")
def health_check():
  return {
    "status" : "Working",
    "message" : "Cricket API is running"
  }

@app.get("/api/cricket/role")
def get_role():
  return {
    "role":"Cricket Knowledge AI Assistant"
  }


@app.post("/api/cricket/task",response_model=CricketResponse)
def cricket_question(request : CricketRequest):
  return analyse_cricket_request(request)