from pathlib import Path
from utils.scraper_utils import *
from src.scraper.tournaments_scraper import TournamentScraper
from src.scraper.matches_scraper import MatchesScraper
from src.scraper.games_scraper import GamesScraper

def main():
        checkpoint = (
            load_json(Path("data/checkpoint/pipeline_state.json"))
            if Path("data/checkpoint/pipeline_state.json").exists()
            else {"pipeline_status": "in_progress", "module_name": "tournaments", "module_status": False}
        )

        if not checkpoint["module_status"] and "tournaments" in checkpoint["module_name"]:
            tournament_scraper = TournamentScraper()
            tournament_scraper.run()
        
        if not checkpoint["module_status"] and "matches" in checkpoint["module_name"]:
            match_scraper = MatchesScraper()
            match_scraper.run(match_pages=Path("data/link/tours.json"))

        if not checkpoint["module_status"] and "games" in checkpoint["module_name"]:
            game_scraper = GamesScraper()
            game_scraper.run(tab_list=Path("data/link/matches.json"))

if __name__ == "__main__":
    main()