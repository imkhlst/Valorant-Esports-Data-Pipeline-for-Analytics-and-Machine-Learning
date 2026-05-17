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
        results = set()
        start_time = datetime.now()
        try:
            soup = get_soup(url=self.base_url)
            contents = get_value(soup=soup, selector=".header-inner a[href]", value="href")
            for content in contents:
                if "events" not in content:
                    continue
                url = absolute(url=content)

            soup = get_soup(url=url)
            contents = get_value(soup=soup, selector=".wf-filter-inner a[href]", value="href")
            for content in contents:
                if "60" not in content:
                    continue
                url = absolute(url=content)

            soup = get_soup(url=url)
            contents = soup.select(".events-container-col a")
            results = set()
            for content in contents:
                href = content.get("href")
                url = absolute(url=href)
                status = get_value(soup=content, selector=".event-item-desc-item-status", select_option=True)
                results.add((status, url))

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraping_tournament_list completed in {duration}s.")
            return list(results)
        
        except Exception as e:
            logging.error(f"Error Occurs when running scrape_tournament_list: {e}")
            print(f"Error Occurs when running scrape_tournament_list: {e}")

    def scrape_tournament_info(self, tour_list: list) -> list:
        processed = set()
        queue = list(tour_list) if isinstance(tour_list, (set, list)) else [tour_list]
        print(f"Queue: {queue[:3]}")
        try:
            results = []
            matches_page = set()
            stats_page = set()
            agents_page = set()
            start_time = datetime.now()
            for item in queue:
                status, url = item[0], item[1]
                if url in processed:
                    logging.info(f"{url} has been processed.")
                    continue

                soup = get_soup(url=url)
                tour_id = url.split("/")[4]
                tag = get_value(soup=soup, selector=".event-desc-inner a[href]", select_option=True)
                if not any(i in self.stage_keyword for i in tag.lower().split(" ")):
                    continue

                title = get_value(soup=soup, selector=".wf-title", select_option=True)
                title_split = title.split(":")[1].strip().split(" ", maxsplit=1) if ":" in title else title.split(" ", maxsplit=2)
                region = title_split[0] if len(title_split) == 2 else "all"
                stage =  title_split[1]
                
                tour = Tour(
                    tour_id=tour_id,
                    tour_name=title,
                    tour_tag=tag,
                    tour_stage=stage,
                    tour_region=region,
                    tour_status=status
                )
                results.append(tour)
                
                if status.lower() == "upcoming" or status.lower() == "ongoing":
                    logging.info(f"{status} tournaments confirmed. Tournament must be completed to scrape matches list.")
                    continue
                contents = soup.select(".wf-nav a[href]")
                for content in contents:
                    href = content.get("href")
                    content_url = absolute(url=href)
                    if "matches" in href:
                        matches_page.add((tour_id, content_url))
                    elif "stats" in href:
                        stats_page.add((tour_id, content_url))
                    elif "agents" in href:
                        agents_page.add((tour_id, content_url))
                    else:
                        continue
                
                processed.add(item)

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraping_tournament_info completed in {duration}s.")
            return list(results), list(matches_page), list(stats_page), list(agents_page)
        
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
        print(f"Tournament scraper pipeline completed in {duration}s")

        return matches_page, stats_page, agents_page