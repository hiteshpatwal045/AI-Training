    from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base
from decimal import Decimal

class InventoryProductDB(Base):
  __tablename__ = "inventory_product"

  product_id        = Column(Integer,nullable=False,unique=True)
  product_name      = Column(String(100),nullable=False)
  category          = Column(String(100),nullable=False)
  supplier_name     = Column(String(100),nullable=False)
  unit_price        = Column(Decimal,nullable=False)
  quantity_in_stock = Column(Integer,nullable=False)
  reorder_level     = Column(Integer,nullable=False)
  warehouse_location= Column(String,nullable=False)
  is_active         = Column(Boolean,nullable=False)