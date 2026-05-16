from datetime import datetime
from dataclasses import asdict
from constants.scraper_contants import *
from utils.scraper_utils import *
from entities.match_entities import Match
from logger import logging

class MatchesScraper:
    def __init__(self):
        pass

    def scrape_matches_list(self, page: list) -> list:
        processed = set()
        queue = list(page) if isinstance(page, (list, set)) else [page]
        print(f"Queue: {queue[:3]}")
        try:
            results = []
            start_time = datetime.now()
            for item in queue:
                tour_id, url = item[0], item[1]
                if url in processed:
                    logging.info(f"{url} has been processed.")
                    continue

                soup = get_soup(url=url)
                match_containers = soup.select(".wf-card a[href]")
                for match in match_containers:
                    href = match.get("href")
                    url = absolute(url=href)
                    results.add([tour_id, url])
                
                processed.add(url)
            
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_matches_list completed in {duration}s")
            return results

        except Exception as e:
            logging.error(f"Error occurs when running scrape_matches_list: {e}")
            print(f"Error occurs when running scrape_matches_list: {e}")
    
    def scrape_matches_info(self, page: list):
        processed = set()
        queue = list(page) if isinstance(page, (list, set)) else [page]
        print(f"Queue: {queue[:3]}")
        try:
            results = []
            start_time = datetime.now()
            for item in queue:
                tour_id, url = item[0], item[1]
                if url in processed:
                    logging.info(f"{url} has been processed.")
                    continue

                soup = get_soup(url=url)
                bracket = get_value(soup=soup, selector=".match-header-event-series", select_option=True)
                match_id = get_value(soup=soup, selector=".vm-stats-tabnav a", value="data-match-id", select_option=True)
                date = get_value(soup=soup, selector=".moment-tz-convert", value="data-utc-ts", select_option=True)
                patch_info = get_value(soup=soup, selector=".match-header-date", select_option=True)
                patch = patch_info.split("Patch")[-1].strip()
                
                home_href = get_value(soup=soup, selector=".match-header-link.wf-link-hover.mod-1", select_option=True)
                home_url = absolute(url=home_href)
                home_soup = get_soup(home_url)
                home_info = get_value(soup=home_soup, selector=".wf-title")
                home_name, home_alias = home_info[0], home_info[1]

                away_href = get_value(soup=soup, selector=".match-header-link.wf-link-hover.mod-2", select_option=True)
                away_url = absolute(url=away_href)
                away_soup = get_soup(away_url)
                away_info = get_value(soup=away_soup, selector=".wf-title")
                away_name, away_alias = away_info[0], away_info[1]

                bo_info = get_value(soup=soup, selector=".match-header-vs-note")[1]
                score_info = get_value(soup=soup, selector=".js-spoiler", select_option=True)
                home_score = score_info.split(":")[0].strip()
                away_score = score_info.split(":")[-1].strip()

                h2h = get_value(soup=soup, selector=".match-h2h-matches-score")
                home_h2h_win, home_h2h_score = 0, 0
                away_h2h_win, away_h2h_score = 0, 0
                for value in h2h:
                    score = value.split("\n")
                    home_h2h_score += int(score[0])
                    away_h2h_score += int(score[1])
                    if int(score[0]) > int(score[1]):
                        home_h2h_win += 1
                    else:
                        away_h2h_win += 1

                last_match = get_value(soup=soup, selector=".wf-card.mod-dark.match-histories", repeat=True)
                home_last_match = get_value(soup=last_match[0], selector=".match-histories-item.wf-module-item", value="class")
                away_last_match = get_value(soup=last_match[1], selector=".match-histories-item.wf-module-item", value="class")
                home_last_match_win, away_last_match = 0, 0
                for i in [home_last_match, away_last_match]:
                    for value in i:
                        if "mod-win" not in value:
                            continue
                        elif i == home_last_match:
                            home_last_match_win += 1
                            home_last_match_wr = home_last_match_win / 5
                        elif i == away_last_match:
                            away_last_match_win += 1
                            away_last_match_wr = away_last_match_win / 5

                map_selection = get_value(soup=soup, selector=".match-header-note", select_option=True)
                if map_selection is None:
                    match = Match(
                        tour_id=tour_id,
                        match_id=match_id,
                        date=date,
                        bracket=bracket,
                        patch=patch,

                        home_name=home_name,
                        home_alias=home_alias,
                        away_name=away_name,
                        away_alias=away_alias,

                        bo=bo_info,
                        home_score=home_score,
                        away_score=away_score,

                        home_h2h_win=home_h2h_win,
                        away_h2h_win=away_h2h_win,
                        home_h2h_score=home_h2h_score,
                        away_h2h_score=away_h2h_score,

                        home_last_5_wr=home_last_match_wr,
                        away_last_5_wr=away_last_match_wr
                    )
                    results.append(match)
                    continue

                home_map_picks, home_map_bans = [], []
                away_map_picks, away_map_bans = [], []
                decider_map = ""
                for map in map_selection:
                    map_split = map.strip().split(" ")
                    if map_split[0] == home_alias:
                        if map_split[1] == "pick":
                            home_map_picks.append(map_split[2].strip())
                        else:
                            home_map_bans.append(map_split[2].strip())
                    elif map_split[0] == away_alias:
                        if map_split[1] == "pick":
                            away_map_picks.append(map_split[2].strip())
                        else:
                            away_map_bans.append(map_split[2].strip())
                    else:
                        decider_map = map_split[0].strip()

                match = Match(
                    tour_id=tour_id,
                    match_id=match_id,
                    date=date,
                    bracket=bracket,
                    patch=patch,

                    home_name=home_name,
                    home_alias=home_alias,
                    away_name=away_name,
                    away_alias=away_alias,

                    bo=bo_info,
                    home_score=home_score,
                    away_score=away_score,

                    home_map_ban_1=home_map_bans[0],
                    home_map_ban_2=home_map_bans[1] if bo_info == "BO3" or bo_info == "BO1" else None,
                    home_map_ban_3=home_map_bans[2] if bo_info == "BO1" else None,
                    home_map_pick_1=home_map_picks[0] if bo_info == "BO3" or bo_info == "BO5" else None,
                    home_map_pick_2=home_map_picks[1] if bo_info == "BO5" else None,
                    away_map_ban_1=away_map_bans[0],
                    away_map_ban_2=away_map_bans[1] if bo_info == "BO3" or bo_info == "BO1" else None,
                    away_map_ban_3=away_map_bans[2] if bo_info == "BO1" else None,
                    away_map_pick_1=away_map_picks[0] if bo_info == "BO3" or bo_info == "BO5" else None,
                    away_map_pick_2=away_map_picks[1] if bo_info == "BO5" else None,
                    decider_map=decider_map,

                    home_h2h_win=home_h2h_win,
                    away_h2h_win=away_h2h_win,
                    home_h2h_score=home_h2h_score,
                    away_h2h_score=away_h2h_score,

                    home_last_5_wr=home_last_match_wr,
                    away_last_5_wr=away_last_match_wr
                )

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_matches_info completed in {duration}s")
            return results
        
        except Exception as e:
            logging.info(f"Error occurs when running scrape_matches_info: {e}")
            print(f"Error occurs when running scrape_matches_info: {e}")
    
    def run(self, page: list):
        start_time = datetime.now()

        logging.info("Initialize scrape_matches_list ...")
        matches_list = self.scrape_matches_list(page=page)
        logging.info("Initialize scrape_matches_info ...")
        matches_info = self.scrape_matches_info(page=matches_list)
        matches_df = pd.DataFrame([asdict(m) for m in matches_info])
        path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw\matches_raw.csv"
        matches_df.to_csv(path)
        logging.info(f"Data has been save in {path}")

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Matches scraper pipeline completed in {duration}s")
        print(f"Matches scraper pipeline completed in {duration}s")