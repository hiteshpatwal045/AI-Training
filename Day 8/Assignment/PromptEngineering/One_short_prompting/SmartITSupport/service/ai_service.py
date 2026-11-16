import json
from openai import AzureOpenAI
from config.setting import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_API_VERSION,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT
)
from model.analysis_model import ITSupportAnalysis
from model.request_model import ITSupportRequest
from model.response_model import ITSupportResponse
from prompt.one_shot_prompt import (
  HUMAN_PROMPT,
  SYSTEM_PROMPT
)

llm = AzureOpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  api_version=AZURE_OPENAI_API_VERSION,
  azure_deployment=AZURE_OPENAI_DEPLOYMENT,
  azure_endpoint=AZURE_OPENAI_ENDPOINT
)


def analyze_ticket(request: ITSupportRequest) -> ITSupportResponse:

  user_prompt = HUMAN_PROMPT.format(
    ticket_id=request.ticket_id,
    employee_id=request.employee_id,
    employee_name=request.employee_name,
    department=request.department,
    issue_description=request.issue_description,
    affected_system=request.affected_system
  )

  response = llm.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT,
    messages=[
      {
        "role": "system",
        "content": SYSTEM_PROMPT
      },
      {
        "role": "user",
        "content": user_prompt
      }
    ],
    response_format={"type": "json_object"}
  )

  ai_text = response.choices[0].message.content

  if not ai_text:
    raise ValueError("Empty Response")

  data = json.loads(ai_text)

  analysis = ITSupportAnalysis(
    issue_category=data["issue_category"],
    priority_level=data["priority_level"],
    suspected_root_cause=data["suspected_root_cause"],
    impact_level=data["impact_level"],
    troubleshooting_steps=data["troubleshooting_steps"],
    estimated_resolution_time=data["estimated_resolution_time"]
  )

  return ITSupportResponse(
    ticket_id=request.ticket_id,
    ticket_status=data["ticket_status"],
    analysis=analysis,
    recommended_actions=data["recommended_actions"],
    escalation_required=data["escalation_required"],
    ai_summary=data["ai_summary"]
  )