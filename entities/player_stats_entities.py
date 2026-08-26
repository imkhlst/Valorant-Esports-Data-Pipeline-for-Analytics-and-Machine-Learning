from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class PlayerStats:
    game_id: str
    name: str
    team_alias: str
    nationality: str
    agent: str
    mod: str
    r: float
    acs: int
    k: int
    d: int
    a: int
    kd: int
    kast: int
    adr: int
    hs: int
    fk: int
    fd: int
    fkfd: int