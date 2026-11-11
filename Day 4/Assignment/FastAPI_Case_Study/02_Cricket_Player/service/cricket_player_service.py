from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from logger import logger
from model.cricket_player_model import CricketPlayer
from schema.cricket_player_schema import (
  CreatePlayer,
  UpdatePlayer,
  BattingStrikeRate
)


# 1. Register a new cricket player.
def create_player(db: Session, data: CreatePlayer):
  try:
    new_player = CricketPlayer(**data.model_dump(exclude_none=True))

    db.add(new_player)
    db.commit()
    db.refresh(new_player)

    logger.info(f"Player created successfully with id: {new_player.player_id}")
    return new_player

  except IntegrityError:
    db.rollback()
    logger.warning("Duplicate player ID or DB constraint violation", exc_info=True)
    raise HTTPException(status_code=409, detail="Player already exists")

  except SQLAlchemyError:
    db.rollback()
    logger.exception("Database error while creating player")
    raise HTTPException(status_code=500, detail="Database error while creating player")


# 2. List all players with pagination.
def get_all_players(db: Session, skip: int = 0, limit: int = 10):
  try:
    return db.query(CricketPlayer).offset(skip).limit(limit).all()
  except SQLAlchemyError:
    logger.exception("DB error while fetching players")
    raise HTTPException(status_code=500, detail="Database error while fetching players")


# 3. Find a player by player ID.
def get_player_by_id(db: Session, id: int):
  try:
    player = db.query(CricketPlayer).filter(CricketPlayer.player_id == id).first()
  except SQLAlchemyError:
    logger.exception(f"DB error while fetching player ID: {id}")
    raise HTTPException(status_code=500, detail="Database error while fetching player")

  if player is None:
    logger.warning(f"Player with ID {id} not found")
    raise HTTPException(status_code=404, detail="Player not found")

  return player


# 4. Update player match statistics.
def update_player(db: Session, id: int, data: UpdatePlayer):
  player = get_player_by_id(db, id)
  update_data = data.model_dump(exclude_none=True)

  try:
    for key, value in update_data.items():
      setattr(player, key, value)

    db.commit()
    db.refresh(player)

    logger.info(f"Player with ID {id} updated successfully")
    return player

  except SQLAlchemyError:
    db.rollback()
    logger.exception(f"DB error while updating player ID: {id}")
    raise HTTPException(status_code=500, detail="Database error while updating player")


# 5. Delete a player.
def delete_player(db: Session, id: int):
  player = get_player_by_id(db, id)

  try:
    db.delete(player)
    db.commit()
    logger.info(f"Player with ID {id} deleted successfully")
    return {"detail": "Player deleted successfully"}

  except SQLAlchemyError:
    db.rollback()
    logger.exception(f"DB error while deleting player ID: {id}")
    raise HTTPException(status_code=500, detail="Database error while deleting player")


# 6. Filter players by team.
def get_players_by_team(db: Session, team_name: str):
  try:
    players = db.query(CricketPlayer).filter(CricketPlayer.team_name == team_name).all()

    if not players:
      logger.info(f"No players found for team {team_name}")

    return players

  except SQLAlchemyError:
    logger.exception(f"DB error while fetching players for team {team_name}")
    raise HTTPException(status_code=500, detail="Database error while fetching players by team")


# 7. List all-rounders with at least 10 wickets.
def get_all_rounders(db: Session):
  try:
    return db.query(CricketPlayer).filter(
      CricketPlayer.role == "All-Rounder",
      CricketPlayer.wickets_taken >= 10
    ).all()
  except SQLAlchemyError:
    logger.exception("DB error while fetching all-rounders")
    raise HTTPException(status_code=500, detail="Database error while fetching all-rounders")


# 8. Return the top five run scorers.
def get_top_run_scorers(db: Session):
  try:
    return db.query(CricketPlayer).order_by(CricketPlayer.total_runs.desc()).limit(5).all()
  except SQLAlchemyError:
    logger.exception("DB error while fetching top run scorers")
    raise HTTPException(status_code=500, detail="Database error while fetching top run scorers")


# 9. Calculate batting strike rate as runs divided by balls faced multiplied by 100.
def get_strike_rate(db: Session, id: int):
  player = get_player_by_id(db, id)

  strike_rate = 0.0
  if player.balls_faced > 0:
    strike_rate = round((player.total_runs / player.balls_faced) * 100, 2)

  return BattingStrikeRate(
    player_id=player.player_id,
    player_name=player.player_name,
    total_runs=player.total_runs,
    balls_faced=player.balls_faced,
    strike_rate=strike_rate
  )


# 10. Calculate total runs and wickets for each team.
def get_team_statistics(db: Session):
  try:
    stats = (
      db.query(
        CricketPlayer.team_name,
        func.sum(CricketPlayer.total_runs),
        func.sum(CricketPlayer.wickets_taken)
      )
      .group_by(CricketPlayer.team_name)
      .all()
    )

    return [
      {
        "team_name": team,
        "total_runs": int(runs or 0),
        "total_wickets": int(wickets or 0)
      }
      for team, runs, wickets in stats
    ]

  except SQLAlchemyError:
    logger.exception("DB error while calculating team statistics")
    raise HTTPException(status_code=500, detail="Database error while calculating team statistics")