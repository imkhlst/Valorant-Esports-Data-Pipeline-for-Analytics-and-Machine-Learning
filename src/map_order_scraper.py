from datetime import datetime
from constants.scraper_constants import *
from utils.scraper_utils import *
from entities.match_entities import *
from logger import logging

class MapOrderScraper:
    def __init__(self):
        pass

    def scrape_map_order(soup):
        map_order_container = get_value(soup=soup, selector=".match-header-note", attr="text", multiple=True)
        if map_order_container[-1] is None:
            logging.info(f"Map selection not found.")
            return None

        map_order = map_order_container[-1].split(";")
        team_name, phase, map_name = [], [], []
        for map in map_order:
            map_split = map.strip().split(" ")
            if map_split[1].strip() == ("ban"|"pick"):
                team_name.append(map_split[0])
                phase.append(map_split[1])
                map_name.append(map_split[2])
            else:
                map_name.append(map_split[0])

        return team_name, phase, map_name