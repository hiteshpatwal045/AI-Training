import json

from openai import AzureOpenAI

from config.setting import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_API_VERSION,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT,
)
from model.request_model import ReturnRequest
from model.analysis_model import ReturnAnalysis
from model.response_model import ReturnResponse
from prompt.one_shot_prompt import SYSTEM_PROMPT, HUMAN_PROMPT


llm = AzureOpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  azure_endpoint=AZURE_OPENAI_ENDPOINT,
  azure_deployment=AZURE_OPENAI_DEPLOYMENT,
  api_version=AZURE_OPENAI_API_VERSION,
)


def analyze_return(request: ReturnRequest) -> ReturnResponse:

  user_prompt = HUMAN_PROMPT.format(
    request_id=request.request_id,
    order_id=request.order_id,
    product_category=request.product_category,
    days_since_delivery=request.days_since_delivery,
    item_price_inr=request.item_price_inr,
    reason=request.reason,
    item_condition=request.item_condition,
    evidence_provided=", ".join(request.evidence_provided),
    customer_description=request.customer_description,
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
    raise ValueError("Empty response")

  data = json.loads(ai_text)

  analysis = ReturnAnalysis(
    issue_category=data["issue_category"],
    urgency=data["urgency"],
    evidence_sufficiency=data["evidence_sufficiency"],
    missing_information=data["missing_information"],
    reasoning_summary=data["reasoning_summary"],
  )

  return ReturnResponse(
    request_id=request.request_id,
    analysis=analysis,
    recommended_next_steps=data["recommended_next_steps"],
    human_review_required=True,
    customer_message_draft=data["customer_message_draft"],
  )