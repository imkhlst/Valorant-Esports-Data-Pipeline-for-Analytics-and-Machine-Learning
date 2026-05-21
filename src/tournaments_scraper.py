from datetime import datetime
from constants.scraper_constants import *
from utils.scraper_utils import *
from entities.tour_entities import *
from logger import logging

class TournamentScraper:
    def __init__(self, base_url: str = BASE_URL, region_keyword: list = REGION_KEYWORD, stage_keyword: list = STAGE_KEYWORD):
        self.base_url = base_url
        self.stage_keyword = stage_keyword
        self.region_keyword = region_keyword

    def scrape_tournament_list(self):
        start_time = datetime.now()
        tour_list = set()
        try:
            soup = get_soup(url=self.base_url)
            elements = get_value(soup=soup, selector=".header-inner a[href]", attr="href", multiple=True)
            for el in elements:
                if "events" not in el:
                    continue
                url = absolute(url=el)

            soup = get_soup(url=url)
            elements = get_value(soup=soup, selector=".wf-filter-inner a[href]", attr="href", multiple=True)
            for el in elements:
                if "60" not in el:
                    continue
                url = absolute(url=el)

            soup = get_soup(url=url)
            elements = get_value(soup=soup, selector=".events-container-col a", multiple=True)
            for el in elements:
                href = el.get("href")
                url = absolute(url=href)
                status = get_value(soup=el, selector=".event-item-desc-item-status", attr="text")
                tour_list.add((status, url))

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraping_tournament_list completed in {duration}s.")
            return list(tour_list)
        
        except Exception as e:
            logging.error(f"Error Occurs when running scrape_tournament_list: {e}")
            print(f"Error Occurs when running scrape_tournament_list: {e}")

    def scrape_tournament_info(self, tour_list: list) -> list:
        start_time = datetime.now()
        processed = set()
        queue = list(tour_list) if isinstance(tour_list, (set, list)) else [tour_list]
        print(f"Queue: {queue[:2]}, ... , {queue[-1]}")
        try:
            tour_info = []
            matches_page = set()
            stats_page = set()
            agents_page = set()
            for item in queue:
                status, url = item[0], item[1]
                if url in processed:
                    logging.info(f"{url} has been processed.")
                    continue

                soup = get_soup(url=url)
                tour_id = int(url.split("/")[4])
                tag = get_value(soup=soup, selector=".event-desc-inner a[href]", attr="text")
                if not any(i in self.stage_keyword for i in tag.lower().split(" ")):
                    processed.add(url)
                    continue

                title = get_value(soup=soup, selector=".wf-title", attr="text")
                title_split = title.split(":")[1].strip().split(" ", maxsplit=1) if ":" in title else title.split(" ", maxsplit=2)
                region = title_split[0] if len(title_split) == 2 else "all"
                stage =  title_split[1]

                logging.info(f"{title} is Exist. Tournament status: {status}.")
                
                tour = Tour(
                    tour_id=tour_id,
                    tour_name=title,
                    tour_tag=tag,
                    tour_stage=stage,
                    tour_region=region,
                    tour_status=status
                )
                tour_info.append(tour)
                
                if status.lower() == "upcoming" or status.lower() == "ongoing":
                    logging.info(f"{status} tournaments confirmed. Tournament must be completed to scrape matches list.")
                    processed.add(url)
                    continue

                elements = get_value(soup=soup, selector=".wf-nav a", attr="href", multiple=True)
                for el in elements:
                    content_url = absolute(url=el)
                    if "matches" in el:
                        content_url = content_url.replace(content_url[-4:], "all")
                        matches_page.add((tour_id, content_url))
                    elif "stats" in el:
                        stats_page.add((tour_id, content_url))
                    elif "agents" in el:
                        agents_page.add((tour_id, content_url))
                    else:
                        continue
                
                processed.add(url)

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraping_tournament_info completed in {duration}s.")
            return list(tour_info), list(matches_page), list(stats_page), list(agents_page)
        
        except Exception as e:
            logging.error(f"Error Occurs when running scrape_tournament_info: {e}")
            print(f"Error Occurs when running scrape_tournament_info: {e}")
    
    def run(self):
        start_time = datetime.now()
        
        logging.info("Initialization scrape_tournament_list ...")
        tour_list = self.scrape_tournament_list()
        logging.info("Initialize scrape_tournament_info ...")
        tour_info, matches_page, stats_page, agents_page = self.scrape_tournament_info(tour_list)
        tour_df = pd.DataFrame([asdict(t) for t in tour_info])
        path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw\tour_raw.csv"
        tour_df.to_csv(path)
        logging.info(f"Data has been save in {path}")

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Tournament scraper pipeline completed in {duration}s")
        print("="*50)
        print(f"Tournament scraper pipeline completed in {duration}s")
        print("="*50)

        return matches_page, stats_page, agents_page