import os
from dotenv import load_dotenv
from crewai import LLM
load_dotenv()

AZURE_DEPLOYMENT = os.getenv("OPENAI_MODEL_NAME")
AZURE_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_ENDPOINT = os.getenv("OPENAI_ENDPOINT")
AZURE_API_VERSION = os.getenv("OPENAI_API_VERSION")


if not all([
    AZURE_API_KEY,
    AZURE_API_VERSION,
    AZURE_DEPLOYMENT,
    AZURE_ENDPOINT
]):
    raise ValueError("Azure OpenAI configuration is missing")

# configure azure openai environment variables
os.environ["OPENAI_ENDPOINT"] = AZURE_ENDPOINT
os.environ["OPENAI_API_KEY"] = AZURE_API_KEY
os.environ["OPENAI_API_VERSION"] = AZURE_API_VERSION

# create crewai llm
llm = LLM(
    model=f"azure/{AZURE_DEPLOYMENT}",
    endpoint=AZURE_ENDPOINT,
    api_key=AZURE_API_KEY,
    api_version=AZURE_API_VERSION
)
