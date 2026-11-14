from openai import OpenAI
from prompt.emp_prompt import (HUMAN_PROMPT,SYSTEM_PROMPT)
from model.emp_models import (ProductResponse,ProductRequest)

from config.settings import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT
)

# create llm
llm = OpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1"
)


def create_product_review(request : ProductRequest) -> ProductRequest:
  #prepare human prompt
  user_prompt = HUMAN_PROMPT.format(
    product_id=request.product_id,
    product_name=request.product_name,
    customer_name=request.customer_name,
    rating=request.rating,
    review_text=request.review_text
  )
  # invoke llm
  response = llm.responses.parse(
    model=AZURE_OPENAI_DEPLOYMENT,
    instructions=SYSTEM_PROMPT,
    input=user_prompt,
    text_format=ProductResponse
  )

  # extract generated response
  result = response.output_parsed

  # return response
  return result


