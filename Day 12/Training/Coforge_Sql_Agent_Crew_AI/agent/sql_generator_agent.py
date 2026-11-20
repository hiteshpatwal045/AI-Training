from crewai import Agent
from config.settings import llm

from tool.sql_tools import execute_employee_sql


sql_generator = Agent(
    role="SQL Generator",
    goal="Convert natural language into MySQL SELECT queries",
    backstory=(
        "You are a sql developer who creates "
        "simple employee analytics queries."
    ),
    tools=[execute_employee_sql],
    llm=llm,
    verbose=True,
    allow_delegation=False
)
