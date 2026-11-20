from crewai import Agent
from config.settings import llm

researcher_agent = Agent(
    role="AI Research Specialist",
    goal="research the given topic and identify the useful information",
    backstory=(
        "You are an experienced researcher."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)
