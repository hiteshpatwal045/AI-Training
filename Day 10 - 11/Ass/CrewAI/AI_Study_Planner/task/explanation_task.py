from crewai import Task
from agent.topic_explainer_agent import topic_explainer


def create_explanation_task(topic):

    explanation_task = Task(

        description=(
            f"Explain the Python topic: {topic}. "
            "Assume the learner is a complete beginner. "
            "Explain the concept in simple English. "
            "Describe its purpose and common use cases. "
            "Provide one short Python example with explanation."
        ),

        expected_output=(
            "A beginner-friendly explanation of the topic "
            "along with one Python example."
        ),

        agent=topic_explainer
    )

    return explanation_task
