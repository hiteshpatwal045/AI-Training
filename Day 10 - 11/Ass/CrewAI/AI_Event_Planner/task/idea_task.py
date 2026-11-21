from crewai import Task

from agent.idea_generator_agent import (
    idea_generator
)


def create_idea_task(
    event_name,
    event_date,
    audience
):

    idea_task = Task(

        description=(

            f"Event Name: {event_name}. "

            f"Event Date: {event_date}. "

            f"Target Audience: {audience}. "

            "Suggest one suitable event theme. "

            "Keep the theme simple, engaging, "

            "and suitable for students."

        ),

        expected_output=(

            "One event theme with a short explanation."

        ),

        agent=idea_generator

    )

    return idea_task
