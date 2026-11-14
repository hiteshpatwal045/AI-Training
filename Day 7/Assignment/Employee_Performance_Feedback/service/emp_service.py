from openai import OpenAI
from prompts.emp_prompt import SYSTEM_PROMPT, HUMAN_PROMPT
from models.emp_models import EmployeeRequest, EmployeeResponse
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


def analyze_employee(data: EmployeeRequest) -> EmployeeResponse:
    user_prompt = HUMAN_PROMPT.format(
        employee_name=data.employee_name,
        reviewer_name=data.reviewer_name,
        project_name=data.project_name,
        performance_rating=data.performance_rating,
        feedback=data.feedback
    )

    response = llm.responses.parse(
        model=AZURE_OPENAI_DEPLOYMENT,
        instructions=SYSTEM_PROMPT,
        input=user_prompt,
        text_format=EmployeeResponse
    )

    return response.output_parsed