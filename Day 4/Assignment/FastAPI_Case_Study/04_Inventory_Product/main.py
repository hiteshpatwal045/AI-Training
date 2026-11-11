from fastapi import FastAPI
from sqlalchemy.orm import Session


from logger import logger
from config.database import get_db
from 
from schema.inventory_products_schema import (
  AddProduct,
  UpdateProduct,
  StockDecrease,
  StockIncrease,
  InventoryValue,
  InventoryProduct
)



Base.metadata.create_all(bind=engine)
app = FastAPI()