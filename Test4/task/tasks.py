from crewai import Task
from agents.agent1 import get_agent1
from agents.agent2 import get_agent2
from agents.agent3 import get_agent3


def create_task(topic, service, record):

    task1 = Task(
        description=(
            f"Go through and analyse the given '{topic}'"
        ),
        expected_output=(
            "Topic could be category and severity (LOW, MEDIUM, HIGH or CRITICAL)."
        ),
        agent=get_agent1
    )

    task2 = Task(
        description=(
            "Analyze the possible root casue what ever is given and extract how "
        ),
        expected_output=(
            f"if '{service}' = True and '{record}' is greater and equal than 100 than Critical"
            "and else Non Critical"
            f"if service Reachable is '{service}' is Yes and affected rows '{record}' are lower than 100 "
            "recommended resolution steps and estimated recovery time"
        ),
        agent=get_agent2,
        context=[task1]
    )

    task3 = Task(
        description=(
            f"Go through and analyse the given: '{topic}'"
        ),
        expected_output=(
            f"if '{service}' = True and '{record}' is greater and equal than 100 than Critical"
            "and else Non Critical "
            "if escalation is critical escalation required "
            "if not escalation than no escalation "
        ),
        agent=get_agent3,
        context=[task2]
    )

    return [task1, task2, task3]
