from fastapi import HTTPException
from sqlalchemy import func, or_
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from logger import logger
from model.training_feedback_model import TrainingFeedback
from schema.training_feedback_schema import (
  CreateFeedback,
  UpdateFeedback,
  TrainerAverageResponse,
  CourseRecommendationResponse
)


# 1. Submit a learner feedback record.
def create_feedback(db: Session, data: CreateFeedback):
  try:
    new_feedback = TrainingFeedback(**data.model_dump(exclude_none=True))

    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    logger.info(f"Feedback created successfully with id: {new_feedback.feedback_id}")
    return new_feedback

  except IntegrityError:
    db.rollback()
    logger.warning("Duplicate feedback ID or DB constraint violation", exc_info=True)
    raise HTTPException(
      status_code=409,
      detail="Feedback already exists"
    )

  except SQLAlchemyError:
    db.rollback()
    logger.exception("Database error while creating feedback")
    raise HTTPException(
      status_code=500,
      detail="Database error while creating feedback"
    )


# 2. List feedback records with pagination.
def get_all_feedback(db: Session, skip: int = 0, limit: int = 10):
  try:
    return (
      db.query(TrainingFeedback)
      .order_by(TrainingFeedback.feedback_id)
      .offset(skip)
      .limit(limit)
      .all()
    )

  except SQLAlchemyError:
    logger.exception("DB error while fetching feedback list")
    raise HTTPException(
      status_code=500,
      detail="Database error while fetching feedback"
    )


# 3. Get feedback by feedback ID.
def get_feedback_by_id(db: Session, id: int):
  try:
    feedback = db.query(TrainingFeedback).filter(
      TrainingFeedback.feedback_id == id
    ).first()

  except SQLAlchemyError:
    logger.exception(f"DB error while fetching feedback ID: {id}")
    raise HTTPException(
      status_code=500,
      detail="Database error while fetching feedback"
    )

  if feedback is None:
    logger.warning(f"Feedback with ID {id} not found")
    raise HTTPException(
      status_code=404,
      detail="Feedback not found"
    )

  return feedback


# 4. Update an existing feedback entry.
def update_feedback(db: Session, id: int, data: UpdateFeedback):
  feedback = get_feedback_by_id(db, id)
  update_data = data.model_dump(exclude_none=True)

  try:
    for key, value in update_data.items():
      setattr(feedback, key, value)

    db.commit()
    db.refresh(feedback)

    logger.info(f"Feedback with ID {id} updated successfully")
    return feedback

  except SQLAlchemyError:
    db.rollback()
    logger.exception(f"DB error while updating feedback ID: {id}")
    raise HTTPException(
      status_code=500,
      detail="Database error while updating feedback"
    )


# 5. Delete a feedback entry.
def delete_feedback(db: Session, id: int):
  feedback = get_feedback_by_id(db, id)

  try:
    db.delete(feedback)
    db.commit()

    logger.info(f"Feedback with ID {id} deleted successfully")
    return {"detail": "Feedback deleted successfully"}

  except SQLAlchemyError:
    db.rollback()
    logger.exception(f"DB error while deleting feedback ID: {id}")
    raise HTTPException(
      status_code=500,
      detail="Database error while deleting feedback"
    )


# 6. Filter feedback by trainer name.
def get_feedback_by_trainer(db: Session, trainer_name: str):
  try:
    feedback = db.query(TrainingFeedback).filter(
      TrainingFeedback.trainer_name == trainer_name
    ).all()

    if not feedback:
      logger.info(f"No feedback found for trainer {trainer_name}")

    return feedback

  except SQLAlchemyError:
    logger.exception(f"DB error while fetching feedback for trainer {trainer_name}")
    raise HTTPException(
      status_code=500,
      detail="Database error while fetching feedback by trainer"
    )


# 7. Filter feedback by course name.
def get_feedback_by_course(db: Session, course_name: str):
  try:
    feedback = db.query(TrainingFeedback).filter(
      TrainingFeedback.course_name == course_name
    ).all()

    if not feedback:
      logger.info(f"No feedback found for course {course_name}")

    return feedback

  except SQLAlchemyError:
    logger.exception(f"DB error while fetching feedback for course {course_name}")
    raise HTTPException(
      status_code=500,
      detail="Database error while fetching feedback by course"
    )


# 8. Calculate average trainer rating for each trainer.
def get_trainer_average_ratings(db: Session):
  try:
    rows = (
      db.query(
        TrainingFeedback.trainer_name,
        func.avg(TrainingFeedback.trainer_rating)
      )
      .group_by(TrainingFeedback.trainer_name)
      .all()
    )

    return [
      TrainerAverageResponse(
        trainer_name=trainer,
        average_trainer_rating=round(float(avg), 2)
      )
      for trainer, avg in rows
    ]

  except SQLAlchemyError:
    logger.exception("DB error while calculating trainer average ratings")
    raise HTTPException(
      status_code=500,
      detail="Database error while calculating trainer averages"
    )


# 9. Identify low-rated sessions where any rating is 2 or below.
def get_low_rated_feedback(db: Session):
  try:
    return db.query(TrainingFeedback).filter(
        (TrainingFeedback.content_rating <= 2) |
        (TrainingFeedback.trainer_rating <= 2) |
        (TrainingFeedback.hands_on_rating <= 2)
    ).all()

  except SQLAlchemyError:
    logger.exception("DB error while fetching low-rated feedback")
    raise HTTPException(
      status_code=500,
      detail="Database error while fetching low-rated feedback"
    )


# 10. Calculate recommendation percentage for a selected course.
def get_course_recommendation(db: Session, course_name: str):
  try:
    total = db.query(func.count(TrainingFeedback.feedback_id)).filter(
      TrainingFeedback.course_name == course_name
    ).scalar()

    recommended = db.query(func.count(TrainingFeedback.feedback_id)).filter(
      TrainingFeedback.course_name == course_name,
      TrainingFeedback.would_recommend.is_(True)
    ).scalar()

  except SQLAlchemyError:
    logger.exception(f"DB error while calculating recommendation for course {course_name}")
    raise HTTPException(
      status_code=500,
      detail="Database error while calculating recommendation percentage"
    )

  if total == 0:
    logger.warning(f"No feedback found for course {course_name}")
    raise HTTPException(
      status_code=404,
      detail="No feedback found for this course"
    )

  return CourseRecommendationResponse(
    course_name=course_name,
    total_responses=total,
    recommended_count=recommended,
    recommendation_percentage=round((recommended / total) * 100, 2)
  )