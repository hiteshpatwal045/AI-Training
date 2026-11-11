from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

PlayerRole = Literal[
  "Batter",
  "Bowler",
  "All-Rounder",
  "Wicketkeeper"
]

# 1. Create Player
class CreatePlayer(BaseModel):
  player_name: str = Field(min_length=1)
  team_name: str = Field(min_length=1)
  role : PlayerRole
  matches_played: int = Field(ge=0, default=0)
  total_runs: int = Field(ge=0, default=0)
  wickets_taken: int = Field(ge=0, default=0)
  balls_faced: int = Field(ge=0, default=0)
  catches: int = Field(ge=0, default=0)

#2. Update Player Statistics
class UpdatePlayer(BaseModel):
  matches_played: int | None = Field(default=None, ge=0)
  total_runs: int | None = Field(default=None, ge=0)
  wickets_taken: int | None = Field(default=None, ge=0)
  balls_faced: int | None = Field(default=None, ge=0)
  catches: int | None = Field(default=None, ge=0)

# 3. Player Response
class ResponsePlayer(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  player_id: int
  player_name: str
  team_name: str
  role: PlayerRole
  matches_played: int
  total_runs: int
  wickets_taken: int
  balls_faced: int
  catches: int

# 4. Team-wise statistics response
class TeamStatistics(BaseModel):
  team_name : str
  total_runs : int
  total_wickets : int


# 5. Batting Strike Rate
class BattingStrikeRate(BaseModel):
  player_id: int
  player_name: str
  total_runs: int
  balls_faced: int
  strike_rate: float | None