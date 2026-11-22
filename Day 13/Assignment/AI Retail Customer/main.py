from fastapi import FastAPI
from model.models import CustomerRequest, CustomerResponse
from service.services import analyze_data

app = FastAPI(
  title="AI Retail customer",
  version="1.1"
)


@app.get("/")
def home():
  return {
    "message":"AI Retail Customer"
  }

@app.post("/api/v1",response_model=CustomerResponse)
def analyzee(req : CustomerRequest):
  result = analyze_data(req)
  return result