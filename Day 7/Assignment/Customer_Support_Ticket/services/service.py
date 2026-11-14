from openai import OpenAI
from prompts.prompt import SYSTEM_PROMPT, HUMAN_PROMPT
from models.tickets import TicketRequest, TicketResponse
from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)

# Create LLM client outside the function
llm = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1"
)


def triage_ticket(ticket: TicketRequest) -> TicketResponse:
    
    user_prompt = HUMAN_PROMPT.format(
        ticket_id=ticket.ticket_id,
        employee_name=ticket.employee_name,
        department=ticket.department,
        issue_description=ticket.issue_description
    )

    response = llm.responses.parse(
        model=AZURE_OPENAI_DEPLOYMENT,
        instructions=SYSTEM_PROMPT,
        input=user_prompt,
        text_format=TicketResponse
    )

    return response.output_parsed