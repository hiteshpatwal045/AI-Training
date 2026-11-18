from crewai import Crew, Process

from agent.tutor_agent import python_tutor
from task.tutor_task import create_tutor_task   


def main():

    print("================================")
    print("          AI PYTHON TUTOR       ")
    print("         Powered by CrewAI      ")
    print("================================")

    topic = input(
        "Enter Python topic "
    ).strip()

    if not topic:
        print("Please enter a vlid topic.")
        return

    # Step 1. Create the task
    tutor_task = create_tutor_task(topic)

    # Step 2. Create the crew
    python_crew = Crew(
        agents=[python_tutor],
        tasks=[tutor_task],
        process=Process.sequential,
        verbose=True
    )

    # step 3. Execute the crew
    try:
        result = python_crew.kickoff()

        print("\n==========AI Response=========\n")
        print(result.raw)
    except Exception as error:
        print(
            "unable to generate the lesson:",
            type(error).__name__
        )


if __name__ == "__main__":
    main()
