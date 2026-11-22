from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from model.models import CustomerRequest,CustomerResponse, CustomerAnalysis
from prompt.prompts import HUMAN_PROMPT, SYSTEM_PROMPT

from config.settings import(
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_API_VERSION,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT
)

llm = AzureChatOpenAI(
  api_key= AZURE_OPENAI_API_KEY,
  azure_endpoint= AZURE_OPENAI_ENDPOINT,
  api_version= AZURE_OPENAI_API_VERSION,
  azure_deployment= AZURE_OPENAI_DEPLOYMENT
)

structure_llm = llm.with_structured_output(
  CustomerResponse
)

prompt = ChatPromptTemplate.from_messages([
  ("system", SYSTEM_PROMPT),
  ("user", HUMAN_PROMPT)
])


chain = prompt | structure_llm

def analyze_data(request : CustomerRequest) -> CustomerResponse:
  result = chain.invoke({
    "customer_id": request.customer_id,
    "customer_name": request.customer_name,
    "product_name": request.product_name,
    "query": request.query
  })

  analysis = CustomerAnalysis(
    category = result.analysis.category,
    sentiment =result.analysis.sentiment,
    priority = result.analysis.priority,
    summary =result.analysis.summary,
  )

  return CustomerResponse(
    customer_id= request.customer_id,
    customer_name=request.customer_name,
    analysis=analysis,
    reply= result.reply,
    next_action= result.next_action,
    status= "success"
  )