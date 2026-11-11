from builtins import str, int, bool, float
from datetime import date
from pydantic import BaseModel, ConfigDict, Field

# 1. Create feedback (request body for POST)
class CreateFeedback(BaseModel):
  learner_name: str = Field(min_length=1, max_length=100)
  trainer_name: str = Field(min_length=1, max_length=100)
  course_name: str = Field(min_length=1, max_length=150)
  session_date: date
  content_rating: int = Field(ge=1, le=5)
  trainer_rating: int = Field(ge=1, le=5)
  hands_on_rating: int = Field(ge=1, le=5)
  comments: str | None = Field(default=None, max_length=500)
  would_recommend: bool

# 2. Update feedback (request body for PATCH, every field optional)
class UpdateFeedback(BaseModel):
  learner_name: str | None = Field(default=None, min_length=1, max_length=100)
  trainer_name: str | None = Field(default=None, min_length=1, max_length=100)
  course_name: str | None = Field(default=None, min_length=1, max_length=150)
  session_date: date | None = None
  content_rating: int | None = Field(default=None, ge=1, le=5)
  trainer_rating: int | None = Field(default=None, ge=1, le=5)
  hands_on_rating: int | None = Field(default=None, ge=1, le=5)
  comments: str | None = Field(default=None, max_length=500)
  would_recommend: bool | None = None

# 3. Feedback response
class ResponseFeedback(CreateFeedback):
  feedback_id: int
  model_config = ConfigDict(from_attributes=True)

# 4. Average trainer rating for 8th endpoint
class TrainerAverageResponse(BaseModel):
  trainer_name: str
  average_trainer_rating: float

# 5. Recommendation percentage for a course for 10th endpoint
class CourseRecommendationResponse(BaseModel):
  course_name: str
  total_responses: int
  recommended_count: int
  recommendation_percentage: float