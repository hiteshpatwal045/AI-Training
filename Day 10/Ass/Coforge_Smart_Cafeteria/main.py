from fastapi import FastAPI

from model.order_model import OrderRequest, InvoiceResponse, OrderResponse
from service.order_service import menu, get_order
from graph.cafeteria_graph import workflow_graph, EXPECTED_MINUTES

app = FastAPI(
    title="Coforge Smart Cafeteria AI",
    version="1.0"
)


@app.get("/")
def home():
  return {"Coforge smart cafeteria AI"}



@app.get("/menu")
def get_menu():
  return menu


@app.get("/health")
def health():
  return {"status": "ok"}


@app.post("/order", response_model=InvoiceResponse)
def place_order(request: OrderRequest):
  result = workflow_graph.invoke(request.model_dump())

  return {
    **result["invoice"],
    "order_id": result["order_id"],
    "employee_id": request.employee_id,
    "employee_name": request.employee_name,
    "status": "Order Placed"
  }


@app.get("/order/{order_id}")
def order_details(order_id: str):
  return get_order(order_id)


@app.post("/order/{order_id}/check-delay", response_model=OrderResponse)
def check_delay(order_id: str, elapsed_minutes: int | None = None):
  result = workflow_graph.invoke({
    "order_id": order_id,
    "simulated": elapsed_minutes
  })
  order = get_order(order_id)

  return {
    "order_id": order_id,
    "employee_id": order["employee_id"],
    "employee_name": order["employee_name"],
    "status": result["status"],
    "elapsed_minutes": result["elapsed_minutes"],
    "expected_minutes": EXPECTED_MINUTES,
    "delay_minutes": result["delay_minutes"],
    "priority": result["priority"],
    "escalated_to": result["escalated_to"],
    "message": result["message"]
  }