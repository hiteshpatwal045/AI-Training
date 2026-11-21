from crewai import Task
from agent.study_planner_agent import study_planner


def create_study_plan_task(explanation_task):

    study_plan_task = Task(

        description=(
            "Use the explanation from the previous task. "
            "Create a 3-day study plan for a beginner. "
            "Include Day 1, Day 2, and Day 3 activities. "
            "Mention learning goals and practice activities."
        ),

        expected_output=(
            "A detailed three-day beginner study plan."
        ),

        agent=study_planner,

        context=[explanation_task]
    )

    return study_plan_task
