from fastapi import FastAPI, HTTPException

from model.models import HelpdeskRequest, HelpdeskResponse
from service.services import analyze_issue

app = FastAPI(
  title="AI IT Helpdesk Assistant",
  version="1.0"
)


@app.get("/")
def home():
  return {
    "message": "Welcome to AI IT Helpdesk Assistant"
  }


@app.get("/health")
def health():
  return {
    "status": "ok"
  }


@app.post("/helpdesk/analyze", response_model=HelpdeskResponse)
def analyze(request: HelpdeskRequest):
  return analyze_issue(request)