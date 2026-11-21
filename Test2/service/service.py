from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from model.models import (EmpResponse, EmpRequest)
from config.settings import (
    OPENAI_API_KEY,
    OPENAI_API_VERSION,
    OPENAI_ENDPOINT,
    OPENAI_MODEL_NAME
)
from prompt.prompts import (HUMAN_PROMPT, SYSTEM_PROMPT)

llm = AzureChatOpenAI(
    api_key=OPENAI_API_KEY,
    azure_endpoint=OPENAI_ENDPOINT,
    azure_deployment=OPENAI_MODEL_NAME,
    api_version=OPENAI_API_VERSION
)

structured_llm = llm.with_structured_output(
    EmpResponse
)

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("user", HUMAN_PROMPT)
])

chain = prompt | structured_llm


def analyze(request: EmpRequest):

    result = chain.invoke({
        "employee_id": request.employee_id,
        "employee_name": request.employee_name,
        "leave_type": request.leave_type,
        "number_of_days": request.number_of_days,
        "reason": request.reason
    })

    return result


def analyze_response(request: EmpRequest) -> EmpResponse:

    result = chain.invoke({
        "employee_id": request.employee_id,
        "employee_name": request.employee_name,
        "leave_type": request.leave_type,
        "number_of_days": request.number_of_days,
        "reason": request.reason
    })

    return result
