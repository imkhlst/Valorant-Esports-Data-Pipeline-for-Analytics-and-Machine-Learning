from utils.scraper_utils import *
from entities.game_entities import *
from logger import logging

class GamesScraper:
    def __init__(self):
        pass

    def scraper_game_overview(self, overview_url: str) -> list:
        start_time = datetime.now()
        logging.info(f"Initialize scraper_game_overview ...")
        try:
            game_overview = []
            soup = get_soup(url=overview_url)
            elements = get_value(soup=soup, selector="vm-stats-gamesnav-item", attr="data-game-id", multiple=True)
            game_id = sorted(elements)
            games = get_value(soup=soup, selector=".vm-stats-game-header", multiple=True)
            for i, game in enumerate(games):
                game_score = get_value(soup=game, selector=".score", attr="text", multiple=True)
                home_score, away_score = int(game_score[0]), int(game_score[1])
                map_duration_container = get_value(soup=game, selector=".map", attr="text", multiple=True)
                map_duration = map_duration_container.split("PICK")
                map_name = map_duration[0]
                game_duration = datetime.strptime(map_duration[1], format="%H:%M:%S")
                att_score = get_value(soup=game, selector=".mod-t", attr="text", multiple=True)
                home_att_score, away_att_score = int(att_score[0]), int(att_score[1])
                def_score = get_value(soup=game, selector=".mode-ct", attr="text", multiple=True)
                home_def_score, away_def_score = int(def_score[0]), int(def_score[1])
                game_overview.append([game_id, map_name, game_duration, home_score, away_score, home_att_score, away_att_score, home_def_score, away_def_score])
            
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraper_game_overview completed in {duration}s")
            return game_overview, soup
        
        except Exception as e:
            logging.info(f"Error occurs when running scraper_game_overview: {e}")
            print(f"Error occurs when running scraper_game_overview: {e}")
    
    def scraper_game_econ(self, econ_url: str) -> list:
        start_time = datetime.now()
        logging.info(f"Initialize scraper_game_econ ...")
        try:
            home_econ, away_econ = [], []
            soup = get_soup(url=econ_url)
            games = get_value(soup=soup, selector=".wf-table-inset.mod-econ", multiple=True)
            for i, game in enumerate(games):
                if len(games) == i + 1:
                    break
                stats = get_value(soup=game, selector=".stats-sq", attr="text", multiple=True)
                if stats == []:
                    continue
                cleaned_stat = []
                for stat in stats:
                    if "(" in stat:
                        stat_split = stat.split("(")
                        round = int(stat_split[0])
                        round_win = int(stat_split[1].split(")")[0])
                        cleaned_stat.append(round)
                        cleaned_stat.append(round_win)
                    else:
                        cleaned_stat.append(stat)

                home_stats, away_stats= cleaned_stat[:9], cleaned_stat[9:]
                home_econ.append(home_stats)
                away_econ.append(away_stats)
            
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraper_game_econ completed in {duration}s")
            return home_econ, away_econ
        
        except Exception as e:
            logging.info(f"Error occurs when running scraper_game_overview: {e}")
            print(f"Error occurs when running scraper_game_overview: {e}")

    def scraper_game_info(self, tab_list: list):
        start_time = datetime.now()
        processed = set()
        queue = list(tab_list) if isinstance(tab_list, (set, list)) else [tab_list]
        print(f"Queue: {queue[:3]}")
        try:
            game_info = []
            soup_list = []
            for item in queue:
                if item in processed:
                    logging.info(f"{item} already processed.")
                    continue

                match_id, tabs = item[0], item[1]
                econ_tab, overview_tab = tabs[0], tabs[1]
                game_overview, soup = self.scraper_game_overview(overview_url=overview_tab)
                home_econ, away_econ = self.scraper_game_econ(econ_url=econ_tab)
                for i, item in enumerate(game_overview):
                    games = Game(
                        match_id=match_id,
                        game_id=item[0],
                        game_map=item[1],
                        game_duration=item[2],
                        home_score=item[3],
                        away_score=item[4],
                        home_att_score=item[5],
                        away_att_score=item[6],
                        home_def_score=item[7],
                        away_def_score=item[8],
                        home_pstl_win=home_econ[i][0],
                        away_pstl_win=away_econ[i][0],
                        home_eco_round=home_econ[i][1],
                        home_eco_win=home_econ[i][2],
                        away_eco_round=away_econ[i][1],
                        away_eco_win=away_econ[i][2],
                        home_semi_eco_round=home_econ[i][3],
                        home_semi_eco_win=home_econ[i][4],
                        away_semi_eco_round=away_econ[i][3],
                        away_semi_eco_win=away_econ[i][4],
                        home_semi_buy_round=home_econ[i][5],
                        home_semi_buy_win=home_econ[i][6],
                        away_semi_buy_round=away_econ[i][5],
                        away_semi_buy_win=away_econ[i][6],
                        home_full_buy_round=home_econ[i][7],
                        home_full_buy_win=home_econ[i][8],
                        away_full_buy_round=away_econ[i][7],
                        away_full_buy_win=away_econ[i][8]
                    )
                    game_info.append(games)
                soup_list.append(soup)
                processed.add(item)

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraper_game_info completed in {duration}s")
            return game_info, soup_list
        
        except Exception as e:
            logging.info(f"Error occurs when running scraper_game_info: {e}")
            print(f"Error occurs when running scraper_game_info: {e}")

    def run(self, tab_list: list):
        start_time = datetime.now()

        logging.info(f"Initialize scraper_game_info ...")
        game_info, soup_list = self.scraper_game_info(tab_list=tab_list)
        games_df = pd.DataFrame([asdict(g) for g in game_info])
        path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw\games_raw.csv"
        games_df.to_csv(path)
        logging.info(f"Data has been save in {path}")

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Games scraper pipeline completed in {duration}s")
        print("="*50)
        print(f"Games scraper pipeline completed in {duration}s")
        print("="*50)
        return soup_list