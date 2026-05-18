from datetime import datetime
from dataclasses import dataclass, asdict, field
from typing import Optional

@dataclass
class Match:
    tour_id: str
    match_id: str
    date: datetime
    bracket: str

    home_name: str
    home_alias: str
    away_name: str
    away_alias: str

    bo: str
    home_score: int
    away_score: int

    home_h2h_win: int
    away_h2h_win: int
    home_h2h_score: int
    away_h2h_score: int

    home_n_last_win: int
    away_n_last_win: int
    home_n_last_match: int
    away_n_last_match: int
    home_n_last_wr: float = field(init=False)
    away_n_last_wr: float = field(init=False)

    patch: Optional[str] = None

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

    def __post_init__(self) -> None:
        self.home_last_5_wr = self.home_n_last_win / self.home_n_last_match
        self.away_last_5_wr = self.away_n_last_win / self.away_n_last_match