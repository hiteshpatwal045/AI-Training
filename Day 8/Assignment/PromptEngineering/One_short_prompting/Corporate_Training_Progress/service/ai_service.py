from model.analysis import LearnerProgressAnalysis
from model.request_model import LearnerProgressRequest
from model.response import LearnerProgressResponse
from config.setting import (
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_API_VERSION,
  AZURE_OPENAI_DEPLOYMENT,
  AZURE_OPENAI_ENDPOINT
)
from prompt.one_shot_prompt import SYSTEM_PROMPT, HUMAN_PROPMT
from openai import AzureOpenAI
import json


llm = AzureOpenAI(
  api_key=AZURE_OPENAI_API_KEY,
  azure_endpoint=AZURE_OPENAI_ENDPOINT,
  azure_deployment=AZURE_OPENAI_DEPLOYMENT,
  api_version=AZURE_OPENAI_API_VERSION
)


def llm_reponse(request: LearnerProgressRequest) -> LearnerProgressResponse:

  user_prompt = HUMAN_PROPMT.format(
    learner_id=request.learner_id,
    learner_name=request.learner_name,
    training_program=request.training_program,
    topics_completed=request.topics_completed,
    assignments_assigned=request.assignments_assigned,
    assignments_completed=request.assignments_completed,
    attendance_percentage=request.attendance_percentage,
    coding_assessment_score=request.coding_assessment_score,
    trainer_feedback=request.trainer_feedback
  )

  response = llm.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT,
    messages=[
      {
        "role": "system",
        "content": SYSTEM_PROMPT
      },
      {
        "role": "user",
        "content": user_prompt
      }
    ],
    response_format={"type": "json_object"}
  )

  ai_text = response.choices[0].message.content

  if not ai_text:
    raise ValueError("Empty Response")

  data = json.loads(ai_text)


  analysis = LearnerProgressAnalysis(
    completion_percentage=data["completion_percentage"],
    learning_level=data["learning_level"],
    strong_topics=data["strong_topics"],
    weak_topics=data["weak_topics"],
    readiness_score=data["readiness_score"],
    improvement_priority=data["improvement_priority"]
  )

  return LearnerProgressResponse(
    learner_id=request.learner_id,
    learner_name=request.learner_name,
    analysis=analysis,
    recommended_practice=data["recommended_practice"],
    next_learning_plan=data["next_learning_plan"],
    trainer_recommendation=data["trainer_recommendation"],
    ai_summary=data["ai_summary"]
  )