from fastapi import FastAPI
from service.emp_service import review_leave
from models.emp_models import LeaveRequest, LeaveResponse

app = FastAPI(
    title="Leave Request Review AI",
    version="1.0"
)

@app.get("/")
def home():
  return {
    "message" : "Leave Request API"
  }

@app.post("/api/v1/review-leave-request", response_model=LeaveResponse)
def review(data: LeaveRequest):
    return review_leave(data)