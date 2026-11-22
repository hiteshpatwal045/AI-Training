from fastapi import FastAPI
from model.claim_request import ClaimRequest
from model.claim_response import ClaimResponse, ClaimComparisonResponse
from service.claim_calculator import calculate_claim, compare_claim, get_rules
from service.ai_claim_service import analyze_claim

app = FastAPI(
  title="ClaimWise AI",
  version="1.0"
)

@app.get("/")
def home():
  return {
    "message": "Welcome to ClaimWise AI",
    "application": "ClaimWise AI"
  }


@app.get("/api/claims/health", tags=["Claims"])
def health():
  return {"status": "healthy"}


@app.post("/api/claims/calculate", response_model=ClaimResponse, tags=["Claims"])
def calculate(request: ClaimRequest):
  return calculate_claim(request)


@app.post("/api/claims/analyze", response_model=ClaimResponse, tags=["Claims"])
def analyze(request: ClaimRequest):
  return analyze_claim(request)


@app.post("/api/claims/compare", response_model=ClaimComparisonResponse, tags=["Claims"])
def compare(request: ClaimRequest):
  return compare_claim(request)


@app.get("/api/claims/rules", tags=["Claims"])
def rules():
  return get_rules()