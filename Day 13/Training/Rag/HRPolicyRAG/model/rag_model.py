from pydantic import BaseModel, Field


class RAGRequest(BaseModel):
    question: str = Field(min_length=3)


class RAGResponse(BaseModel):
    question: str
    answer: str
    sources: list[str]
