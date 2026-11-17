from fastapi import FastAPI

from model.request_model import HospitalAskRequest
from model.response_model import HospitalAskResponse
from service.agents_service import process_hospital_query
app = FastAPI(
    title="AI Hospital Management System"
)


@app.get("/")
def health_check():
    return {
        "message": "AI Hospital Management System"
    }


@app.get("/health")
def health_check():
    return {
        "message": "Application is running"
    }


@app.post("/hospital/ask", response_model=HospitalAskResponse)
def ask_hospital(request: HospitalAskRequest):
    result = process_hospital_query(request)
    return result
