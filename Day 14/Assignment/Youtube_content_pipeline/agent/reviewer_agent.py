from crewai import Agent
from config.settings import llm
from tool.tools import keyword_tool

reviewer_agent = Agent(
    role="Content Quality Reviewer",
    goal="Check accuracy, clarity, completeness, originality and SEO quality",
    backstory="You are a strict editor who scores content honestly from 1 to 10.",
    tools=[keyword_tool],
    llm=llm,
    verbose=True,
    allow_delegation=True
)