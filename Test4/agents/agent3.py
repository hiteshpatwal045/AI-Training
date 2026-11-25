from crewai import Agent
from config.settings import llm


get_agent3 = Agent(
    role="Your role is a Escalation Agent",
    goal="Escalation report containing incident ID, business impact, severity, recommended action and escalation recipient role.",
    backstory=(
        "if escalation is critical escalation required "
        "if not escalation than no escalation "
    ),
    llm=llm,
    verbose=True,
    allow_delegations=False
)
