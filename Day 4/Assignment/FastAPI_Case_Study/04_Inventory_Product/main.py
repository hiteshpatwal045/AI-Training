from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session

from config.database import engine, Base, get_db
from model.inventory_products_model import InventoryProductDB  # noqa: F401 (registers table)
from schema.inventory_products_schema import (
  AddProduct,
  UpdateProduct,
  InventoryProduct,
  ProductPage
)
from service import inventory_products_service as service

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory and Product Management API")


# 1. Add a product
@app.post("/products", response_model=InventoryProduct)
def add_product(data: AddProduct, db: Session = Depends(get_db)):
  return service.add_product(db, data)


# 2. List all products with pagination
@app.get("/products", response_model=ProductPage)
def list_products(
  page: int = Query(1, ge=1),
  limit: int = Query(10, ge=1, le=100),
  db: Session = Depends(get_db)
):
  return service.list_products(db, page, limit)


# 6. Filter products by category
@app.get("/products/category/{category}", response_model=list[InventoryProduct])
def filter_by_category(category: str, db: Session = Depends(get_db)):
  return service.filter_by_category(db, category)


# 7. Low-stock products (must stay above /products/{id})
@app.get("/products/low-stock", response_model=list[InventoryProduct])
def low_stock(db: Session = Depends(get_db)):
  return service.get_low_stock(db)


# 10. Inventory value (must stay above /products/{id})
@app.get("/products/inventory-value")
def inventory_value(db: Session = Depends(get_db)):
  return service.inventory_value(db)


# 3. Retrieve a product by ID
@app.get("/products/{id}", response_model=InventoryProduct)
def get_product(id: int, db: Session = Depends(get_db)):
  return service.get_product_by_id(db, id)


# 4. Update product information and pricing
@app.put("/products/{id}", response_model=InventoryProduct)
def update_product(id: int, data: UpdateProduct, db: Session = Depends(get_db)):
  return service.update_product(db, id, data)


# 5. Delete a product
@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
  return service.delete_product(db, id)


# 8. Increase stock
@app.patch("/products/{id}/increase-stock", response_model=InventoryProduct)
def increase_stock(
  id: int,
  quantity: int = Query(..., gt=0),
  db: Session = Depends(get_db)
):
  return service.increase_stock(db, id, quantity)


# 9. Decrease stock
@app.patch("/products/{id}/decrease-stock", response_model=InventoryProduct)
def decrease_stock(
  id: int,
  quantity: int = Query(..., gt=0),
  db: Session = Depends(get_db)
):
  return service.decrease_stock(db, id, quantity)