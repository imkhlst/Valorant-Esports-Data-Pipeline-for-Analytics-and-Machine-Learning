from datetime import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class Player:
    player_id: str
    player_nickname: str
    player_realname: str
    player_nationality: str
    # status: str
    # current_team: str
    # join_date: str
    # past_team: str
    # leave_date: str
    scraped_at: datetime