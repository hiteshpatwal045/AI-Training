from crewai import Agent
from config.settings import llm


get_agent1 = Agent(
    role="You are an Incident Analysis Agent ",
    goal="your task is to analyse Incident summary, category and.",
    backstory=(
        "You are an experienced Incident Agent with 20 Years of experience. "
        "Do check the grammer mistakes. "
    ),
    llm=llm,
    verbose=True,
    allow_delegations=False
)
