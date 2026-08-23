from datetime import datetime
from constants.scraper_constants import *
from utils.scraper_utils import *
from entities.match_entities import *
from entities.map_veto_entities import *
from logger import logging

class MatchesScraper:
    def __init__(self):
        pass

    def scrape_map_veto(self, soup, match_id: str,):
        start_time = datetime.now()
        logging.info("Initialize scrape_map_veto ...")
        try:
            map_order_container = get_value(soup=soup, selector=".match-header-note", attr="text", multiple=True)
            if map_order_container[-1] is None:
                logging.info(f"Map selection not found.")
                return None

            map_order = map_order_container[-1].split(";")
            vetos = []
            for map in map_order:
                map_split = map.strip().split(" ")
                if map_split[1].strip() == "ban" or map_split[1].strip() == "pick":
                    veto = MapVeto(
                        match_id=match_id,
                        team_name=map_split[0],
                        action=map_split[1].lower(),
                        map_name=map_split[2]
                    )
                    vetos.append(veto)
                else:
                    veto = MapVeto(
                        match_id=match_id,
                        map_name=map_split[0]
                    )
                    logging.info(f"Found decider map: {map_split[0]}")
                    vetos.append(veto)

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_map_veto completed in {duration}s")
            return vetos

        except Exception as e:
            logging.error(f"Error occurs whe running scrape_map_veto: {e}")
            print(f"Error occurs whe running scrape_map_veto: {e}")

    def scrape_matches_list(self, match_page: list) -> list:
        start_time = datetime.now()
        processed = set()
        queue = list(match_page) if isinstance(match_page, (list, set)) else [match_page]
        print(f"Queue: {queue[0]}, ... {len(queue)} more.")
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
        print(f"Queue: {queue[0]}, ... {len(queue)} more.")
        try:
            matches_info = []
            map_veto = []
            tab_list = []
            progress = 0
            for i, item in enumerate(queue):
                tour_id, url = item[0], item[1]
                if url in processed:
                    logging.info(f"{url} has been processed.")
                    continue

                soup = get_soup(url=url)
                bracket = get_value(soup=soup, selector=".match-header-event-series", attr="text")
                if "showmatch" in bracket.lower():
                    continue
                match_id = get_value(soup=soup, selector=".vm-stats-tabnav a", attr="data-match-id")
                tab_elements = get_value(soup=soup, selector=".vm-stats-tabnav a", attr="href", multiple=True)
                tab_url = [absolute(url=i) for i in tab_elements]
                tab_list.append([match_id, sorted(tab_url)])
                date = get_value(soup=soup, selector=".moment-tz-convert", attr="data-utc-ts")
                date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                patch_info = get_value(soup=soup, selector=".match-header-date", attr="text")
                if "patch" in patch_info.lower():
                    patch = patch_info.split("Patch")[-1].strip()
                else:
                    patch = None

                logging.info(f"Found {match_id}, {bracket}, {date}, and {patch}.")
                
                home_href = get_value(soup=soup, selector=".match-header-link.wf-link-hover.mod-1", attr="href")
                home_url = absolute(url=home_href)
                home_soup = get_soup(url=home_url)
                home_info = get_value(soup=home_soup, selector=".wf-title", attr="text", multiple=True)
                home_name = home_alias = home_info[0]
                if len(home_info) > 1:
                    home_alias = home_info[1]

                away_href = get_value(soup=soup, selector=".match-header-link.wf-link-hover.mod-2", attr="href")
                away_url = absolute(url=away_href)
                away_soup = get_soup(url=away_url)
                away_info = get_value(soup=away_soup, selector=".wf-title", attr="text", multiple=True)
                away_name = away_alias = away_info[0]
                if len(away_info) > 1:
                    away_alias = away_info[1]

                logging.info(f"Found {home_name} as {home_alias} and {away_name} as {away_alias}.")

                bo_info = get_value(soup=soup, selector=".match-header-vs-note", attr="text", multiple=True)[-1]
                score_info = get_value(soup=soup, selector=".sp-hide span", attr="text", multiple=True)
                home_score = int(score_info[0])
                away_score = int(score_info[-1])
                
                logging.info(f"Found {bo_info} match score (home) {home_score} vs {away_score} (away).")

                h2h = get_value(soup=soup, selector=".match-h2h-matches-score", attr="text", multiple=True)
                home_h2h_win, home_h2h_score = 0, 0
                away_h2h_win, away_h2h_score = 0, 0
                for value in h2h:
                    home_h2h_score += int(value[0])
                    away_h2h_score += int(value[1])
                    if int(value[0]) > int(value[1]):
                        home_h2h_win += 1
                    else:
                        away_h2h_win += 1
                        
                logging.info(f"Head to Head score (home) {home_h2h_score}({home_h2h_win}) vs {away_h2h_score}({away_h2h_win}) (away).")

                last_match = get_value(soup=soup, selector=".wf-card.mod-dark.match-histories", multiple=True)
                if len(last_match) > 0:
                    home_last_match = get_value(soup=last_match[0], selector=".match-histories-item-result", attr="class", multiple=True)
                    away_last_match = get_value(soup=last_match[1], selector=".match-histories-item-result", attr="class", multiple=True)
                    home_n_last_match_win, away_n_last_match_win = 0, 0
                    home_n_last_match, away_n_last_match = len(home_last_match), len(away_last_match)
                    for value in home_last_match:
                        if "mod-win" in value:
                            home_n_last_match_win += 1
                        else:
                            continue
                    for value in away_last_match:
                        if "mod-win" in value:
                            away_n_last_match_win += 1
                        else:
                            continue
                        
                else:
                    home_n_last_match_win = home_n_last_match = away_n_last_match_win = away_n_last_match = 0
                    logging.info(f"{value} unindentified.")
                
                logging.info(f"n-last match win (home) {home_n_last_match_win} vs {away_n_last_match_win} (away).")

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

                vetos = self.scrape_map_veto(soup=soup, match_id=match_id)
                map_veto.extend(vetos)
                progress = get_progress(i, len(queue), progress)
                logging.info(f"Match info and map veto has been added.")
                processed.add(url)

            save_json(data=tab_list, filename="matches")
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_matches_info completed in {duration}s")
            return matches_info, map_veto, tab_list
        
        except Exception as e:
            logging.error(f"Error occurs when running scrape_matches_info: {e}")
            print(f"Error occurs when running scrape_matches_info: {e}")
    
    def run(self, match_pages):
        start_time = datetime.now()

        logging.info("Initialize scrape_matches_list ...")
        if not isinstance(match_pages, (set, list)):
            match_pages = load_json(match_pages)
        
        matches_list = self.scrape_matches_list(match_page=match_pages)
        logging.info("Initialize scrape_matches_info ...")
        matches_info, map_veto, tab_list = self.scrape_matches_info(match_list=matches_list)

        matches_df = pd.DataFrame([asdict(m) for m in matches_info])
        path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw\matches.parquet"
        matches_df.to_parquet(path, index=False)
        logging.info(f"Data has been save in {path}")

        map_veto_df = pd.DataFrame([asdict(m) for m in map_veto])
        path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw\map_vetos.parquet"
        map_veto_df.to_parquet(path, index=False)
        logging.info(f"Data has been save in {path}")

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Matches scraper pipeline completed in {duration}s")
        print("="*50)
        print(f"Matches scraper pipeline completed in {duration}s")
        print("="*50)
        return tab_list