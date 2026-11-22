from crewai import Agent
from config.settings import llm
from tool.tools import keyword_tool

seo_agent = Agent(
    role="YouTube SEO Specialist",
    goal="Create title, description, keywords, hashtags and thumbnail text",
    backstory="You are a YouTube growth expert who writes titles under 60 characters with the main keyword first.",
    tools=[keyword_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)