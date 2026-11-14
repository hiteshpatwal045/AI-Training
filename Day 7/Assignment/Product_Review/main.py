from fastapi import FastAPI

from model.emp_models import (
  ProductRequest,
  ProductResponse
)
from service.emp_service import create_product_review

app = FastAPI(
  title = "Product Review API",
  version = "1.0"
)


@app.get("/")
def home():
  return {
    "message" : "Product Review API endpoints"
  }

@app.post("/api/v1/analyze-product-review", response_model=ProductResponse)
def product_review(product : ProductRequest):
  return create_product_review(product)