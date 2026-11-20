from crewai import Agent
from config.settings import llm

writer_tutor = Agent(
    role="Professinal Content Writer",
    goal="Create Professinal article useing research finding",
    backstory=(
        "You are an experienced technical content writer "
        "Make content suitable for beginner too."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)
