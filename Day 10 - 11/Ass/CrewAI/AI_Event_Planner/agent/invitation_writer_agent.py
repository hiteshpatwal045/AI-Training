from crewai import Agent

from config.settings import llm


invitation_writer = Agent(

    role="Invitation Writer",

    goal=(
        "Write short and friendly event "
        "invitations for participants."
    ),

    backstory=(
        "You are a communication specialist "
        "who creates attractive invitation "
        "messages for events and programs."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False

)
