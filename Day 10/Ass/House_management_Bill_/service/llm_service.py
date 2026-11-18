from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
)
from prompt.maintenance_prompt import SYSTEM_PROMPT, HUMAN_PROMPT

llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT
)

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("user", HUMAN_PROMPT),
])

chain = prompt | llm

def answer_question(question: str) -> str:
    result = chain.invoke({"question": question})
    return result.content.strip()