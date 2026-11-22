from crewai import Agent
from config.settings import llm
from tool.tools import research_tool

writer_agent = Agent(
    role="YouTube Script Writer",
    goal="Write an engaging video script using the research",
    backstory="You are a top educational YouTuber who writes strong hooks, simple examples and clear conclusions.",
    tools=[research_tool],
    llm=llm,
    verbose=True,
    allow_delegation=True
)