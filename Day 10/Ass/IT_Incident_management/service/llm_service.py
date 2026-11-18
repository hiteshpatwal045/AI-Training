from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
)
from model.incident_model import IncidentRequest, IncidentResponse
from prompt.incident_prompt import SYSTEM_PROMPT, HUMAN_PROMPT

llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
)

# LLM now returns an IncidentResponse object
structured_llm = llm.with_structured_output(IncidentResponse)

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("user", HUMAN_PROMPT),
])

chain = prompt | structured_llm


def analyze_incident(request: IncidentRequest) -> IncidentResponse:
    
    result = chain.invoke({
        "employee_id": request.employee_id,
        "employee_name": request.employee_name,
        "department": request.department,
        "issue": request.issue,
    })

    return result