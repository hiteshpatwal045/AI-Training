from langchain_openai import AzureChatOpenAI

from config.settings import (
    AZURE_API_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT
)

def create_llm():

    llm = AzureChatOpenAI(
        azure_endpoint=AZURE_API_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_deployment=AZURE_OPENAI_DEPLOYMENT
    )
    return llm


