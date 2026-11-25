from crewai import Crew, Process
from agents.agent3 import get_agent3
from agents.agent2 import get_agent2
from agents.agent1 import get_agent1
from task.tasks import create_task

# Accept incident_id, system_name, issue_description, affected_users (non-negative integer) and service_unavailable (boolean). Validate inputs before starting the crew.
topic = input("Issue Descriptionp: ")
service_unavailable = input("serviceUnavailable (Yes or not): ")
record = input("enter records : ")
task = create_task(topic, service_unavailable, record)

crew = Crew(
    agents=[get_agent1, get_agent2, get_agent3],
    tasks=task,
    verbose=True,
    process=Process.sequential
)

result = crew.kickoff()
print(result)
