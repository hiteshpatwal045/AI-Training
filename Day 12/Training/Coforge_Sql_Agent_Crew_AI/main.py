from crewai import Crew, Process

from agent.sql_executor_agent import sql_executor
from agent.sql_validator_validator import sql_validator
from agent.sql_generator_agent import sql_generator

from task.tasks import create_tasks

question = input("Ask your SQL question: ")
tasks = create_tasks(question)

crew = Crew(
    agents=[
        sql_generator,
        sql_validator,
        sql_executor
    ],
    tasks=tasks,
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print("\nFINAL SQL AGENT RESPONSE")
print(result.raw)

