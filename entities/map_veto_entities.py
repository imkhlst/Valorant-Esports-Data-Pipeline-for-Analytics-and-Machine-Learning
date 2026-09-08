from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass(frozen=True)
class MapVeto:
    match_id: str
    map_name: str
    scraped_at: datetime
    team_name: Optional[str] = None
    action: Optional[str] = "decider"