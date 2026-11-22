import os
from dotenv import load_dotenv
from crewai import LLM
load_dotenv()

AZURE_DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT")
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")

if not all([AZURE_API_KEY, AZURE_API_VERSION, AZURE_DEPLOYMENT, AZURE_ENDPOINT]):
    raise ValueError("Azure OpenAI configuration is missing")

os.environ["OPENAI_ENDPOINT"] = AZURE_ENDPOINT
os.environ["OPENAI_API_KEY"] = AZURE_API_KEY
os.environ["OPENAI_API_VERSION"] = AZURE_API_VERSION

llm = LLM(
    model=f"azure/{AZURE_DEPLOYMENT}",
    endpoint=AZURE_ENDPOINT,
    api_key=AZURE_API_KEY,
    api_version=AZURE_API_VERSION
)