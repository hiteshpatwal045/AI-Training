from crewai import Crew, Process

from task.task import create_tasks
from agent.researcher_agent import researcher_agent
from agent.writer_agent import writer_tutor
from agent.editor_agent import editor_tutor


topic = input("Enter Topic: ")

tasks = create_tasks(topic)

crew = Crew(
    agents=[researcher_agent, writer_tutor, editor_tutor],
    tasks=tasks,
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print("\n\n===== FINAL ARTICLE =====\n")
print(result)
