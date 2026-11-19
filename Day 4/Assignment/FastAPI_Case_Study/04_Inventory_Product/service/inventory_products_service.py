from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from logger import logger
from model.inventory_products_model import InventoryProductDB
from schema.inventory_products_schema import (
  AddProduct,
  UpdateProduct
)


# 1. Add a product.
def add_product(db: Session, data: AddProduct):
  try:
    product = InventoryProductDB(**data.model_dump(exclude_none=True))

    db.add(product)
    db.commit()
    db.refresh(product)

    logger.info(f"Product added successfully with ID: {product.product_id}")
    return product

  except IntegrityError:
    db.rollback()
    logger.warning("Duplicate product ID while adding a product")
    raise HTTPException(
      status_code=409,
      detail="Product ID already exists"
    )

  except SQLAlchemyError as e:
    db.rollback()
    logger.exception("DB error while adding a product")
    raise HTTPException(
      status_code=500,
      detail="DB error while adding a product"
    ) from e


# 2. List all products with pagination.
def list_products(db: Session, page: int = 1, limit: int = 10):
  try:
    total = db.query(InventoryProductDB).count()
    items = (
      db.query(InventoryProductDB)
      .order_by(InventoryProductDB.product_id)
      .offset((page - 1) * limit)
      .limit(limit)
      .all()
    )
    return {"total": total, "page": page, "limit": limit, "items": items}

  except SQLAlchemyError as e:
    logger.exception("DB error while listing products")
    raise HTTPException(
      status_code=500,
      detail="Internal server error"
    ) from e


# 3. Retrieve a product by ID.
def get_product_by_id(db: Session, id: int):
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
def update_product(db: Session, id: int, data: UpdateProduct):
  product = get_product_by_id(db, id)
  updated_product = data.model_dump(exclude_none=True)

  try:
    for key, value in updated_product.items():
      setattr(product, key, value)

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
def delete_product(db: Session, id: int):
  product = get_product_by_id(db, id)

  try:
    db.delete(product)
    db.commit()

    logger.info(f"Successfully deleted the product with ID: {id}")
    return {"detail": "Successfully deleted the product"}

  except SQLAlchemyError as e:
    db.rollback()
    logger.exception(f"DB error while deleting the Product with ID: {id}")
    raise HTTPException(
      status_code=500,
      detail="Internal server error"
    ) from e


# 6. Filter products by category.
def filter_by_category(db: Session, category: str):
  try:
    return db.query(InventoryProductDB).filter(
      func.lower(InventoryProductDB.category) == category.lower()
    ).all()

  except SQLAlchemyError as e:
    logger.exception(f"DB error while filtering category: {category}")
    raise HTTPException(
      status_code=500,
      detail="Internal server error"
    ) from e


# 7. Find low-stock products where quantity is at or below reorder level.
def get_low_stock(db: Session):
  try:
    return db.query(InventoryProductDB).filter(
      InventoryProductDB.quantity <= InventoryProductDB.reorder_level
    ).all()

  except SQLAlchemyError as e:
    logger.exception("DB error while fetching low-stock products")
    raise HTTPException(
      status_code=500,
      detail="Internal server error"
    ) from e


# 8. Increase stock by a supplied positive quantity.
def increase_stock(db: Session, id: int, qty: int):
  if qty <= 0:
    raise HTTPException(
      status_code=400,
      detail="Quantity must be positive"
    )

  product = get_product_by_id(db, id)

  try:
    product.quantity += qty
    db.commit()
    db.refresh(product)

    logger.info(f"Increased stock of product {id} by {qty}")
    return product

  except SQLAlchemyError as e:
    db.rollback()
    logger.exception(f"DB error while increasing stock for ID: {id}")
    raise HTTPException(
      status_code=500,
      detail="Internal server error"
    ) from e


# 9. Decrease stock for an order without allowing negative inventory.
def decrease_stock(db: Session, id: int, qty: int):
  if qty <= 0:
    raise HTTPException(
      status_code=400,
      detail="Quantity must be positive"
    )

  product = get_product_by_id(db, id)

  if product.quantity < qty:
    logger.warning(f"Insufficient stock for product {id}")
    raise HTTPException(
      status_code=400,
      detail="Insufficient stock"
    )

  try:
    product.quantity -= qty
    db.commit()
    db.refresh(product)

    logger.info(f"Decreased stock of product {id} by {qty}")
    return product

  except SQLAlchemyError as e:
    db.rollback()
    logger.exception(f"DB error while decreasing stock for ID: {id}")
    raise HTTPException(
      status_code=500,
      detail="Internal server error"
    ) from e


# 10. Calculate total inventory value and inventory value by category.
def inventory_value(db: Session):
  try:
    value = InventoryProductDB.price * InventoryProductDB.quantity

    total = db.query(func.coalesce(func.sum(value), 0)).scalar()
    rows = db.query(
      InventoryProductDB.category,
      func.coalesce(func.sum(value), 0)
    ).group_by(InventoryProductDB.category).all()

    return {
      "total_inventory_value": float(total),
      "by_category": {cat: float(val) for cat, val in rows}
    }

  except SQLAlchemyError as e:
    logger.exception("DB error while calculating inventory value")
    raise HTTPException(
      status_code=500,
      detail="Internal server error"
    ) from e