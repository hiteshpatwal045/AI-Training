from crewai import Task

from agent.quality_checker_agent import (
    quality_checker
)


def create_quality_check_task(
    invitation_task
):

    quality_check_task = Task(

        description=(

            "Review the complete event plan. "
            "Check whether the following details "
            "are available: Event Theme, Activities, "
            "Event Date, Invitation, Venue. "
            "If any detail is missing, mention it clearly."

        ),

        expected_output=(

            "A checklist showing available and missing details."

        ),

        agent=quality_checker,

        context=[invitation_task]

    )

    return quality_check_task
