from pydantic import BaseModel, Field


class AstronautRequest(BaseModel):
  ast_id : int
  ast_name : str
  age : int
  training_hours : int
  medical_clearance : bool
  previous_missions : int

class AstronautResponse(BaseModel):
  ast_id : int
  ast_name : str
  mission_status : str
  assigned_mission : str
  reason : str

class AstronautRes(BaseModel):
  mission_status : str