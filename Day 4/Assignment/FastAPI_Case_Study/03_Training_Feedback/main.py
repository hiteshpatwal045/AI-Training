from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from config.database import Base, engine, get_db
from logger import logger
from model.training_feedback_model import TrainingFeedback  # noqa: F401 (needed so create_all sees the table)
from service import training_feedback_service as service

from schema.training_feedback_schema import (
  CreateFeedback,
  UpdateFeedback,
  ResponseFeedback,
  TrainerAverageResponse,
  CourseRecommendationResponse
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Training Feedback API")

# 1. Submit a learner feedback record.
@app.post("/feedback", response_model=ResponseFeedback)
def add_feedback(data: CreateFeedback, db: Session = Depends(get_db)):
  return service.create_feedback(db, data)


# 2. List feedback records with pagination.
@app.get("/feedback", response_model=list[ResponseFeedback])
def list_feedback(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
  return service.get_all_feedback(db, skip, limit)


# 9. Identify low-rated sessions where any rating is 2 or below.
@app.get("/feedback/low-rated", response_model=list[ResponseFeedback])
def low_rated_feedback(db: Session = Depends(get_db)):
  return service.get_low_rated_feedback(db)


# 8. Calculate average trainer rating for each trainer.
@app.get("/feedback/trainer-averages", response_model=list[TrainerAverageResponse])
def trainer_averages(db: Session = Depends(get_db)):
  return service.get_trainer_average_ratings(db)


# 6. Filter feedback by trainer name.
@app.get("/feedback/trainer/{trainer_name}", response_model=list[ResponseFeedback])
def feedback_by_trainer(trainer_name: str, db: Session = Depends(get_db)):
  return service.get_feedback_by_trainer(db, trainer_name)


# 10. Calculate recommendation percentage for a selected course.
@app.get("/feedback/course/{course_name}/recommendation", response_model=CourseRecommendationResponse)
def course_recommendation(course_name: str, db: Session = Depends(get_db)):
  return service.get_course_recommendation(db, course_name)


# 7. Filter feedback by course name.
@app.get("/feedback/course/{course_name}", response_model=list[ResponseFeedback])
def feedback_by_course(course_name: str, db: Session = Depends(get_db)):
  return service.get_feedback_by_course(db, course_name)


# 3. Get feedback by feedback ID.
@app.get("/feedback/{id}", response_model=ResponseFeedback)
def feedback_details(id: int, db: Session = Depends(get_db)):
  return service.get_feedback_by_id(db, id)


# 4. Update an existing feedback entry.
@app.patch("/feedback/{id}", response_model=ResponseFeedback)
def update_feedback(id: int, data: UpdateFeedback, db: Session = Depends(get_db)):
  return service.update_feedback(db, id, data)


# 5. Delete a feedback entry.
@app.delete("/feedback/{id}")
def delete_feedback(id: int, db: Session = Depends(get_db)):
  return service.delete_feedback(db, id)