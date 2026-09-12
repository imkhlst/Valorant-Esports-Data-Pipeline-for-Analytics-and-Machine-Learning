import pandas as pd
from pathlib import Path
from datetime import timedelta

BASE_URL = "https://www.vlr.gg"

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/142.0")
}

STAGE_KEYWORD = [
    "masters",
    "champions",
    "stage 1",
    "stage 2",
    "kickoff"
]

REGION_KEYWORD = [
    "pasific",
    "emea",
    "americas",
    "china"
]

FILE_NAME = [
    "tours",
    "matches",
    "games_overview",
    "games_economy",
    "map_vetos",
    "players"
]

MAX_RUNTIME = timedelta(hours=4, minutes=45)

try:
    EXIST_TOUR_DATA = pd.read_parquet(Path("data/raw/tours.parquet"))

except Exception:
    EXIST_TOUR_DATA = pd.DataFrame(columns=["tour_id", "status"])