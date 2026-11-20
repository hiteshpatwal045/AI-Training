from crewai import Agent
from config.settings import llm

editor_tutor = Agent(
    role="Cotent Quality Editor",
    goal="Review the quality of the given aritcle",
    backstory=(
        "You are an professional editor "
        "check the mistakes in grammer "
        "dont change the actual meaning of the content provide to you "
        "most appropiate definition should be given"
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)
