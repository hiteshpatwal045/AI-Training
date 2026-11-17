from openai import AzureOpenAI
import json
from config.setting import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_MODEL_DEPLOYMENT
)

from model.student_model import (
    StudentPerformanceAnalysis,
    StudentPerformanceRequest,
    ModelResponse
)

from prompt.student_prompt import (
    HUMAN_PROMPT,
    SYSTEM_PROMPT
)


llm = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_MODEL_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION
)


def analyze_student_profile(request: StudentPerformanceRequest) -> ModelResponse:

    user_prompt = HUMAN_PROMPT.format(
        student_id=request.student_id,
        student_name=request.student_name,
        python_marks=request.python_marks,
        sql_marks=request.sql_marks,
        fastapi_marks=request.fastapi_marks
    )

    response = llm.chat.completions.create(
        model=AZURE_OPENAI_MODEL_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        response_format={
            "type": "json_object"
        }
    )

    content = response.choices[0].message.content

    if not content:
        raise ValueError("AI returned empty response")

    ai_analysis = json.loads(content)

    analysis = StudentPerformanceAnalysis(
        total_marks=ai_analysis["total_marks"],
        average_marks=ai_analysis["average_marks"],
        grade=ai_analysis["grade"],
        result=ai_analysis["result"],
        calculation_summary=ai_analysis["calculation_summary"]
    )

    return ModelResponse(
        student_id=request.student_id,
        student_name=request.student_name,
        analysis=analysis,
        # improvement_suggestion=ai_analysis["improvement_suggestion"]
    )
