from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from prompt.emp_prompt import HUMAN_PROMPT, SYSTEM_PROMPT
from model.emp_model import EmpRequest, EmpResponse
from config.settings import (
    AZURE_API_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT
)

# creating a llm
llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_API_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION
)

structure_llm = llm.with_structured_output(
    EmpResponse
)

prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", HUMAN_PROMPT)
    ])

chain = prompt | structure_llm


def analyze_output(request: EmpRequest) -> EmpResponse:
    result = chain.invoke({
        "emp_id": request.emp_id,
        "emp_name": request.emp_name,
        "emp_rating": request.emp_rating,
        "emp_weak_sub": request.emp_weak_sub
    })
    return EmpResponse(
        "emp_id":request.emp_id,
        "emp"
    )
