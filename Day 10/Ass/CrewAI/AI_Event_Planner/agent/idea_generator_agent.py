from crewai import Agent

from config.settings import llm


idea_generator = Agent(

    role="Event Idea Generator",

    goal=(
        "Generate a suitable event theme based on "
        "the event details provided."
    ),

    backstory=(
        "You are a creative event consultant who "
        "specializes in designing engaging themes "
        "for student events and college activities."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False

)
