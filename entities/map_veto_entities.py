from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class MapVeto:
    match_id: str
    map_name: str
    team_name: Optional[str] = None
    action: Optional[str] = "decider"