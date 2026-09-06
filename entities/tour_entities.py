from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class Tour:
    tour_id: str
    tour_name: str
    tour_tag: str
    tour_stage: str
    tour_region: str
    tour_status: str