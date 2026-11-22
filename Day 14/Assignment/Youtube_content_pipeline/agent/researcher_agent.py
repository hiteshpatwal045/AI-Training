from crewai import Agent
from config.settings import llm
from tool.tools import research_tool

researcher_agent = Agent(
    role="YouTube Research Specialist",
    goal="Research the video topic and prepare a clear content outline",
    backstory="You are an experienced researcher who prepares accurate research for educational tech videos.",
    tools=[research_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)