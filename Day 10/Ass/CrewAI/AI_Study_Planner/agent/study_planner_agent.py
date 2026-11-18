from crewai import Agent
from config.settings import llm

study_planner = Agent(
    role="Study Planner",

    goal=(
        "Create structured learning plans that help "
        "beginners learn Python topics step by step."
    ),

    backstory=(
        "You are a learning mentor who designs effective "
        "study schedules. You break learning into manageable "
        "daily activities to help students progress steadily."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False
)
