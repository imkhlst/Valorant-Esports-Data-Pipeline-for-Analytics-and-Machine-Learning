from datetime import datetime
from constants.scraper_constants import *
from utils.scraper_utils import *
from entities.match_entities import *
from logger import logging

class MatchesScraper:
    def __init__(self):
        pass

    def scrape_matches_list(self, match_page: list) -> list:
        start_time = datetime.now()
        processed = set()
        queue = list(match_page) if isinstance(match_page, (list, set)) else [match_page]
        print(f"Queue: {queue[:3]}")
        try:
            matches_list = []
            for item in queue:
                tour_id, url = item[0], item[1]
                if url in processed:
                    logging.info(f"{url} has been processed.")
                    continue

                soup = get_soup(url=url)
                match_href = get_value(soup=soup, selector=".wf-module-item.match-item", attr="href", multiple=True)
                for href in match_href:
                    match_url = absolute(url=href)
                    matches_list.append((tour_id, match_url))
                
                processed.add(url)
            
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_matches_list completed in {duration}s")
            return matches_list

        except Exception as e:
            logging.error(f"Error occurs when running scrape_matches_list: {e}")
            print(f"Error occurs when running scrape_matches_list: {e}")
    
    def scrape_matches_info(self, match_list: list):
        start_time = datetime.now()
        processed = set()
        queue = list(match_list) if isinstance(match_list, (set, list)) else [match_list]
        print(f"Queue: {queue[:3]}")
        try:
            matches_info = []
            tab_list = []
            for item in queue:
                tour_id, url = item[0], item[1]
                if url in processed:
                    logging.info(f"{url} has been processed.")
                    continue

                soup = get_soup(url=url)
                bracket = get_value(soup=soup, selector=".match-header-event-series", attr="text")
                match_id = get_value(soup=soup, selector=".vm-stats-tabnav a", attr="data-match-id")
                tab_elements = get_value(soup=soup, selector=".vm-stats-tabnav a", attr="href")
                tab_list.append([match_id, sorted[tab_elements]])
                date = get_value(soup=soup, selector=".moment-tz-convert", attr="data-utc-ts")
                date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                patch_info = get_value(soup=soup, selector=".match-header-date", attr="text")
                if "patch" in patch_info.lower():
                    patch = patch_info.split("Patch")[-1].strip()
                else:
                    patch = None
                
                home_href = get_value(soup=soup, selector=".match-header-link.wf-link-hover.mod-1", attr="href")
                home_url = absolute(url=home_href)
                home_soup = get_soup(url=home_url)
                home_info = get_value(soup=home_soup, selector=".wf-title", attr="text", multiple=True)
                home_name, home_alias = home_info[0], home_info[1]

                away_href = get_value(soup=soup, selector=".match-header-link.wf-link-hover.mod-2", attr="href")
                away_url = absolute(url=away_href)
                away_soup = get_soup(url=away_url)
                away_info = get_value(soup=away_soup, selector=".wf-title", attr="text", multiple=True)
                away_name, away_alias = away_info[0], away_info[1]

                bo_info = get_value(soup=soup, selector=".match-header-vs-note", multiple=True)[1]
                score_info = get_value(soup=soup, selector=".js-spoiler")
                home_score = int(score_info.split(":")[0].strip())
                away_score = int(score_info.split(":")[-1].strip())

                h2h = get_value(soup=soup, selector=".match-h2h-matches-score", attr="text", multiple=True)
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

                last_match = get_value(soup=soup, selector=".wf-card.mod-dark.match-histories")
                home_last_match = get_value(soup=last_match[0], selector=".match-histories-item.wf-module-item", attr="class")
                away_last_match = get_value(soup=last_match[1], selector=".match-histories-item.wf-module-item", attr="class")
                home_n_last_match_win, away_n_last_match_win = 0, 0
                for i in [home_last_match, away_last_match]:
                    for value in i:
                        if "mod-win" not in value:
                            continue
                        elif i == home_last_match:
                            home_n_last_match_win += 1
                            home_n_last_match = len(i)
                        elif i == away_last_match:
                            away_n_last_match_win += 1
                            away_n_last_match = len(i)
                        else:
                            logging.info(f"{value} unindentified.")

                map_selection_container = get_value(soup=soup, selector=".match-header-note", attr="text")
                if map_selection_container is None:
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

                        home_n_last_match=home_n_last_match,
                        home_n_last_win=home_n_last_match_win,
                        away_n_last_match=away_n_last_match,
                        away_n_last_win=away_n_last_match_win
                    )

                    matches_info.append(match)

                    processed.add(url)
                    continue

                # Need to seperate into different dataclass next update
                map_selection = map_selection_container.split(";").strip()
                home_map_picks, home_map_bans = [], []
                away_map_picks, away_map_bans = [], []
                decider_map = ""
                for map in map_selection:
                    map_split = map.split(" ").strip()
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

                    home_h2h_win=home_h2h_win,
                    away_h2h_win=away_h2h_win,
                    home_h2h_score=home_h2h_score,
                    away_h2h_score=away_h2h_score,

                    home_n_last_match=home_n_last_match,
                    home_n_last_win=home_n_last_match_win,
                    away_n_last_match=away_n_last_match,
                    away_n_last_win=away_n_last_match_win,

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
                    decider_map=decider_map
                )

                matches_info.append(match)

                processed.add(url)

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_matches_info completed in {duration}s")
            return matches_info, tab_list
        
        except Exception as e:
            logging.error(f"Error occurs when running scrape_matches_info: {e}")
            print(f"Error occurs when running scrape_matches_info: {e}")
    
    def run(self, match_pages: list):
        start_time = datetime.now()

        logging.info("Initialize scrape_matches_list ...")
        matches_list = self.scrape_matches_list(match_page=match_pages)
        logging.info("Initialize scrape_matches_info ...")
        matches_info, tab_list = self.scrape_matches_info(match_list=matches_list)
        matches_df = pd.DataFrame([asdict(m) for m in matches_info])
        path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw\matches_raw.csv"
        matches_df.to_csv(path)
        logging.info(f"Data has been save in {path}")

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Matches scraper pipeline completed in {duration}s")
        print("="*50)
        print(f"Matches scraper pipeline completed in {duration}s")
        print("="*50)
        return tab_list