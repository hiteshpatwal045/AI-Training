from fastapi import HTTPException
from datetime import datetime
import json

with open("config/menu.json") as file:
  menu = json.load(file)

from model.order_model import OrderRequest

orders = {}


def create_order(request : OrderRequest, invoice : dict):
  order_id = f"ORD{1001 + len(orders)}"

  order = {
    "order_id": order_id,
    "employee_id": request.employee_id,
    "employee_name": request.employee_name,
    "items": [item.model_dump() for item in request.items],
    "invoice": invoice,
    "status": "Order Placed",
    "created_at": datetime.now()
  }

  orders[order_id] = order
  return order


def validate_order(request: OrderRequest):

  for item in request.items:
    if item.food_name not in menu:
      raise HTTPException(
        status_code=400,
        detail=f"{item.food_name} is not available in the menu"
      )

def get_order(id : str):
  if id not in orders:
    raise HTTPException(
      status_code=404,
      detail=f"Order {id} not found"
    )

  return orders[id]


def get_elapsed_minutes(order_id: str, simulated: int | None = None):
  if simulated is not None:
    return simulated

  order = get_order(order_id)
  seconds = (datetime.now() - order["created_at"]).total_seconds()
  return int(seconds // 60)