from dataclasses import dataclass

@dataclass(frozen=True)
class ScraperResult:
    data: object
    completed: bool