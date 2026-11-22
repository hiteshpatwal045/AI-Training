from openai import AzureOpenAI

from config.setting import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_API_VERSION,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT,
)
from model.claim_request import ClaimRequest
from model.claim_response import ClaimResponse
from prompt.claim_prompt import SYSTEM_PROMPT, HUMAN_PROMPT
from service.claim_calculator import calculate_claim


llm = AzureOpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  azure_endpoint=AZURE_OPENAI_ENDPOINT,
  azure_deployment=AZURE_OPENAI_DEPLOYMENT,
  api_version=AZURE_OPENAI_API_VERSION,
)


def analyze_claim(request: ClaimRequest) -> ClaimResponse:

  # Python calculates every amount first
  result = calculate_claim(request)

  user_prompt = HUMAN_PROMPT.format(
    customer_name=request.customer_name,
    customer_category=request.customer_category,
    policy_number=request.policy_number,
    vehicle_age_years=request.vehicle_age_years,
    claimed_repair_cost=request.claimed_repair_cost,
    coverage_limit=request.coverage_limit,
    next_renewal_base_premium=request.next_renewal_base_premium,
    claim_filed=request.claim_filed,
    depreciation_rate_percent=round(result.depreciation_rate * 100),
    depreciation_amount=result.depreciation_amount,
    eligible_repair_amount=result.eligible_repair_amount,
    covered_amount=result.covered_amount,
    deductible=result.deductible,
    claim_payout=result.claim_payout,
    inspection_fee=result.inspection_fee,
    gst=result.gst,
    inspection_total=round(result.inspection_fee + result.gst, 2),
    net_customer_benefit=result.net_customer_benefit,
    no_claim_bonus=result.no_claim_bonus,
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
    ]
  )

  explanation = response.choices[0].message.content

  if not explanation:
    raise ValueError("AI returned empty response")

  # The AI only adds the explanation; the amounts stay as Python calculated them
  result.ai_explanation = explanation

  return result