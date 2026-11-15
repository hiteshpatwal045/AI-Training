from fastapi import FastAPI

from config.setting import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_MODEL_DEPLOYMENT
)
from model.student_model import (StudentPerformanceRequest, ModelResponse)
from prompt.student_prompt import (HUMAN_PROMPT, SYSTEM_PROMPT)
from service.student_service import analyze_student_profile

app = FastAPI(
    title="Student Chain Of Thoughts API",
    version="1.0"
)


@app.get("/")
def Home():
    return {
        "message": "Student Chain of Thoughts API"
    }


@app.post("/v1/api/data_analysis", response_model=ModelResponse)
def data_analysis(data: StudentPerformanceRequest):
    return analyze_student_profile(data)
