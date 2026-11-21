from crewai import Agent
from config.settings import llm

quiz_creator = Agent(
    role="Quiz Creator",

    goal=(
        "Create beginner-level quizzes that help "
        "students assess their understanding."
    ),

    backstory=(
        "You are an assessment specialist who creates "
        "simple practice questions designed to reinforce "
        "learning and improve retention."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False
)
