from datetime import datetime
from constants.scraper_contants import *
from utils.scraper_utils import *
from logger import logging

class TournamentScraper:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url

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
            logging.info(f"Scraping tournament list completed in {duration}s.")
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
                    continue
                soup = get_soup(url=item)
                tour_id = item.split("/")[4]
                title = get_value(soup=soup, selector=".wf-title", select_option=True)
                info = get_value(soup=soup, selector=".event-desc-inner a[href]")
                tag, stage, region = info[0], info[1], info[2]
                if len(info) > 3:
                    region = "all"
                
                if tag.lower() != "valorant champions tour":
                    logging.info(f"{title} not part of Valorant Champions Tour")
                    return None
                
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

                # if len(matches_page) > 0 and len(stats_page) > 0 and len(agents_page) > 0:
                #     logging.info(f"Matches page, stats page, and agents page url exists.")
                # else:
                #     raise ValueError(print("One or all of page url does not exists."))
                
                processed.add(item)

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"Scraping tournament information completed in {duration}s.")
            return list(results), list(matches_page), list(stats_page), list(agents_page)
        
        except Exception as e:
            logging.error(f"Error Occurs when running scrape_tournament_info: {e}")
            print(f"Error Occurs when running scrape_tournament_info: {e}")
    
    def run(self):
        start_time = datetime.now()
        
        tour_list = self.scrape_tournament_list()
        tour_info, matches_page, stats_page, agents_page = self.scrape_tournament_info(tour_list)
        tour_df = pd.DataFrame(tour_info, columns=["tour_id", "tour_name", "tour_tag", "tour_stage", "tour_region"])
        tour_df.to_csv(r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw")

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Tournament scraper pipeline completed in {duration}s")
        print(f"Tournament scraper pipeline completed in {duration}s")

        return matches_page, stats_page, agents_page