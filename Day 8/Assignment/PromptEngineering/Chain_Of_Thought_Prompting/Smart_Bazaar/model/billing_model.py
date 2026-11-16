from pydantic import BaseModel, Faild


class ProductItem(BaseModel):
  product_id : str
  name : str
  category : str
  quantity : int
  unit_price : int
  gst_rate : int

class BillingRequest(BaseModel):
  customer_name : str
  membership_tier : str
  coupon_code : str
  loyalty_points_available : int
  loyalty_points_to_redeem : int
  items : ProductItem

class BillingResponse(BaseModel):
  