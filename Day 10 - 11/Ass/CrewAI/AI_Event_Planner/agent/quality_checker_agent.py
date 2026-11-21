from crewai import Agent

from config.settings import llm


quality_checker = Agent(

    role="Quality Checker",

    goal=(
        "Verify event details and identify "
        "any missing information."
    ),

    backstory=(
        "You are a quality reviewer who checks "
        "whether an event plan contains all "
        "required details before publication."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False

)
