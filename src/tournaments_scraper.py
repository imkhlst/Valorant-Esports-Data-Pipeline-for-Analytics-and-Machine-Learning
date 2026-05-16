from datetime import datetime
from constants.scraper_contants import *
from utils.scraper_utils import *
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
            contents = soup.select(".header-inner a[href]")
            for content in contents:
                href = content.get("href")
                if "events" not in href:
                    continue
                url = absolute(url=href)

            soup = get_soup(url=url)
            contents = soup.select(".wf-filter-inner a[href]")
            for content in contents:
                href = content.get("href")
                if "60" not in href:
                    continue
                url = absolute(url=href)

            soup = get_soup(url=url)
            contents = soup.select(".events-container-col a[href]")
            results = set()
            for content in contents:
                href = content.get("href")
                url = absolute(url=href)
                results.add(url)

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraping_tournament_list completed in {duration}s.")
            return list(results)
        
        except Exception as e:
            logging.error(f"Error Occurs when running scrape_tournament_list: {e}")
            print(f"Error Occurs when running scrape_tournament_list: {e}")

    def scrape_tournament_info(self, url: list) -> list:
        processed = set()
        queue = list(url) if isinstance(url, (set, list)) else [url]
        print(f"Queue: {queue[:3]}")
        try:
            results = []
            matches_page = set()
            stats_page = set()
            agents_page = set()
            start_time = datetime.now()
            for item in queue:
                if item in processed:
                    logging.info(f"{item} has been processed.")
                    continue

                soup = get_soup(url=item)
                tour_id = item.split("/")[4]
                tag = get_value(soup=soup, selector=".event-desc-inner a[href]", select_option=True)
                if not any(i in self.stage_keyword for i in tag.lower().split(" ")):
                    continue

                title = get_value(soup=soup, selector=".wf-title", select_option=True)
                title_split = title.split(":")[1].strip().split(" ", maxsplit=1) if ":" in title else title.split(" ", maxsplit=2)
                region = title_split[0] if len(title_split) == 2 else "all"
                stage =  title_split[1]
                
                results.append([tour_id, title, tag, stage, region])

                contents = soup.select(".wf-nav a[href]")
                for content in contents:
                    href = content.get("href")
                    url = absolute(url=href)
                    if "matches" in href:
                        matches_page.add((tour_id, url))
                    elif "stats" in href:
                        stats_page.add((tour_id, url))
                    elif "agents" in href:
                        agents_page.add((tour_id, url))
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
        tour_df = pd.DataFrame(tour_info, columns=["tour_id", "tour_name", "tour_tag", "tour_stage", "tour_region"])
        path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw\tour_raw.csv"
        tour_df.to_csv(path)
        logging.info(f"Data has been save in {path}")

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Tournament scraper pipeline completed in {duration}s")
        print(f"Tournament scraper pipeline completed in {duration}s")

        return matches_page, stats_page, agents_page