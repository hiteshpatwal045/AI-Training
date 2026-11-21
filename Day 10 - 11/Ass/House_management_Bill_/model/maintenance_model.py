from pydantic import BaseModel


# What the user sends
class QuestionRequest(BaseModel):
  question: str


# What the API returns
class AnswerResponse(BaseModel):
  question: str
  answer: str