from dataclasses import dataclass, asdict

@dataclass
class PlayerStats:
    match_id: str
    game_id: str
    name: str
    team: str
    nationality: str
    stat_scope: str
    side: str
    r: float
    acs: int
    k: int
    d: int
    a: int
    kd: int
    kast: float
    adr: int
    hs: float
    fk: int
    fd: int
    fkfd: int