from openai import OpenAI
from prompts.emp_prompt import SYSTEM_PROMPT, HUMAN_PROMPT
from models.emp_models import LeaveRequest, LeaveResponse
from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)

# Create LLM client outside the function
llm = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1"
)


def review_leave(data: LeaveRequest) -> LeaveResponse:
    user_prompt = HUMAN_PROMPT.format(
        employee_name=data.employee_name,
        department=data.department,
        leave_type=data.leave_type,
        start_date=data.start_date,
        end_date=data.end_date,
        reason=data.reason
    )

    response = llm.responses.parse(
        model=AZURE_OPENAI_DEPLOYMENT,
        instructions=SYSTEM_PROMPT,
        input=user_prompt,
        text_format=LeaveResponse
    )

    return response.output_parsed