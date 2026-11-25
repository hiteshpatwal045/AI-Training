from crewai import Agent
from config.settings import llm


get_agent2 = Agent(
    role="Your role is a Resolution Agent",
    goal="Possible root cause, recommended resolution steps and estimated recovery time (labelled as an estimate)",
    backstory=(
        "You are an experienced Resolution Agent with 20 Years of experience. "
        "check the grammer mistakes."
    ),
    llm=llm,
    verbose=True,
    allow_delegations=False
)
