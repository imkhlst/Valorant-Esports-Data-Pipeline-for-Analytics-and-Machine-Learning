from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

@dataclass
class GameOverview:
    match_id: str
    game_id: str
    game_map: str
    game_duration: str
    home_score: int
    away_score: int
    home_atk_score: int
    away_atk_score: int
    home_def_score: int
    away_def_score: int
    home_ot_score: int
    away_ot_score: int

@dataclass
class GameEconomy:
    match_id: str
    game_id: str
    home_pstl_win: Optional[int] = None
    away_pstl_win: Optional[int] = None
    home_eco_round: Optional[int] = None
    away_eco_round: Optional[int] = None
    home_eco_win: Optional[int] = None
    away_eco_win: Optional[int] = None
    home_semi_eco_round: Optional[int] = None
    away_semi_eco_round: Optional[int] = None
    home_semi_eco_win: Optional[int] = None
    away_semi_eco_win: Optional[int] = None
    home_semi_buy_round: Optional[int] = None
    away_semi_buy_round: Optional[int] = None
    home_semi_buy_win: Optional[int] = None
    away_semi_buy_win: Optional[int] = None
    home_full_buy_round: Optional[int] = None
    away_full_buy_round: Optional[int] = None
    home_full_buy_win: Optional[int] = None
    away_full_buy_win: Optional[int] = None