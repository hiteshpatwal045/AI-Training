from pydantic import BaseModel

class RequestStudent(BaseModel):
  student_name : str
  course_name : str
  assignment_title : str
  assignment_description : str
  evaluation_criteria : list[str]

class ResponseStudent(BaseModel):
  student_name : str
  overall_assessment : str
  demonstrated_skills : list[str];
  gaps_or_missing_evidence : list[str]
  improvement_suggestions : list[str]
  next_practice_tasks : list[str]
  feedback_summary : str