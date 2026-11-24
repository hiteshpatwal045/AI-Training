from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)
from prompt.feedback_prompt import HUMAN_PROMPT, SYSTEM_PROMPT
from model.feedback_model import FeedbackRequest, FeedbackAnalysis

# creating the llm
llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
)

# structured output
structured_llm = llm.with_structured_output(FeedbackAnalysis)

# creating the prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("user", HUMAN_PROMPT),
])

# chain
chain = prompt | structured_llm

def analyze_feedback(request: FeedbackRequest) -> FeedbackAnalysis:
    return chain.invoke({
        "customer_id": request.customer_id,
        "order_id": request.order_id,
        "rating": request.rating,
        "feedback": request.feedback,
    })
