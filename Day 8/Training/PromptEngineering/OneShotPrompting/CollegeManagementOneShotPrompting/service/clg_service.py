from openai import AzureOpenAI
import json

from config.settings import (
    AZURE_API_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_API_VERSION
)

from model.cllg_model import (
    StudentAnalysis,
    StudentRequest,
    StudentResponse
)
from prompt.cllg_prompt import (
    HUMAN_PROMPT,
    SYSTEM_PROMPT
)


# create the llm
llm = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_API_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION
)


def analyze_student_profile(request: StudentRequest) -> StudentResponse:

    user_prompt = HUMAN_PROMPT.format(
        student_id=request.student_id,
        student_name=request.student_name,
        course=request.course,
        semester=request.semester,
        percentage=request.percentage,
        primary_skill=request.primary_skill,
        career_goal=request.career_goal
    )

    # call llm
    response = llm.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
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

    # # extract ai response
    ai_text = response.choices[0].message.content
    if not ai_text:
        raise ValueError("AI return empty response  ")

    # convert JSON into pydantic
    # parsed_data.setdefault("student_name", request.student_name)
    # parsed_data.setdefault("course", request.course)
    # parsed_data.setdefault("semester", request.semester)
    # parsed_data.setdefault("percentage", request.percentage)
    # parsed_data.setdefault("primary_skill", request.primary_skill)
    # parsed_data.setdefault("career_goal", request.career_goal)

    # # convert JSON into pydantic
    ai_analysis = StudentAnalysis(**json.loads(ai_text))

    return StudentResponse(
        student_id=request.student_id,
        student_name=request.student_name,
        promptin_technique="One Shot Prompting",
        ai_analysis=ai_analysis
    )
