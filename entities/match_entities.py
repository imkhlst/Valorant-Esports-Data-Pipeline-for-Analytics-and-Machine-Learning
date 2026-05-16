import dataclasses
from typing import Optional

@dataclasses
class Match:
    tour_id: str
    match_id: str
    date: str
    bracket: str
    patch: str

    home_name: str
    home_alias: str
    away_name: str
    away_alias: str

    bo: str
    home_score: str
    away_score: str

    home_map_ban_1: Optional[str] = None
    home_map_ban_2: Optional[str] = None
    home_map_ban_3: Optional[str] = None
    home_map_pick_1: Optional[str] = None
    home_map_pick_2: Optional[str] = None
    away_map_ban_1: Optional[str] = None
    away_map_ban_2: Optional[str] = None
    away_map_ban_3: Optional[str] = None
    away_map_pick_1: Optional[str] = None
    away_map_pick_2: Optional[str] = None
    decider_map: Optional[str] = None

    home_h2h_win: int
    away_h2h_win: int
    home_h2h_score: int
    away_h2h_score: int

    home_last_5_wr: float
    away_last_5_wr: float