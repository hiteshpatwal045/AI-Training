from crewai import Task

from agent.invitation_writer_agent import (
    invitation_writer
)


def create_invitation_task(activity_task):

    invitation_task = Task(

        description=(

            "Using the event theme and activities, "
            "write a short and friendly invitation. "
            "Include event name, date, audience, and "
            "mention that the venue is "
            "'To be confirmed'."

        ),

        expected_output=(

            "A professional invitation message."

        ),

        agent=invitation_writer,

        context=[activity_task]

    )

    return invitation_task
