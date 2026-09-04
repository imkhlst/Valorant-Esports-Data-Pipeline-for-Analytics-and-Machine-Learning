from src.scraper.tournaments_scraper import TournamentScraper
from src.scraper.matches_scraper import MatchesScraper
from src.scraper.games_scraper import GamesScraper

# file_path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\link\tour.json"
def main():
    tournament_scraper = TournamentScraper()
    matches_page, stats_page, agents_page = tournament_scraper.run()

    match_scraper = MatchesScraper()
    matches = match_scraper.run(match_pages=matches_page)

    game_scraper = GamesScraper()
    games = game_scraper.run(tab_list=matches)


if __name__ == "__main__":
    main()