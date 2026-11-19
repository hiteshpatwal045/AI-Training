from model.order_model import OrderRequest
from service.order_service import menu, orders


def calculate_invoice(request: OrderRequest):
  line_items = []
  subtotal = 0

  for item in request.items:
    amount = menu[item.food_name] * item.quantity
    subtotal += amount
    line_items.append({
      "food_name": item.food_name,
      "quantity": item.quantity,
      "amount": float(amount)
    })

  gst = round(subtotal * 0.05, 2)
  total_payable = round(subtotal + gst, 2)
  invoice_id = f"INV{1000 + len(orders) + 1}"

  return {
    "invoice_id": invoice_id,
    "line_items": line_items,
    "subtotal": float(subtotal),
    "gst": gst,
    "total_payable": total_payable
  }