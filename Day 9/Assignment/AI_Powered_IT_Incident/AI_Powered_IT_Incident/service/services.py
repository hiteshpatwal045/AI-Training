from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config.settings import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_API_VERSION,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT,
)
from model.models import IncidentRequest, IncidentAnalysis
from prompt.prompts import SYSTEM_PROMPT, HUMAN_PROMPT


llm = AzureChatOpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  azure_deployment=AZURE_OPENAI_DEPLOYMENT,
  azure_endpoint=AZURE_OPENAI_ENDPOINT,
  api_version=AZURE_OPENAI_API_VERSION,
)


structured_llm = llm.with_structured_output(IncidentAnalysis)


prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("user", HUMAN_PROMPT),
  ]
)


chain = prompt | structured_llm


def analyze_incident(request: IncidentRequest) -> IncidentAnalysis:
  result = chain.invoke({
      "employee_id": request.employee_id,
      "employee_name": request.employee_name,
      "department": request.department,
      "issue": request.issue,
    }
  )

  return result