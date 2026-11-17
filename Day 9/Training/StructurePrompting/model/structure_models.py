from pydantic import BaseModel, Field


class LearnerRequest(BaseModel):
    learnerName : str = Field(min_length=1)
    department : str = Field(min_length=1)
    pythonScore : int = Field(ge=0,le=100)
    sqlScore : int = Field(ge=0,le=100)
    fastapiScore : int = Field(ge=0,le=100)
    attendancePercentage : float = Field(ge=0,le=100)
    assignmentCompleted : int = Field(ge=0)
    totalAssignment : int = Field(gt=0)


class LearnerAnalysis(BaseModel):

    averageScore : float
    performanceLevel : str
    strongestTechonology : str
    weakestTechnology : str
    technicalAssesment : str
    recommendedLearning : list[str]

class LearnerResponse(BaseModel):

    learnerName : str
    department : str
    analysis : LearnerAnalysis
    finalRecommendation : str
    