from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from config.settings import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_API_VERSION,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT
)
from model.models import (AstronautRequest,AstronautResponse)
from prompt.prompts import (HUMAN_PROMPT,SYSTEM_PROMPT)

llm = AzureChatOpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  api_version=AZURE_OPENAI_API_VERSION,
  azure_deployment=AZURE_OPENAI_DEPLOYMENT,
  azure_endpoint=AZURE_OPENAI_ENDPOINT,
)


structure_llm = llm.with_structured_output(
  AstronautResponse
)

prompt = ChatPromptTemplate.from_messages([
  ("system",SYSTEM_PROMPT),
  ("user",HUMAN_PROMPT)
])

chain = prompt | structure_llm

def analyze(request : AstronautRequest):

  result = chain.invoke({
    "ast_id": request.ast_id,
    "ast_name" : request.ast_name,
    "age" : request.age,
    "training_hours" : request.training_hours,
    "medical_clearance" : request.medical_clearance,
    "previous_missions" : request.previous_missions
  })

  return result