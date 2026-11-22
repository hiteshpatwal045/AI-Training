import logging

from fastapi import FastAPI, HTTPException

from model.feedback_model import FeedbackRequest, FeedbackResponse
from workflow.feedback_workflow import workflow_graph


app = FastAPI(
    title="AI Customer Feedback Analyzer",
    version="1.0",
)


@app.get("/")
def home():
    return {"message": "AI Customer Feedback Analyzer"}


@app.post("/api/v1/feedback", response_model=FeedbackResponse)
def analyze(data: FeedbackRequest):
    result = workflow_graph.invoke({
        "customer_id": data.customer_id,
        "order_id": data.order_id,
        "rating": data.rating,
        "feedback": data.feedback,
    })

    return FeedbackResponse(
        customer_id=result["customer_id"],
        sentiment=result["sentiment"],
        issue_category=result["issue_category"],
        priority=result["priority"],
        reply=result["reply"],
        status=result["status"],
    )