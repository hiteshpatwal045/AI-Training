from crewai import Task
from agent.tutor_agent import python_tutor


def create_tutor_task(topic):

    tutor_task = Task(
        description=(
            f"Teach the python topic : {topic}. "
            "The learner is a complete fresher. "
            "Explain the concept in simple English. "
            "Provide one real-world example. "
            "Write two beginner-griendly Python programs. "
            "Show the expected output of each program. "
            "Create three practice assignments. "
            "Do not execute any code."
        ),
        expected_output=(
            "A structured Python lesson containing. "
            "1. Topic introduction "
            "2. Detailed explanation "
            "3. Real-world example "
            "4. Two Python programs "
            "5. Expected outputs "
            "6. Three practice assignments"
        ),

        agent=python_tutor
    )
    return tutor_task
