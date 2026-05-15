from src.tournaments_scraper import TournamentScraper

tournament_scraper = TournamentScraper()
matches_page, stats_page, agents_page = tournament_scraper.run()