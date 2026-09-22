from datetime import datetime
from utils.scraper_utils import *
from entities.map_veto_entities import *
from logger import logging

class MapVetosScraper:
    def __init__(self):
        pass

    def scrape_map_veto(self, soup, match_id: str):
        logging.info("Initialize scrape_map_veto ...")

        try:
            map_order_container = get_value(soup=soup, selector=".match-header-note", attr="text", multiple=True)

            if map_order_container[-1] is None:
                logging.info(f"Map selection not found.")
                return None

            map_order = map_order_container[-1].split(";")
            vetos = set()

            for map in map_order:
                map_split = map.strip().split(" ")

                if map_split[1].strip() == "ban" or map_split[1].strip() == "pick":
                    veto = MapVeto(
                        match_id=match_id,
                        team_name=map_split[0],
                        action=map_split[1].lower(),
                        map_name=map_split[2],
                        scraped_at=datetime.now()
                    )
                    logging.info(f"Completed! {map_split[2]} as {map_split[1].strip()} map by {map_split[0]} on match ID {match_id} has been scraped.")
                    vetos.add(veto)

                else:
                    veto = MapVeto(
                        match_id=match_id,
                        map_name=map_split[0],
                        scraped_at=datetime.now()
                    )
                    logging.info(f"Completed! {map_split[0]} as decider map on match ID {match_id} has been scraped.")
                    vetos.add(veto)

            return vetos

        except Exception as e:
            logging.error(f"Error occurs whe running scrape_map_veto: {e}")
            save_pipeline(
                status="failed",
                module=["matches"]
            )
            raise