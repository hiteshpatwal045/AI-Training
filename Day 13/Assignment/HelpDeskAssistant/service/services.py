from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config.settings import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_API_VERSION,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT
)
from model.models import HelpdeskAnalysis, HelpdeskRequest, HelpdeskResponse
from prompt.prompts import HUMAN_PROMPT, SYSTEM_PROMPT

# Create the LLM
llm = AzureChatOpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  azure_deployment=AZURE_OPENAI_DEPLOYMENT,
  azure_endpoint=AZURE_OPENAI_ENDPOINT,
  api_version=AZURE_OPENAI_API_VERSION
)

# Make the LLM return a HelpdeskAnalysis object
structured_llm = llm.with_structured_output(HelpdeskAnalysis)

# Prompt Making
prompt = ChatPromptTemplate.from_messages(
  [
    ("system", SYSTEM_PROMPT),
    ("user", HUMAN_PROMPT)
  ]
)

# Create the Langchain
chain = prompt | structured_llm


# create the function
def analyze_issue(request: HelpdeskRequest) -> HelpdeskResponse:

  analysis = chain.invoke({
    "employee_id": request.employee_id,
    "employee_name": request.employee_name,
    "issue_type": request.issue_type,
    "issue_description": request.issue_description
  })

  return HelpdeskResponse(
    employee_id=request.employee_id,
    employee_name=request.employee_name,
    analysis=analysis,
    suggested_steps=analysis.suggested_steps,
  )