from crewai import Task
from agent.quiz_creator_agent import quiz_creator


def create_quiz_task(study_plan_task):

    quiz_task = Task(

        description=(
            "Use the study plan from the previous task. "
            "Create five beginner-friendly practice questions. "
            "The questions should test conceptual understanding "
            "and basic coding knowledge. "
            "Do not provide answers."
        ),

        expected_output=(
            "Five beginner-level practice questions "
            "without solutions."
        ),

        agent=quiz_creator,

        context=[study_plan_task]
    )

    return quiz_task
