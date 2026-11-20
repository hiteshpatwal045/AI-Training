from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from model.models import (AstronautRequest,AstronautResponse)
from service.serivces import analyze
class AstState(TypedDict):
  ast_id : int
  ast_name : str
  age : int
  training_hours : int
  medical_clearance : bool
  previous_missions : int


  ast_id : int
  ast_name : str
  mission_status : str
  assigned_mission : str
  reason : str


def analyze_data(request : AstronautRequest):
  result = AstronautResponse(
    ast_id=request.ast_id,
    ast_name=request.ast_id,
    age=request.age,
    training_hours= request.training_hours,
    medical_clearanc=request.medical_clearance,
    previous_missions=request.previous_missions
  )

  analysis = analyze(result)

  return {
      "ast_id" : analysis.ast_id,
      "ast_name" : analysis.ast_name,
      "mission_status" : analysis.mission_status,
      "assigned_mission" : analysis.assigned_mission,
      "reason" : analysis.reason
  }

workflow = StateGraph(AstState)

workflow.add_node("llm",analyze_data)

workflow.add_edge(START,"llm")
workflow.add_edge("llm",END)

workflow_graph = workflow.compile()