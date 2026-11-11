from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session

from logger import logger
from config.database import engine, Base, get_db
from model.inventory_products_model import InventoryProductDB
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
def add_product(data : AddProduct, db : Session = Depends(get_db)):
  return service.add_product(db, data)


# 2. List all products with pagination
@app.get("/products", response_model=ProductPage)
def list_products(
  page : int = Query(1, ge=1),
  page_size : int = Query(10, ge=1, le=100),
  db : Session = Depends(get_db)
):
  return service.list_products(db, page, page_size)


# 3. Retrieve a product by ID
@app.get("/products/{id}", response_model=InventoryProduct)
def get_product(id : int, db : Session = Depends(get_db)):
  return service.get_product_by_id(db, id)


# 4. Update product information and pricing
@app.put("/products/{id}", response_model=InventoryProduct)
def update_product(id : int, data : UpdateProduct, db : Session = Depends(get_db)):
  return service.update_product(db, id, data)


# 5. Delete a product
@app.delete("/products/{id}")
def delete_product(id : int, db : Session = Depends(get_db)):
  return service.delete_product(db, id)
