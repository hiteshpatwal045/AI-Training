from crewai import Task
from agent.researcher_agent import researcher_agent
from agent.writer_agent import writer_tutor
from agent.editor_agent import editor_tutor


def create_tasks(topic):

    research_task = Task(
        description=(
            f"Research the topic '{topic}'. "
            "Gather accurate information, key concepts."
        ),
        expected_output=(
            "Detailed research notes about the topic."
        ),
        agent=researcher_agent
    )

    writing_task = Task(
        description=(
            f"Write a professional article on '{topic}'. "
            "The article should be beginner friendly "
            "content should be well structured "
            "Easy to understand."
        ),
        expected_output=(
            "A complete professional article."
        ),
        agent=writer_tutor,
        context=[research_task]
    )

    editing_task = Task(
        description=(
            "Review the article. "
            "Correct grammar and improve readability. "
            "Keep the original meaning unchanged."
        ),
        expected_output=(
            "Final edited article."
        ),
        agent=editor_tutor,
        context=[writing_task]
    )

    return [research_task, writing_task, editing_task]
