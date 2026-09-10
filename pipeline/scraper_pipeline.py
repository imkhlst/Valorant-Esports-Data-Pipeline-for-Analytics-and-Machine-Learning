from pathlib import Path
from utils.scraper_utils import *
from src.scraper.tournaments_scraper import TournamentScraper
from src.scraper.matches_scraper import MatchesScraper
from src.scraper.games_scraper import GamesScraper

def main():
    checkpoint = load_json(Path("data/checkpoint/pipeline_state.json"))

    if not checkpoint.completed and "tournaments" in checkpoint.module:
        tournament_scraper = TournamentScraper()
        tournament_scraper.run()

    if not checkpoint.completed and "matches" in checkpoint.module:
        match_scraper = MatchesScraper()
        match_scraper.run(match_pages=Path("data/link/tours.json"))

    if not checkpoint.completed and "games" in checkpoint.module:
        game_scraper = GamesScraper()
        game_scraper.run(tab_list=Path("data/link/matches.json"))


if __name__ == "__main__":
    main()