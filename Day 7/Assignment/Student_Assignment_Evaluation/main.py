from fastapi import FastAPI

from model.student_model import (ResponseStudent,RequestStudent)
from service.student_service import student_evaluation

app = FastAPI(
  title="Student Assignment Evaluation API",
  version="1.0"
)


@app.get("/")
def home():
  return {
    "message" : "Student Assignment Evaluation API"
  }

@app.post("/api/v1/evaluate-assignment", response_model=ResponseStudent)
def getResponse(request : RequestStudent):
  return student_evaluation(request)