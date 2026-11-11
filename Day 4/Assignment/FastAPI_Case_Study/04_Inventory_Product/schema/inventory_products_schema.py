from pydantic import Field, BaseModel, ConfigDict
from decimal import Decimal

# 1. AddProduct
class AddProduct(BaseModel):
  product_name: str = Field(min_length=1)
  category: str = Field(min_length=1)
  supplier_name: str = Field(min_length=1)
  unit_price: Decimal = Field(ge=0)
  quantity_in_stock: int = Field(ge=0)
  reorder_level: int = Field(ge=0)
  warehouse_location: str = Field(min_length=1)
  is_active: bool

# 2. update Product
class UpdateProduct(BaseModel):
  product_name: str | None = Field(default=None,min_length=1)
  unit_price: Decimal | None = Field(default=None,ge=0)
  quantity_in_stock: int | None = Field(default=None,ge=0)
  reorder_level: int | None = Field(default=None,ge=0)
  warehouse_location: str | None = Field(default=None,min_length=1)
  is_active: bool | None = None

# 3. Response
class InventoryProduct(AddProduct):
  product_id : int
  model_config = ConfigDict(from_attributes=True)

# 4. StockIncrease
class StockIncrease(BaseModel):
  quantity : int = Field(gt=0)

# 5. StockDecrease
class StockDecrease(BaseModel):
  quantity : int = Field(gt=0)

# 6. total InventoryValue and inventory value by Category
class InventoryValue(BaseModel):
  category : str
  total_value : int
