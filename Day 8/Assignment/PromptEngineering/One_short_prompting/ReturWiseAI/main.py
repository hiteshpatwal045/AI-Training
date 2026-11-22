from fastapi import FastAPI
from model.request_model import ReturnRequest
from model.response_model import ReturnResponse
from service.ai_service import analyze_return

app = FastAPI(
  title="ReturnWise AI",
  version="1.0"
)


@app.get("/")
def home():
  return {
    "message": "Welcome to ReturnWise AI",
    "application": "ReturnWise AI"
  }


@app.get("/health")
def health():
  return {"status": "healthy"}


@app.post("/api/returns/analyze", response_model=ReturnResponse, tags=["Returns"])
def analyze(request: ReturnRequest):
  return analyze_return(request)