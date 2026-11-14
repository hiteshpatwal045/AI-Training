import os
from dotenv import load_dotenv

load_dotenv()

AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_API_ENDPOINT = os.getenv("AZURE_API_ENDPOINT")
