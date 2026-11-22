import os
from crewai import Crew, Process

from config.settings import llm
from model.models import YouTubeContentRequest
from task.task import create_tasks
from agent.researcher_agent import researcher_agent
from agent.writer_agent import writer_agent
from agent.seo_agent import seo_agent
from agent.reviewer_agent import reviewer_agent

os.makedirs("output", exist_ok=True)

req = YouTubeContentRequest(
    topic=input("Topic: "),
    target_audience=input("Target audience: "),
    video_duration=int(input("Duration (minutes): ")),
    language=input("Language: "),
    content_style=input("Style: ")
)

mode = input("Process - 1 Sequential, 2 Hierarchical: ")
hierarchical = mode == "2"
feedback = ""

while True:
    tasks = create_tasks(req, hierarchical, feedback)

    crew = Crew(
        agents=[researcher_agent, writer_agent, seo_agent, reviewer_agent],
        tasks=tasks,
        process=Process.hierarchical if hierarchical else Process.sequential,
        manager_llm=llm if hierarchical else None,
        memory=False,      # set True for optional memory
        verbose=True
    )
    crew.kickoff()

    research, script, seo_task, review_task = tasks
    seo = seo_task.output.pydantic
    review = review_task.output.pydantic

    print("\nTitle:", seo.video_title)
    print("Quality score:", review.quality_score)
    print("Feedback:", review.feedback)

    choice = input("\n1 Approve / 2 Request Changes / 3 Reject: ")
    if choice == "2":
        feedback = input("Your feedback: ")
        continue
    break

approval = {"1": "Approved", "2": "Request Changes", "3": "Rejected"}.get(choice, "Rejected")
status = "Ready" if choice == "1" else "Not Ready"

open("output/research.md", "w", encoding="utf-8").write(research.output.raw)
open("output/video_script.md", "w", encoding="utf-8").write(script.output.raw)
open("output/seo_content.json", "w", encoding="utf-8").write(seo.model_dump_json(indent=2))

final = {
    "video_topic": req.topic,
    "video_title": seo.video_title,
    "video_description": seo.video_description,
    "video_script": script.output.raw,
    "seo_keywords": seo.seo_keywords,
    "hashtags": seo.hashtags,
    "thumbnail_text": seo.thumbnail_text,
    "quality_score": review.quality_score,
    "human_approval": approval,
    "publishing_status": status
}

import json
json.dump(final, open("output/final_content.json", "w", encoding="utf-8"), indent=2)
print("\nFinal package saved to output/final_content.json")