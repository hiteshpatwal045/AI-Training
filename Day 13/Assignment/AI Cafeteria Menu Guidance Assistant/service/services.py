from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config.settings import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_API_VERSION,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT
)
from model.models import CafeteriaAnalysis, CafeteriaRequest, CafeteriaResponse
from prompt.prompts import HUMAN_PROMPT, SYSTEM_PROMPT

# Create the LLM
llm = AzureChatOpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  azure_deployment=AZURE_OPENAI_DEPLOYMENT,
  azure_endpoint=AZURE_OPENAI_ENDPOINT,
  api_version=AZURE_OPENAI_API_VERSION
)

# Make the LLM return a CafeteriaAnalysis object
structured_llm = llm.with_structured_output(CafeteriaAnalysis)

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
def recommend_meal(request: CafeteriaRequest) -> CafeteriaResponse:

  analysis = chain.invoke({
    "employee_id": request.employee_id,
    "employee_name": request.employee_name,
    "food_preference": request.food_preference,
    "budget": request.budget,
    "question": request.question
  })

  return CafeteriaResponse(
    employee_id=request.employee_id,
    employee_name=request.employee_name,
    analysis=analysis,
    suggested_meal=analysis.suggested_meal,
    estimated_price=analysis.estimated_price,
    reason=analysis.reason,
    status="success"
  )