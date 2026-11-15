from openai import OpenAI

from model.cricket_model import (CricketResponse,CricketRequest)
from prompt.cricket_prompt import (HUMAN_PROMPT,SYSTEM_PROMPT)
from logger import logger

from config.setting import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT
)

llm = OpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1"
)


def analyse_cricket_request(request : CricketRequest) -> CricketResponse:

  logger.info("Hit LLM")

  user_prompt = HUMAN_PROMPT.format(
    user_name=request.user_name,
    knowledge_level=request.knowledge_level,
    question=request.question
  )

  responses = llm.responses.parse(
    model=AZURE_OPENAI_DEPLOYMENT,
    instructions=SYSTEM_PROMPT,
    input=user_prompt,
    text_format= CricketResponse
  )
  result = responses.output_parsed
  logger.info("Successfully return the Output")

  return result