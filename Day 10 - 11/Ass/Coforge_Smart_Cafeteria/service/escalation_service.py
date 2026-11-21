import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from model.order_model import EscalationResponse
from prompt.escalation_prompt import SYSTEM_PROMPT, HUMAN_PROMPT

load_dotenv()

llm = AzureChatOpenAI(
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),
  azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
  api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
  azure_endpoint=os.getenv("AZURE_API_ENDPOINT")
)

structured_llm = llm.with_structured_output(EscalationResponse)

prompt = ChatPromptTemplate.from_messages(
  [
    ("system", SYSTEM_PROMPT),
    ("human", HUMAN_PROMPT),
  ])

chain = prompt | structured_llm


def generate_escalation_message(order: dict, elapsed_minutes: int, delay_minutes: int, priority: str, recipient: str):

  items = ""
  for item in order["items"]:
    food_name = item["food_name"]
    quantity = item["quantity"]

    items += f"{food_name} x{quantity}, "

  items = items.rstrip(", ")


  result = chain.invoke({
    "order_id": order["order_id"],
    "employee_id": order["employee_id"],
    "employee_name": order["employee_name"],
    "items": items,
    "elapsed_minutes": elapsed_minutes,
    "delay_minutes": delay_minutes,
    "priority": priority,
    "recipient": recipient
  })

  return result