import pandas as pd
from pathlib import Path

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
    "tours1",
    "matches1",
    "games_overview1",
    "games_economy1",
    "map_vetos1",
    "players1"
]

try:
    EXIST_TOUR_DATA = pd.read_parquet(Path("data/raw/final/tours.parquet"))
    if EXIST_TOUR_DATA.empty:
        EXIST_TOUR_DATA = []

except Exception:
    EXIST_TOUR_DATA = []