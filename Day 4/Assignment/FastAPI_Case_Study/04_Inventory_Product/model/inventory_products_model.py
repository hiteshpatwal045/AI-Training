from sqlalchemy import Column, Integer, String, Boolean, Numeric
from config.database import Base

class InventoryProductDB(Base):
  __tablename__ = "inventory_product"

  product_id        = Column(Integer,primary_key=True,autoincrement=True)
  product_name      = Column(String(100),nullable=False)
  category          = Column(String(100),nullable=False)
  supplier_name     = Column(String(100),nullable=False)
  unit_price        = Column(Numeric(10,2),nullable=False)
  quantity_in_stock = Column(Integer,nullable=False)
  reorder_level     = Column(Integer,nullable=False)
  warehouse_location= Column(String(100),nullable=False)
  is_active         = Column(Boolean,nullable=False)