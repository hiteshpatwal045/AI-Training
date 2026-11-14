from pydantic import BaseModel, Field

class ProductRequest(BaseModel):
  product_id : str
  product_name : str
  customer_name : str
  rating : float
  review_text : str


class ProductResponse(BaseModel):
  product_id: str
  sentiment : str
  review_summary : str
  positive_aspects : list[str]
  negative_aspects : list[str]
  issue_categories : list[str]
  improvement_suggestions : list[str]
  recommended_follow_up : str
