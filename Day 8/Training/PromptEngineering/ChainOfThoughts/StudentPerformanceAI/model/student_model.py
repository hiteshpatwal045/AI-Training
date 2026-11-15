from pydantic import BaseModel, Field


class StudentPerformanceRequest(BaseModel):
    student_id: str
    student_name: str
    python_marks: float = Field(ge=0, le=100)
    sql_marks: float = Field(ge=0, le=100)
    fastapi_marks: float = Field(ge=0, le=100)


class StudentPerformanceAnalysis(BaseModel):
    total_marks: float
    average_marks: float
    grade: str
    result: str
    calculation_summary: str


class ModelResponse(BaseModel):
    student_id: str
    student_name: str
    analysis: StudentPerformanceAnalysis
    # improvement_suggestion: list[str]
