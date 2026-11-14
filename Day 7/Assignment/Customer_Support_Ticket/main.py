from fastapi import FastAPI
from services.service import triage_ticket
from models.tickets import TicketRequest, TicketResponse

app = FastAPI(
    title="Ticket Triage AI",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message":"Customer Support Ticket API"
    }


@app.post("/api/v1/triage-ticket", response_model=TicketResponse)
def triage(ticket: TicketRequest):
    return triage_ticket(ticket)