from typing import List, Optional

from pydantic import BaseModel


class TeamInfo(BaseModel):
    name: str


class PlaceInfo(BaseModel):
    name: str


class MatchInfo(BaseModel):
    match_id: int
    status_code: int
    status: str
    match_start: str
    home_team: TeamInfo
    away_team: TeamInfo
    venue: Optional[PlaceInfo]


class ApiResponse(BaseModel):
    data: List[MatchInfo]
