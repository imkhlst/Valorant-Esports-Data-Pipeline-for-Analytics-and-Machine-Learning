from dataclasses import dataclass

@dataclass
class Game:
    match_id: str
    game_id: str
    map: str
    duration: str
    home_score: str
    away_score: str
    home_att_score: str
    away_att_score: str
    home_def_score: str
    away_def_score: str
    home_att_score: str
    away_att_score: str
    home_pstl_win: str
    away_pstl_win: str
    home_eco_round: str
    away_eco_round: str
    home_eco_win: str
    away_eco_win: str
    home_semi_eco_round: str
    away_semi_eco_round: str
    home_semi_eco_win: str
    away_semi_eco_win: str
    home_semi_buy_round: str
    away_semi_buy_round: str
    home_semi_buy_win: str
    away_semi_buy_win: str
    home_full_buy_round: str
    away_full_buy_round: str
    home_full_buy_win: int
    away_full_buy_win: int