from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config.settings import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_API_VERSION,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT
)
from model.models import LeaveRequest, LeaveAnalysis, LeaveResponse
from prompt.prompts import SYSTEM_PROMPT, HUMAN_PROMPT

# Create the LLM
llm = AzureChatOpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  azure_deployment=AZURE_OPENAI_DEPLOYMENT,
  azure_endpoint=AZURE_OPENAI_ENDPOINT,
  api_version=AZURE_OPENAI_API_VERSION,
)

structured_llm = llm.with_structured_output(LeaveResponse)

prompt = ChatPromptTemplate.from_messages(
  [
    ("system", SYSTEM_PROMPT),
    ("user", HUMAN_PROMPT),
  ]
)

chain = prompt | structured_llm


def get_leave_guidance(request: LeaveRequest) -> LeaveResponse:
  result = chain.invoke(
    {
      "employee_id": request.employee_id,
      "employee_name": request.employee_name,
      "leave_type": request.leave_type,
      "days_requested": request.days_requested,
      "question": request.question,
    }
  )

  analysis = LeaveAnalysis(
    category=result.analysis.category,
    urgency=result.analysis.urgency,
    requires_hr_review=result.analysis.requires_hr_review,
    summary=result.analysis.summary,
  )

  return LeaveResponse(
    employee_id=request.employee_id,
    employee_name=request.employee_name,
    analysis=analysis,
    guidance=result.guidance,
    next_step=result.next_step,
    disclaimer=result.disclaimer,
    status="success",
  )