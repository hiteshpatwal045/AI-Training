from langchain.agents import create_agent
from langchain_openai import AzureChatOpenAI

from config.setttings import (
    AZURE_API_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT
)
from prompt.ai_prompt import SALARY_SYSTEM_PROMPT
from tool.ai_tool import (
    calculate_hra,
    calculate_da,
    calculate_basic_salary, 
    calculate_gross_salary
)
def create_salary_agent():

    # step 1. connect to azure openai
    llm = AzureChatOpenAI(
        azure_endpoint=AZURE_API_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        azure_deployment=AZURE_OPENAI_DEPLOYMENT,
        api_version=AZURE_OPENAI_API_VERSION
    )

    # step 2. Register four tools
    salary_tools = [
        calculate_basic_salary,
        calculate_hra,
        calculate_da,
        calculate_gross_salary
    ]

    # step 3. Create AI agent
    agent = create_agent(
        model=llm,
        tools=salary_tools,
        system_prompt=SALARY_SYSTEM_PROMPT
    )

    return agent
