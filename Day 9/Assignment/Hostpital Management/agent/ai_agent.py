from langchain.agents import create_agent
from langchain_openai import AzureChatOpenAI

from config.settings import (
    AZURE_API_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT
)
from prompt.hospital_prompt import SYSTEM_PROMPT
from tool.hospital_tool import (
    calculate_hospital_bill,
    check_doctor_availability,
    register_patient,
    get_patient_medical_records,
    book_appointment
)


def create_hospital_agent():

    # connet to azure openai
    llm = AzureChatOpenAI(
        azure_endpoint=AZURE_API_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        azure_deployment=AZURE_OPENAI_DEPLOYMENT,
        api_version=AZURE_OPENAI_API_VERSION
    )

    # register 4 tools
    tools = [
        calculate_hospital_bill,
        check_doctor_availability,
        register_patient,
        get_patient_medical_records,
        book_appointment
    ]

    # create ai agents
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT
    )

    return agent
