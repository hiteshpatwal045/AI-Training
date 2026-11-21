from crewai import Task

from agent.activity_planner_agent import (
    activity_planner
)


def create_activity_task(idea_task):

    activity_task = Task(

        description=(

            "Create four activities based on the "
            "event theme suggested previously. "
            "The activities should be suitable for "
            "students and should encourage participation."

        ),

        expected_output=(

            "Four event activities with short descriptions."

        ),

        agent=activity_planner,

        context=[idea_task]

    )

    return activity_task
