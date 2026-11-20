from fastapi import FastAPI

from model.models import (AstronautRequest,AstronautRes)
from workflow.workflows import workflow_graph

app = FastAPI(
  title="Astranaut Mission",
  version="1.1"
)



@app.get("/")
def home():
  return {
    "message":"Astraunat Mission"
  }

@app.post("/api/v1/analyze",response_model=AstronautRes)
def analyze_data(data : AstronautRequest):
  result = workflow_graph.invok({
    "ast_id" :data.ast_id,
    "ast_name" : data.ast_name,
    "age" : data.age,
    "training_hours" : data.training_hours,
    "medical_clearance" : data.medical_clearance,
    "previous_missions" : data.previous_missions
  })

  return AstronautRes(
    mission_status = result["mission_status"]
  )