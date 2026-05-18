from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Game:
    match_id: str
    game_id: str
    game_map: str
    game_duration: datetime
    home_score: int
    away_score: int
    home_att_score: int
    away_att_score: int
    home_def_score: int
    away_def_score: int
    home_pstl_win: int
    away_pstl_win: int
    home_eco_round: int
    away_eco_round: int
    home_eco_win: int
    away_eco_win: int
    home_semi_eco_round: int
    away_semi_eco_round: int
    home_semi_eco_win: int
    away_semi_eco_win: int
    home_semi_buy_round: int
    away_semi_buy_round: int
    home_semi_buy_win: int
    away_semi_buy_win: int
    home_full_buy_round: int
    away_full_buy_round: int
    home_full_buy_win: int
    away_full_buy_win: int