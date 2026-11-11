from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session

from config.database import Base, get_db, engine
from service import cricket_player_service as service

from schema.cricket_player_schema import (
  CreatePlayer,
  UpdatePlayer,
  TeamStatistics,
  ResponsePlayer,
  BattingStrikeRate
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cricket Player API")


# 1. Register a new cricket player.
@app.post("/players", response_model=ResponsePlayer)
def add_player(data: CreatePlayer, db: Session = Depends(get_db)):
  return service.create_player(db, data)


# 2. List all players with pagination.
@app.get("/players", response_model=list[ResponsePlayer])
def list_player(
  skip: int = Query(default=0, ge=0),
  limit: int = Query(default=10, ge=1, le=100),
  db: Session = Depends(get_db)
):
  return service.get_all_players(db, skip, limit)


# 6. Filter players by team.
@app.get("/players/team/{team_name}", response_model=list[ResponsePlayer])
def players_by_team(team_name: str, db: Session = Depends(get_db)):
  return service.get_players_by_team(db, team_name)


# 7. List all-rounders with at least 10 wickets.
@app.get("/players/all-rounders", response_model=list[ResponsePlayer])
def all_rounders(db: Session = Depends(get_db)):
  return service.get_all_rounders(db)


# 8. Return the top five run scorers.
@app.get("/players/top-scorers", response_model=list[ResponsePlayer])
def top_run_scorers(db: Session = Depends(get_db)):
  return service.get_top_run_scorers(db)


# 9. Calculate batting strike rate.
@app.get("/players/{id}/strike-rate", response_model=BattingStrikeRate)
def batting_strike_rate(id: int, db: Session = Depends(get_db)):
  return service.get_strike_rate(db, id)


# 10. Get total runs and wickets for each team.
@app.get("/teams/statistics", response_model=list[TeamStatistics])
def team_statistics(db: Session = Depends(get_db)):
  return service.get_team_statistics(db)


# 3. Find a player by player ID.
@app.get("/players/{id}", response_model=ResponsePlayer)
def player_details(id: int, db: Session = Depends(get_db)):
  return service.get_player_by_id(db, id)


# 4. Update player match statistics.
@app.patch("/players/{id}", response_model=ResponsePlayer)
def update_player(id: int, data: UpdatePlayer, db: Session = Depends(get_db)):
  return service.update_player(db, id, data)


# 5. Delete a player.
@app.delete("/players/{id}")
def delete_player(id: int, db: Session = Depends(get_db)):
  return service.delete_player(db, id)