from crewai import Crew, Process

from agent.topic_explainer_agent import topic_explainer
from agent.study_planner_agent import study_planner
from agent.quiz_creator_agent import quiz_creator

from task.explanation_task import create_explanation_task
from task.study_plan_task import create_study_plan_task
from task.quiz_task import create_quiz_task


def main():

    print("================================")
    print("      AI STUDY PLANNER")
    print("         CrewAI")
    print("================================")

    topic = input(
        "Enter Python topic: "
    ).strip()

    if not topic:

        print(
            "Please enter a valid topic."
        )

        return

    # Step 1. Create Explanation Task

    explanation_task = (
        create_explanation_task(topic)
    )

    # Step 2. Create Study Plan Task

    study_plan_task = (
        create_study_plan_task(
            explanation_task
        )
    )

    # Step 3. Create Quiz Task

    quiz_task = (
        create_quiz_task(
            study_plan_task
        )
    )

    # Step 4. Create Crew

    study_crew = Crew(

        agents=[
            topic_explainer,
            study_planner,
            quiz_creator
        ],

        tasks=[
            explanation_task,
            study_plan_task,
            quiz_task
        ],

        process=Process.sequential,

        verbose=True

    )

    # Step 5. Execute Crew

    try:

        result = study_crew.kickoff()

        print("\n")
        print("*" * 50)
        print("        AI STUDY PLANNER REPORT")
        print("*" * 50)

        print("\nSECTION 1 : TOPIC OVERVIEW\n")
        print(explanation_task.output.raw)

        print("\nSECTION 2 : 3-DAY STUDY ROADMAP\n")
        print(study_plan_task.output.raw)

        print("\nSECTION 3 : SELF-ASSESSMENT QUIZ\n")
        print(quiz_task.output.raw)

        print("\n" + "*" * 50)
        print("         END OF STUDY REPORT")
        print("*" * 50)

    except Exception as error:

        print(
            "Unable to generate study plan:",
            type(error).__name__,
            error
        )


if __name__ == "__main__":
    main()