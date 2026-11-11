from sqlalchemy import Integer, Column, String
from config.database import Base

class CricketPlayer(Base):
  __tablename__ = "cricket_player"

  player_id = Column(Integer, primary_key=True, index=True)
  player_name = Column(String(100), nullable=False)
  team_name = Column(String(100), nullable=False)
  role = Column(String(50), nullable=False)
  matches_played = Column(Integer, nullable=False, default=0)
  total_runs = Column(Integer, nullable=False, default=0)
  wickets_taken = Column(Integer, nullable=False, default=0)
  balls_faced = Column(Integer, nullable=False, default=0)
  catches = Column(Integer, nullable=False, default=0)