from datetime import datetime
from utils.scraper_utils import *
from entities.team_entities import *
from logger import logging

class TeamScraper:
    def __init__(self, url: str, tour_id: str):
        self.url = url
        self.tour_id = tour_id

    def scrape_team_info(self):
        logging.info("Initialize scrape_team_info ...")
        try:
            team_soup = get_soup(url=self.url)
            team_id = self.url.split("/")[-2]
            team_info = get_value(soup=team_soup, selector=".wf-title", attr="text", multiple=True)
            team_name = team_alias = team_info[0]

            if len(team_info) > 0:
                team_alias = team_info[1]

            team_country = get_value(soup=team_soup, selector=".team-header-country", attr="text")

            team = Team(
                tour_id=self.tour_id,
                team_id=team_id,
                team_name=team_name,
                team_alias=team_alias,
                team_country=team_country,
                scraped_at=datetime.now()
            )

            logging.info(f"Completed! {team_name} ({team_id}) as {team_alias} from {team_country} has been scraped.")

            return team

        except Exception as e:
            logging.error(f"Error occurs when running scrape_team_info: {e}")
            save_pipeline(
                status="failed",
                module=["matches"]
            )
            raise