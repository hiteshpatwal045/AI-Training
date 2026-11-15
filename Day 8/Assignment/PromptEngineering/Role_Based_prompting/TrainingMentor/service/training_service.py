from openai import OpenAI

from model.training_model import (TrainingRequest,TrainingResponse)
from prompt.training_prompt import (HUMAN_PROMPT,SYSTEM_PROMPT)
from config.setting import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT
)


llm = OpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1"
)

#  emp_name
#  exp_level
#  question

def llm_analyze(request : TrainingRequest) -> TrainingResponse:

  user_prompt = HUMAN_PROMPT.format(
    emp_name=request.emp_name,
    exp_level=request.exp_level,
    question=request.question
  )

  response = llm.responses.parse(
    model=AZURE_OPENAI_DEPLOYMENT,
    instructions=SYSTEM_PROMPT,
    input=user_prompt,
    text_format=TrainingResponse
  )

  return response.output_parsed