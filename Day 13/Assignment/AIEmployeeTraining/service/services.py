from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config.settings import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_API_VERSION,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT
)
from model.models import TrainingRequest, TrainingResponse, TrainingAnalysis
from prompt.prompts import HUMAN_PROMPT, SYSTEM_PROMPT

# Create the LLM
llm = AzureChatOpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  azure_deployment=AZURE_OPENAI_DEPLOYMENT,
  azure_endpoint=AZURE_OPENAI_ENDPOINT,
  api_version=AZURE_OPENAI_API_VERSION
)

# Make the LLM return a CafeteriaAnalysis object
structured_llm = llm.with_structured_output(TrainingResponse)

# Prompt Making
prompt = ChatPromptTemplate.from_messages(
  [
    ("system", SYSTEM_PROMPT),
    ("user", HUMAN_PROMPT)
  ]
)

chain = prompt | structured_llm

# create the function
def recommend_meal(request: TrainingRequest) -> TrainingResponse:

  data = chain.invoke({
    "employee_id": request.employee_id,
    "employee_name": request.employee_name,
    "topic": request.topic,
    "question": request.question
  })

  analysis = TrainingAnalysis(
    category = data.analysis.category,
    difficulty = data.analysis.difficulty,
    priority = data.analysis.priority,
    summary = data.analysis.summary
  )

  return TrainingResponse(
    employee_id = request.employee_id,
    employee_name = request.employee_name,
    topic =  data.topic,
    analysis = analysis,
    answer = data.answer,
    recommended_action = data.recommended_action,
    status = data.status
  )