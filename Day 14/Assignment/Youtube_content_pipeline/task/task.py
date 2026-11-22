from crewai import Task
from agent.researcher_agent import researcher_agent
from agent.writer_agent import writer_agent
from agent.seo_agent import seo_agent
from agent.reviewer_agent import reviewer_agent
from model.models import SEOContent, QualityReview


def create_tasks(req, hierarchical=False, feedback=""):
    # in hierarchical mode the manager picks the agent, so agent=None
    pick = lambda a: None if hierarchical else a

    research_task = Task(
        description=(
            f"Research '{req.topic}' for {req.target_audience}. "
            f"Video length {req.video_duration} minutes, language {req.language}. "
            "Give key concepts, examples and a section-wise outline."
        ),
        expected_output="Research notes and content outline in markdown.",
        agent=pick(researcher_agent)
    )

    script_task = Task(
        description=(
            f"Write a full YouTube script on '{req.topic}' in {req.language}, "
            f"{req.content_style} style, about {req.video_duration} minutes. "
            "Include hook, introduction, explanations with examples, conclusion. "
            f"{('Apply this feedback: ' + feedback) if feedback else ''}"
        ),
        expected_output="Complete video script in markdown.",
        agent=pick(writer_agent),
        context=[research_task]
    )

    seo_task = Task(
        description=(
            "Create video_title (max 60 chars), video_description, seo_keywords, "
            "hashtags and 3 short thumbnail_text suggestions for the script."
        ),
        expected_output="SEO content.",
        agent=pick(seo_agent),
        context=[script_task],
        output_pydantic=SEOContent
    )

    review_task = Task(
        description="Review the script and SEO content. Give quality_score (1-10) and feedback.",
        expected_output="Quality score and feedback.",
        agent=pick(reviewer_agent),
        context=[script_task, seo_task],
        output_pydantic=QualityReview
    )

    return [research_task, script_task, seo_task, review_task]