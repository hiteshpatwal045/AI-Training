from model.claim_request import ClaimRequest
from model.claim_response import ClaimResponse, ClaimComparisonResponse

# ---------- Fictional training rules ----------
MAX_COVERAGE_LIMIT = 300000
DEDUCTIBLE = 2000
PREMIUM_DEDUCTIBLE_DISCOUNT = 0.10
INSPECTION_FEE = 1000
GST_RATE = 0.18
NO_CLAIM_BONUS_RATE = 0.20


def get_depreciation_rate(vehicle_age_years: int) -> float:
  if vehicle_age_years <= 2:
    return 0.05
  if vehicle_age_years <= 5:
    return 0.15
  return 0.30


def calculate_claim(request: ClaimRequest) -> ClaimResponse:
  # 1. Depreciation
  depreciation_rate = get_depreciation_rate(request.vehicle_age_years)
  depreciation_amount = request.claimed_repair_cost * depreciation_rate

  # 2. Eligible and covered amount
  eligible_repair_amount = request.claimed_repair_cost - depreciation_amount
  coverage_limit = min(request.coverage_limit, MAX_COVERAGE_LIMIT)
  covered_amount = min(eligible_repair_amount, coverage_limit)

  # 3. Deductible (Premium customers get 10% off the deductible)
  deductible = DEDUCTIBLE
  if request.customer_category == "Premium":
    deductible = DEDUCTIBLE * (1 - PREMIUM_DEDUCTIBLE_DISCOUNT)

  # 4. Claim payout
  claim_payout = max(0, covered_amount - deductible)

  # 5. Inspection fee and GST (paid by the customer)
  inspection_fee = INSPECTION_FEE
  gst = INSPECTION_FEE * GST_RATE

  # 6. Net benefit
  net_customer_benefit = claim_payout - (inspection_fee + gst)

  # 7. No-claim bonus (only if no claim is filed)
  no_claim_bonus = 0
  if not request.claim_filed:
    no_claim_bonus = request.next_renewal_base_premium * NO_CLAIM_BONUS_RATE

  return ClaimResponse(
    customer_name=request.customer_name,
    depreciation_rate=round(depreciation_rate, 2),
    depreciation_amount=round(depreciation_amount, 2),
    eligible_repair_amount=round(eligible_repair_amount, 2),
    covered_amount=round(covered_amount, 2),
    deductible=round(deductible, 2),
    claim_payout=round(claim_payout, 2),
    inspection_fee=round(inspection_fee, 2),
    gst=round(gst, 2),
    net_customer_benefit=round(net_customer_benefit, 2),
    no_claim_bonus=round(no_claim_bonus, 2),
  )


def compare_claim(request: ClaimRequest) -> ClaimComparisonResponse:
  regular = calculate_claim(
    request.model_copy(update={"customer_category": "Regular"})
  )
  premium = calculate_claim(
    request.model_copy(update={"customer_category": "Premium"})
  )

  return ClaimComparisonResponse(
    customer_name=request.customer_name,
    regular=regular,
    premium=premium,
    payout_difference=round(premium.claim_payout - regular.claim_payout, 2),
  )


def get_rules() -> dict:
  return {
    "note": "All rules are fictional and for classroom practice only.",
    "claimed_repair_cost": "Rs 5,000 to Rs 10,00,000",
    "depreciation": {
      "vehicle_age_0_to_2_years": "5%",
      "vehicle_age_3_to_5_years": "15%",
      "vehicle_age_6_plus_years": "30%",
    },
    "deductible": "Rs 2,000 per approved claim",
    "coverage_limit": "Maximum Rs 3,00,000 per claim",
    "loyalty_benefit": "Premium customers get a 10% reduction in the deductible",
    "inspection_fee": "Rs 1,000 per claim",
    "gst": "18% on the inspection fee only",
    "no_claim_bonus": "20% discount on next renewal base premium if no claim is filed",
  }