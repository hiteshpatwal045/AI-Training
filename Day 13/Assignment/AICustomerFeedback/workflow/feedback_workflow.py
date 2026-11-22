from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from service.llm_service import analyze_feedback
from model.feedback_model import FeedbackRequest


# creating the state
class FeedbackState(TypedDict):
    customer_id: str
    order_id: str
    rating: int
    feedback: str

    sentiment: str
    issue_category: str
    priority: str
    reply: str
    status: str


def analyze_feedback_node(state: FeedbackState):
    request = FeedbackRequest(
        customer_id=state["customer_id"],
        order_id=state["order_id"],
        rating=state["rating"],
        feedback=state["feedback"],
    )

    result = analyze_feedback(request)

    return {
        "sentiment": result.sentiment,
        "issue_category": result.issue_category,
        "priority": result.priority,
        "reply": result.reply,
    }


def check_priority(state: FeedbackState):
    if state["priority"] == "High":
        return "Escalate"
    return "Standard"


def escalate_node(state: FeedbackState):
    # High priority: make sure the reply mentions the support-review flag
    reply = state["reply"]
    if "flagged" not in reply.lower():
        reply = f"{reply} Your feedback has been flagged for customer support review."
    return {"reply": reply, "status": "Processed"}


def standard_node(state: FeedbackState):
    return {"status": "Processed"}


# create workflow
workflow = StateGraph(FeedbackState)

# add nodes
workflow.add_node("analyze_feedback_node", analyze_feedback_node)
workflow.add_node("escalate_node", escalate_node)
workflow.add_node("standard_node", standard_node)

# edges
workflow.add_edge(START, "analyze_feedback_node")

workflow.add_conditional_edges(
    "analyze_feedback_node",
    check_priority,
    {
        "Escalate": "escalate_node",
        "Standard": "standard_node",
    },
)
workflow.add_edge("escalate_node", END)
workflow.add_edge("standard_node", END)

workflow_graph = workflow.compile()