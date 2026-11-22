from fastapi import FastAPI

from model.models import LeaveRequest, LeaveResponse
from service.services import get_leave_guidance

app = FastAPI(
  title="AI HR Leave Guidance Assistant",
  version="1.0"
)

@app.get("/")
def home():
  return {
    "message": "Welcome to the AI HR Leave Guidance Assistant",
    "application": "AI HR Leave Guidance Assistant"
  }


@app.get("/health")
def health():
  return {"status": "healthy"}


@app.post("/leave/guide", response_model=LeaveResponse)
def leave_guide(data: LeaveRequest):
  return get_leave_guidance(data)