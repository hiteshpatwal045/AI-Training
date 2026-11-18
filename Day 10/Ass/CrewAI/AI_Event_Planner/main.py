from crewai import Crew, Process
from agent.idea_generator_agent import idea_generator
from agent.activity_planner_agent import activity_planner
from agent.invitation_writer_agent import invitation_writer
from agent.quality_checker_agent import quality_checker
from task.idea_task import create_idea_task
from task.activity_task import create_activity_task
from task.invitation_task import create_invitation_task
from task.quality_check_task import create_quality_check_task


def main():

    print("================================")
    print(" AI EVENT PLANNER ")
    print(" CrewAI ")
    print("================================")

    event_name = input(
        "Enter Event Name: "
    ).strip()

    event_date = input(
        "Enter Event Date: "
    ).strip()

    audience = input(
        "Enter Target Audience: "
    ).strip()

    if not event_name or not event_date or not audience:

        print(
            "Please enter all required details."
        )

        return

    # Step 1

    idea_task = create_idea_task(
        event_name,
        event_date,
        audience
    )

    # Step 2

    activity_task = create_activity_task(
        idea_task
    )

    # Step 3

    invitation_task = create_invitation_task(
        activity_task
    )

    # Step 4

    quality_check_task = (
        create_quality_check_task(
            invitation_task
        )
    )

    # Step 5

    event_crew = Crew(

        agents=[
            idea_generator,
            activity_planner,
            invitation_writer,
            quality_checker
        ],

        tasks=[
            idea_task,
            activity_task,
            invitation_task,
            quality_check_task
        ],

        process=Process.sequential,

        verbose=True

    )

    try:

        event_crew.kickoff()

        print("\n")
        print("*" * 50)
        print("         AI EVENT PLANNER REPORT")
        print("*" * 50)

        print("\nPART A : EVENT THEME\n")
        print(idea_task.output.raw)

        print("\nPART B : EVENT ACTIVITIES\n")
        print(activity_task.output.raw)

        print("\nPART C : INVITATION MESSAGE\n")
        print(invitation_task.output.raw)

        print("\nPART D : QUALITY CHECKLIST\n")
        print(quality_check_task.output.raw)

        print("\n" + "*" * 50)
        print("          END OF REPORT")
        print("*" * 50)

    except Exception as error:

        print(
            "Unable to generate event plan:",
            type(error).__name__
        )


if __name__ == "__main__":
    main()
