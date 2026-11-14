from openai import OpenAI
from config.settings import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT
)
from model.student_model import(
  RequestStudent,
  ResponseStudent
)
from prompt.llm_prompt import (
  HUMAN_PROMPT,
  SYSTEM_PROMPT
)


llm = OpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1"
)

def student_evaluation(request : RequestStudent) -> RequestStudent:

  print("DEPLOYMENT:", repr(AZURE_OPENAI_DEPLOYMENT))
  print("ENDPOINT:", repr(AZURE_OPENAI_ENDPOINT))
  user_prompt = HUMAN_PROMPT.format(
    student_name=request.student_name,
    course_name=request.course_name,
    assignment_title=request.assignment_title,
    assignment_description=request.assignment_description,
    evaluation_criteria=request.evaluation_criteria
  )

  response = llm.responses.parse(
    model=AZURE_OPENAI_DEPLOYMENT,
    instructions=SYSTEM_PROMPT,
    input=user_prompt,
    text_format=ResponseStudent
  )

  return response.output_parsed