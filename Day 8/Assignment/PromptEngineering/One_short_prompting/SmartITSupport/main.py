from fastapi import FastAPI
from model.request_model import ITSupportRequest
from model.response_model import ITSupportResponse
from service.ai_service import analyze_ticket

app = FastAPI(title="SmartITSupport AI")


@app.get("/")
def home():
  return {
    "message":"Smart AI Support AI "
  }

@app.get("/api/tickets/health", tags=["IT Support"])
def health():
  return {"status": "ok"}


@app.post("/api/tickets/analyze", response_model=ITSupportResponse, tags=["IT Support"])
def analyze(request: ITSupportRequest):
  return analyze_ticket(request)