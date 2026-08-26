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

    patch: Optional[str] = None