from datetime import datetime
from constants.scraper_constants import *
from utils.scraper_utils import *
from entities.tour_entities import *
from entities.checkpoint_entities import *
from src.checkpoint.checkpoint import *
from logger import logging

class TournamentScraper:
    def __init__(
            self,
            base_url: str = BASE_URL,
            region_keyword: list = REGION_KEYWORD,
            stage_keyword: list = STAGE_KEYWORD,
            exist_tour_data: list = EXIST_TOUR_DATA
    ):
        self.base_url = base_url
        self.stage_keyword = stage_keyword
        self.region_keyword = region_keyword
        self.exist_tour_data = exist_tour_data

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
            elements = get_value(soup=soup, selector=".wf-card.mod-flex.event-item", multiple=True)
            for el in elements:
                href = el.get("href")
                tour_id = href.split("/")[2]
                url = absolute(url=href)
                status = get_value(soup=el, selector=".event-item-desc-item-status", attr="text")
                tour_list.add((status, tour_id, url))

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraping_tournament_list completed in {duration}s.")
            return list(tour_list)
        
        except Exception as e:
            logging.error(f"Error Occurs when running scrape_tournament_list: {e}")
            raise

    def scrape_tournament_info(self, tour_list: list, start_time: datetime) -> list:
        processed = set()
        queue = list(tour_list) if isinstance(tour_list, (set, list)) else [tour_list]
        print(f"Queue: {queue[0]}, ... {len(queue)} more." if len(queue) > 1 else f"Queue: {queue}")
        try:
            tour_info = []
            matches_page = set()
            progress = 0
            print(f"{progress}% of Completion")
            for i, item in enumerate(queue):
                logging.info(f"Check Runtime ...")
                end_time = datetime.now()

                if end_time - start_time >= MAX_RUNTIME:
                    save_pipeline(
                        status="in_progress",
                        module="tournaments"
                    )
                    logging.info(f"Timeout - scraper has been stopped.")
                    break

                logging.info("Check status ...")
                status, current_toud_id, url = item[0].lower(), item[1], item[2]

                checkpoint = Checkpoint(Path("data/checkpoint/tours.json"))
                checkpoint.load()
                
                if url in processed:
                    logging.info(f"{url} has been processed.")
                    continue

                if checkpoint.is_completed(current_toud_id):
                    logging.info(f"{current_toud_id} already exists.")
                    continue

                if current_toud_id in self.exist_tour_data["tour_id"]:

                    existing_status = (
                        self.exist_tour_data.loc[
                            self.exist_tour_data["tour_id"] == current_toud_id,
                            "tour_status"
                        ]
                        .iloc[0]
                        .lower()
                    )
                    if status == existing_status:
                        logging.info(f"Tournament {current_toud_id} already exists and status is unchanged ({status}).")
                        if status == "completed":
                            logging.info(f"Skip scraping.")
                            continue
                        logging.info(f"Start re-scraping ...")

                    elif status == "upcoming":
                        logging.info(f"Tournament {current_toud_id} already exists but is {status}. Skip scraping.")
                        continue

                    elif status != existing_status:
                        logging.info(
                            f"Tournament {current_toud_id} already exists but is status changed."
                            f"from {existing_status} to {status}."
                            f"Start re-scraping ..."
                        )

                    else:
                        raise ValueError(f"Status unrecognized. Found: {status.capitalize()}.")

                else:
                    if status == "upcoming":
                        logging.info(f"New tournament {current_toud_id} but tournament is {status}. Skip scraping.")
                        continue

                    elif status in ["ongoing", "completed"]:
                        logging.info(
                            f"New Tournament {current_toud_id} and tournament is {status}."
                            f"Start scraping ..."
                        )

                    else:
                        raise ValueError(
                            f"Status unrecognized. Found: {status.capitalize()}"
                        )
                
                soup = get_soup(url=url)
                tour_id = url.split("/")[4]
                tag = get_value(soup=soup, selector=".event-header-main-bc a[href]", attr="text")
                if not any(i in self.stage_keyword for i in tag.lower().split(" ")):
                    processed.add(url)
                    continue

                title = get_value(soup=soup, selector=".event-header-main-title", attr="text")
                title_split = title.split(":")[1].strip().split(" ", maxsplit=1) if ":" in title else title.split(" ", maxsplit=2)
                region = title_split[0] if len(title_split) == 2 else "World"
                stage =  title_split[1]

                logging.info(f"{title} is Exist. Tournament status: {status}.")
                
                tour = Tour(
                    tour_id=tour_id,
                    tour_name=title,
                    tour_tag=tag,
                    tour_stage=stage,
                    tour_region=region,
                    tour_status=status,
                    scraped_at= datetime.now()
                )
                tour_info.append(tour)
                
                if status.lower() in ["upcoming", "ongoing"]:
                    logging.info(f"{status} tournaments confirmed. Tournament must be completed to scrape matches list.")
                    processed.add(url)
                    continue

                elements = get_value(soup=soup, selector=".wf-nav a", attr="href", multiple=True)
                for el in elements:
                    content_url = absolute(url=el)
                    if "matches" in el:
                        content_url = content_url.replace(content_url[-4:], "all")
                        matches_page.add((tour_id, content_url))
                    else:
                        continue

                new_progress = get_progress(current_unit=i, total_unit=len(queue), current_progress=progress)
                progress += new_progress
                processed.add(url)

                checkpoint.mark_completed(tour_id)
                
                save_pipeline(
                    status="completed",
                    module="tournaments",
                    completed=True
                )
            
            save_file(data=matches_page, file_name="tours", format="json")
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraping_tournament_info completed in {duration}s.")
            return tour_info
        
        except Exception as e:
            logging.error(f"Error Occurs when running scrape_tournament_info: {e}")
            save_pipeline(
                status="failed",
                module="tournaments"
            )
            raise
    
    def run(self):
        start_time = datetime.now()
        
        logging.info("Initialize scrape_tournament_list ...")
        tour_list = self.scrape_tournament_list()
        logging.info("Initialize scrape_tournament_info ...")
        tour_info = self.scrape_tournament_info(tour_list=tour_list)
        tour_df = pd.DataFrame([asdict(t) for t in tour_info])
        save_file(data=tour_df, file_name="tours", format="parquet")

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Tournament scraper pipeline completed in {duration}s")
        print("="*50)
        print(f"Tournament scraper pipeline completed in {duration}s")
        print("="*50)