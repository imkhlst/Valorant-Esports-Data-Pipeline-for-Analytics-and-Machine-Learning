
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
        else {"pipeline_status": "in_progress", "module_name": ["tournaments"], "module_status": False}
    )

    if not checkpoint["module_status"] and "tournaments" in checkpoint["module_name"]:
        tournament_scraper = TournamentScraper()
        if args.dev:
            tournament_scraper.run(mode="dev", pipeline_start_time=start_time)
        elif args.ci:
            tournament_scraper.run(mode="ci", pipeline_start_time=start_time)
        elif args.prod:
            tournament_scraper.run(mode="prod", pipeline_start_time=start_time)

    checkpoint = load_json(Path("data/checkpoint/pipeline_state.json"))
    
    if not checkpoint["module_status"] and "matches" in checkpoint["module_name"]:
        match_scraper = MatchesScraper()
        if args.dev:
            match_scraper.run(mode="dev", pipeline_start_time=start_time)
        elif args.ci:
            match_scraper.run(mode="ci", pipeline_start_time=start_time)
        elif args.prod:
            match_scraper.run(mode="prod", pipeline_start_time=start_time)

    checkpoint = load_json(Path("data/checkpoint/pipeline_state.json"))

    if not checkpoint["module_status"] and "games" in checkpoint["module_name"]:
        game_scraper = GamesScraper()
        if args.dev:
            game_scraper.run(mode="dev", pipeline_start_time=start_time)
        elif args.ci:
            game_scraper.run(mode="ci", pipeline_start_time=start_time)
        elif args.prod:
            game_scraper.run(mode="prod", pipeline_start_time=start_time)

if __name__ == "__main__":
    main()