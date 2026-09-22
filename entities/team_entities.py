from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Team:
    tour_id: str
    team_id: str
    team_name: str
    team_alias: str
    team_country: str
    scraped_at: datetime