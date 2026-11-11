from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from logger import logger
from model.inventory_products_model import InventoryProductDB
from schema.inventory_products_schema import (
  AddProduct,
  UpdateProduct
)


# 1. Add a product.
def add_product(db : Session, data : AddProduct):
  try:
    product = InventoryProductDB(**data.model_dump(exclude_none=True))

    db.add(product)
    db.commit()
    db.refresh(product)

    logger.info(f"Product added successfully with ID: {product.product_id}")

    return product

  except IntegrityError as e:
    db.rollback()
    logger.warning("Duplicate product ID while adding a product")
    raise HTTPException(
      status_code=409,
      detail="Product ID already exists"
    ) from e

  except SQLAlchemyError as e:
    db.rollback()
    logger.exception("DB error while adding a product")
    raise HTTPException(
      status_code=500,
      detail="DB error while adding a product"
    ) from e


# 2. List all products with pagination.
def list_products(db : Session, page : int, page_size : int):
  try:
    total = db.query(InventoryProductDB).count()
    items = (
      db.query(InventoryProductDB)
        .order_by(InventoryProductDB.product_id)
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

  except SQLAlchemyError as e:
    logger.exception("DB error while listing products")
    raise HTTPException(
      status_code=500,
      detail="Internal server error"
    ) from e

  logger.info(f"Fetched {len(items)} products (page {page})")
  return {"items": items, "total": total, "page": page, "page_size": page_size}


# 3. Retrieve a product by ID.
def get_product_by_id(db : Session, id : int):
  try:
    product = db.query(InventoryProductDB).filter(
      InventoryProductDB.product_id == id
    ).first()

  except SQLAlchemyError as e:
    logger.exception(f"DB error while fetching the ID: {id}")
    raise HTTPException(
      status_code=500,
      detail="Internal server error"
    ) from e

  if product is None:
    logger.warning(f"Product with Id: {id} not found")
    raise HTTPException(
      status_code=404,
      detail="Product id not found"
    )

  return product


# 4. Update product information and pricing.
def update_product(db : Session, id : int, data : UpdateProduct):
  product = get_product_by_id(db,id)
  updated_product = data.model_dump(exclude_none=True)

  try:
    for key, value in updated_product.items():
      setattr(product,key,value)

    db.commit()
    db.refresh(product)

    logger.info(f"Successfully Updated the Product with ID: {id}")
    return product

  except SQLAlchemyError as e:
    db.rollback()
    logger.exception(f"DB error while updating product with ID: {id}")
    raise HTTPException(
      status_code=500,
      detail="Internal server error"
    ) from e


# 5. Delete a product.
def delete_product(db : Session, id : int):
  product = get_product_by_id(db, id)

  try:
    db.delete(product)
    db.commit()

    logger.info(f"Successfully deleted the product with ID: {id}")
    return{"detail":"Successfully deleted the product"}

  except SQLAlchemyError as e:
    db.rollback()
    logger.exception(f"DB error while deleting the Product with ID: {id}")
    raise HTTPException(
      status_code=500,
      detail="Internal server error"
    ) from e


# 6. Filter products by category.


# 7. Find low-stock products where quantity is at or below reorder level.


# 8. Increase stock by a supplied positive quantity.


# 9. Decrease stock for an order without allowing negative inventory.


# 10. Calculate total inventory value and inventory value by category.