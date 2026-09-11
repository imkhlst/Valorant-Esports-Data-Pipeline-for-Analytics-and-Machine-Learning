
import argparse
from datetime import datetime
from pathlib import Path
from utils.scraper_utils import *
from src.scraper.tournaments_scraper import TournamentScraper
from src.scraper.matches_scraper import MatchesScraper
from src.scraper.games_scraper import GamesScraper

def main():
    start_time = datetime.now()

    parser = argparse.ArgumentParser(description="Pipeline multi-environment.")

    parser.add_argument("--ci", action="store_true", help="CI mode activated")
    parser.add_argument("--dev", action="store_true", help="Development mode activated")
    parser.add_argument("--prod", action="store_true", help="Production mode activated")

    args = parser.parse_args()
    
    checkpoint = (
        load_json(Path("data/checkpoint/pipeline_state.json"))
        if Path("data/checkpoint/pipeline_state.json").exists()
        else {"pipeline_status": "in_progress", "module_name": ["tournaments", "matches", "games"], "module_status": False}
    )

    if args.dev:
        if not checkpoint["module_status"] and "tournaments" in checkpoint["module_name"]:
            tournament_scraper = TournamentScraper()
            tournament_scraper.run(mode="dev", pipeline_start_time=start_time)
        
        if not checkpoint["module_status"] and "matches" in checkpoint["module_name"]:
            match_scraper = MatchesScraper()
            match_scraper.run(match_pages=Path("data/link/tours.json"), mode="dev", pipeline_start_time=start_time)

        if not checkpoint["module_status"] and "games" in checkpoint["module_name"]:
            game_scraper = GamesScraper()
            game_scraper.run(tab_list=Path("data/link/matches.json"), mode="dev", pipeline_start_time=start_time)

    elif args.ci:
        if not checkpoint["module_status"] and "tournaments" in checkpoint["module_name"]:
            tournament_scraper = TournamentScraper()
            tournament_scraper.run(mode="ci", pipeline_start_time=start_time)
        
        if not checkpoint["module_status"] and "matches" in checkpoint["module_name"]:
            match_scraper = MatchesScraper()
            match_scraper.run(match_pages=Path("data/link/tours.json"), mode="ci", pipeline_start_time=start_time)

        if not checkpoint["module_status"] and "games" in checkpoint["module_name"]:
            game_scraper = GamesScraper()
            game_scraper.run(tab_list=Path("data/link/matches.json"), mode="ci", pipeline_start_time=start_time)

    elif args.prod:
        if not checkpoint["module_status"] and "tournaments" in checkpoint["module_name"]:
            tournament_scraper = TournamentScraper()
            tournament_scraper.run(mode="prod", pipeline_start_time=start_time)
        
        if not checkpoint["module_status"] and "matches" in checkpoint["module_name"]:
            match_scraper = MatchesScraper()
            match_scraper.run(match_pages=Path("data/link/tours.json"), mode="prod", pipeline_start_time=start_time)

        if not checkpoint["module_status"] and "games" in checkpoint["module_name"]:
            game_scraper = GamesScraper()
            game_scraper.run(tab_list=Path("data/link/matches.json"), mode="prod", pipeline_start_time=start_time)

if __name__ == "__main__":
    main()