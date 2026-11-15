from fastapi import FastAPI

from service.clg_service import analyze_student_profile
from model.cllg_model import (
    StudentResponse,
    StudentRequest,
)

app = FastAPI(
    title="College Management One Shot prompting"
)


@app.get("/")
def home():
    return {
        "message": "College Management One Shot Prompting"
    }


@app.post("/v1/api/data_analysis", response_model=StudentResponse)
def data_analysis(data: StudentRequest):
    return analyze_student_profile(data)
