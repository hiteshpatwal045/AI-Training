from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from model.order_model import OrderRequest, OrderItem
from service.order_service import (
  validate_order,
  create_order,
  get_order,
  get_elapsed_minutes
)
from service.invoice_service import calculate_invoice
from service.escalation_service import generate_escalation_message

EXPECTED_MINUTES = 20

class CafeteriaState(TypedDict, total=False):
  employee_id: str
  employee_name: str
  items: list[OrderItem]
  simulated: int | None

  order_id: str
  invoice: dict
  status: str

  elapsed_minutes: int
  delay_minutes: int
  priority: str
  escalated_to: str | None
  message: str


# Node 1: validate_order
def validate_order_node(state: CafeteriaState):
  request = OrderRequest(
    employee_id=state["employee_id"],
    employee_name=state["employee_name"],
    items=state["items"]
  )
  validate_order(request)
  return {}


# Node 2: generate_invoice
def generate_invoice_node(state: CafeteriaState):
  request = OrderRequest(
    employee_id=state["employee_id"],
    employee_name=state["employee_name"],
    items=state["items"]
  )
  invoice = calculate_invoice(request)
  order = create_order(request, invoice)
  return {
    "order_id": order["order_id"],
    "invoice": invoice,
    "status": order["status"]
  }


# Node 3: check_delivery
def check_delivery_node(state: CafeteriaState):
  get_order(state["order_id"])
  elapsed = get_elapsed_minutes(state["order_id"], state.get("simulated"))
  delay = max(elapsed - EXPECTED_MINUTES, 0)
  return {
    "elapsed_minutes": elapsed,
    "delay_minutes": delay
  }


# Node 4: escalate_order
def escalate_order_node(state: CafeteriaState):
  order = get_order(state["order_id"])

  if state["elapsed_minutes"] <= 30:
    priority, recipient = "HIGH", "Cafeteria Supervisor"
  else:
    priority, recipient = "CRITICAL", "Cafeteria Manager"

  result = generate_escalation_message(order,
    state["elapsed_minutes"],
    state["delay_minutes"],
    priority,
    recipient
  )
  return {
    "priority": priority,
    "escalated_to": recipient,
    "message": result.message,
    "status": "Escalated"
  }


# Node 5: confirm_order
def confirm_order_node(state: CafeteriaState):
  return {
    "priority": "NORMAL",
    "escalated_to": None,
    "message": "Your order is on track and will be delivered within 20 minutes.",
    "status": "Order Confirmed"
  }


# condition functions
def route_start(state: CafeteriaState):
  if state.get("order_id"):
    return "Check Delivery"
  return "Validate Order"


def route_after_delivery(state: CafeteriaState):
  if state["delay_minutes"] > 0:
    return "Escalate Order"
  return "Confirm Order"


# Create Workflow
workflow = StateGraph(CafeteriaState)

# Add Nodes
workflow.add_node("validate_order_node", validate_order_node)
workflow.add_node("generate_invoice_node", generate_invoice_node)
workflow.add_node("check_delivery_node", check_delivery_node)
workflow.add_node("escalate_order_node", escalate_order_node)
workflow.add_node("confirm_order_node", confirm_order_node)

# Starting Edge (new order or existing order)
workflow.add_conditional_edges(
  START,
  route_start,
  {
    "Validate Order": "validate_order_node",
    "Check Delivery": "check_delivery_node"
  }
)

workflow.add_edge("validate_order_node", "generate_invoice_node")
workflow.add_edge("generate_invoice_node", "check_delivery_node")

# Conditional edge after check_delivery
workflow.add_conditional_edges(
  "check_delivery_node",
  route_after_delivery,
  {
    "Escalate Order": "escalate_order_node",
    "Confirm Order": "confirm_order_node"
  }
)

workflow.add_edge("escalate_order_node", END)
workflow.add_edge("confirm_order_node", END)

workflow_graph = workflow.compile()