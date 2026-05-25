from utils.scraper_utils import *
from entities.game_entities import *
from logger import logging

class GamesScraper:
    def __init__(self):
        pass

    def scraper_game_overview(self, overview_url: str) -> list:
        logging.info(f"Initialize scraper_game_overview ...")
        try:
            game_overview = []
            soup = get_soup(url=overview_url)
            elements = get_value(soup=soup, selector=".vm-stats-gamesnav-item", attr="data-game-id", multiple=True)
            game_id = sorted(elements)
            games = get_value(soup=soup, selector=".vm-stats-game-header", multiple=True)
            for i, game in enumerate(games):
                game_score = get_value(soup=game, selector=".score", attr="text", multiple=True)
                home_score, away_score = int(game_score[0]), int(game_score[1])
                map_duration_container = get_value(soup=game, selector=".map", attr="text")
                if "PICK" in map_duration_container:
                    map_duration = map_duration_container.split("PICK")
                    map_name = map_duration[0]
                    game_duration = map_duration[1]
                
                else:
                    map_name = re.split("\d+", map_duration_container)[0]
                    game_duration = map_duration_container.replace(map_name, "")

                home_att_score, away_att_score = None, None
                att_score = get_value(soup=game, selector=".mod-t", attr="text", multiple=True)
                if att_score:
                    home_att_score, away_att_score = int(att_score[0]), int(att_score[1])

                home_def_score, away_def_score = None, None
                def_score = get_value(soup=game, selector=".mod-ct", attr="text", multiple=True)
                if def_score:
                    home_def_score, away_def_score = int(def_score[0]), int(def_score[1])
                
                logging.info(f"Found {game_id[i]}, on {map_name} - {game_duration}.")
                logging.info(f"Found game score home ({home_att_score}/{home_def_score}) {home_score} vs {away_score} ({away_att_score}/{away_def_score}) away.")
                game_overview.append([game_id[i], map_name, game_duration, home_score, away_score, home_att_score, away_att_score, home_def_score, away_def_score])

            return game_overview, soup
        
        except Exception as e:
            logging.info(f"Error occurs when running scraper_game_overview: {e}")
            print(f"Error occurs when running scraper_game_overview: {e}")
    
    def scraper_game_econ(self, econ_url: str) -> list:
        logging.info(f"Initialize scraper_game_econ ...")
        try:
            home_econ, away_econ = [], []
            soup = get_soup(url=econ_url)
            games = get_value(soup=soup, selector=".vm-stats-game", multiple=True)
            for game in games:
                if game.get("data-game-id") == "all":
                    continue

                table = get_value(soup=game, selector=".wf-table-inset.mod-econ")
                if not table:
                    home_stats, away_stats = [], []
                    home_econ.append(home_stats)
                    away_econ.append(away_stats)
                    continue

                stats = get_value(soup=table, selector=".stats-sq", attr="text", multiple=True)
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

            return home_econ, away_econ
        
        except Exception as e:
            logging.info(f"Error occurs when running scraper_game_overview: {e}")
            print(f"Error occurs when running scraper_game_overview: {e}")

    def scraper_game_info(self, tab_list: list):
        start_time = datetime.now()
        processed = set()
        queue = list(tab_list) if isinstance(tab_list, (set, list)) else [tab_list]
        print(f"Queue: {queue[:2]}, ... , {queue[-1]}")
        try:
            game_info = []
            soup_list = []
            for item in queue:
                match_id, tabs = item[0], item[1]
                econ_tab, overview_tab = tabs[0], tabs[1]
                if overview_tab in processed:
                    logging.info(f"{overview_tab} already processed.")
                    continue

                game_overview, soup = self.scraper_game_overview(overview_url=overview_tab)

                if econ_tab in processed:
                    logging.info(f"{econ_tab} already processed.")
                    continue

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
                        home_pstl_win=home_econ[i][0] if home_econ[i] else None,
                        away_pstl_win=away_econ[i][0] if away_econ[i] else None,
                        home_eco_round=home_econ[i][1] if home_econ[i] else None,
                        home_eco_win=home_econ[i][2] if away_econ[i] else None,
                        away_eco_round=away_econ[i][1] if home_econ[i] else None,
                        away_eco_win=away_econ[i][2] if away_econ[i] else None,
                        home_semi_eco_round=home_econ[i][3] if home_econ[i] else None,
                        home_semi_eco_win=home_econ[i][4] if home_econ[i] else None,
                        away_semi_eco_round=away_econ[i][3] if away_econ[i] else None,
                        away_semi_eco_win=away_econ[i][4] if away_econ[i] else None,
                        home_semi_buy_round=home_econ[i][5] if home_econ[i] else None,
                        home_semi_buy_win=home_econ[i][6] if home_econ[i] else None,
                        away_semi_buy_round=away_econ[i][5] if away_econ[i] else None,
                        away_semi_buy_win=away_econ[i][6] if away_econ[i] else None,
                        home_full_buy_round=home_econ[i][7] if home_econ[i] else None,
                        home_full_buy_win=home_econ[i][8] if home_econ[i] else None,
                        away_full_buy_round=away_econ[i][7] if away_econ[i] else None,
                        away_full_buy_win=away_econ[i][8] if away_econ[i] else None
                    )
                    game_info.append(games)
                soup_list.append(soup)
                processed.add(overview_tab)
                processed.add(econ_tab)

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraper_game_info completed in {duration}s")
            return game_info, soup_list
        
        except Exception as e:
            logging.info(f"Error occurs when running scraper_game_info: {e}")
            print(f"Error occurs when running scraper_game_info: {e}")

    def run(self, tab_list):
        start_time = datetime.now()

        logging.info(f"Initialize scraper_game_info ...")
        if isinstance(tab_list, str):
            tab_list = load_json(tab_list)
        
        game_info, soup_list = self.scraper_game_info(tab_list=tab_list)
        games_df = pd.DataFrame([asdict(g) for g in game_info])
        path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw\games_raw.csv"
        games_df.to_csv(path, index=False)
        logging.info(f"Data has been save in {path}")

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Games scraper pipeline completed in {duration}s")
        print("="*50)
        print(f"Games scraper pipeline completed in {duration}s")
        print("="*50)
        return soup_list