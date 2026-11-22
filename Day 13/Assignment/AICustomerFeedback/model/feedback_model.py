from typing import Literal
from pydantic import BaseModel, Field


class FeedbackRequest(BaseModel):
    customer_id: str = Field(min_length=1)
    order_id: str = Field(min_length=1)
    rating: int = Field(ge=1, le=5)          # rating = 6 -> HTTP 422
    feedback: str = Field(min_length=1)


# What the LLM must return (structured output)
class FeedbackAnalysis(BaseModel):
    sentiment: Literal["Positive", "Neutral", "Negative"]
    issue_category: Literal["Product", "Delivery", "Support", "Billing", "Other"]
    priority: Literal["High", "Normal", "Low"]
    reply: str


# What the API returns
class FeedbackResponse(BaseModel):
    customer_id: str
    sentiment: Literal["Positive", "Neutral", "Negative"]
    issue_category: Literal["Product", "Delivery", "Support", "Billing", "Other"]
    priority: Literal["High", "Normal", "Low"]
    reply: str
    status: Literal["Processed"]