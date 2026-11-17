from openai import AzureOpenAI
import json
from config.settings import (AZURE_API_ENDPOINT,AZURE_OPENAI_API_KEY,AZURE_OPENAI_API_VERSION,AZURE_OPENAI_DEPLOYMENT)
from model.structure_models import (LearnerRequest,LearnerResponse,LearnerAnalysis)
from prompt.structure_prompt import (HUMAN_PROMPT,SYSTEM_PROMPT)

llm = AzureOpenAI(
    azure_endpoint=AZURE_API_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION
)


def analyze_learner(request: LearnerRequest) -> LearnerResponse:

    # step 01. Validate Assignment Count
    if request.assignmentCompleted > request.totalAssignment:
        raise ValueError(
            "Completed assignments cannot exceed total assignments."
        )

    # step 02. Validate Average Score
    average_score = round(
        (request.pythonScore + request.sqlScore + request.fastapiScore) / 3,
        2
    )

    # step 03. Determine Performance Level
    if average_score >= 85:
        performance_level = "Excellent"
    elif average_score >= 70:
        performance_level = "Good"
    elif average_score >= 50:
        performance_level = "Average"
    else:
        performance_level = "Needs Improvement"

    # step 04. Identity Strongest Technology
    scores = {
        "Python": request.pythonScore,
        "SQL": request.sqlScore,
        "FastAPI": request.fastapiScore
    }
    strongest_tech = max(scores, key=scores.get)

    # step 05. Identity Weakest Technology
    weakest_tech = min(scores, key=scores.get)

    # step 06. Calculate Assignment Completed
    assignment_percentage = round(
        (request.assignmentCompleted / request.totalAssignment) * 100, 2
    )

    # step 07. Human Prompt
    formatted_human_prompt = HUMAN_PROMPT.format(
        learnerName=request.learnerName,
        department=request.department,
        pythonScore=request.pythonScore,
        sqlScore=request.sqlScore,
        fastapiScore=request.fastapiScore,
        attendancePercentage=request.attendancePercentage,
        totalAssignment=request.totalAssignment,
        assignmentCompleted=request.assignmentCompleted,
        assignmentPercentage=assignment_percentage,
        averageScore=average_score,
        performanceLevel=performance_level,
        strongestTechonology=strongest_tech,
        weakestTechnology=weakest_tech
    )

    # step 08. Call Azure OpenAI
    response = llm.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": formatted_human_prompt}
        ]
    )

    # step 09. Parse JSON Response from LLM
    raw_content = response.choices[0].message.content
    llm_data = json.loads(raw_content)

    # step 10. Build LearnerAnalysis Object (enforcing server-calculated metrics)
    analysis = LearnerAnalysis(
        averageScore=average_score,
        performanceLevel=performance_level,
        strongestTechonology=strongest_tech,
        weakestTechnology=weakest_tech,
        technicalAssesment=llm_data["technicalAssesment"],
        recommendedLearning=llm_data["recommendedLearning"]
    )

    # step 11. Return Final LearnerResponse
    return LearnerResponse(
        learnerName=request.learnerName,
        department=request.department,
        analysis=analysis,
        finalRecommendation=llm_data["finalRecommendation"]
    )
