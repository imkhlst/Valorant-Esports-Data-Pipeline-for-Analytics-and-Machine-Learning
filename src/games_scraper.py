from utils.scraper_utils import *
from entities.game_entities import *
from entities.player_stats_entities import *
from logger import logging

class GamesScraper:
    def __init__(self):
        pass

    def scrape_player_stat(self, game_id: str,  soup: str):
        start_time = datetime.now()
        logging.info("Initialize scrape_player_info ...")
        try:
            stats_info = []
            tables = get_value(soup=soup, selector=".ovw-scroll-wrap", multiple=True)
            for table in tables:
                flags = get_value(soup=table, selector=".flag", attr="title", multiple=True)
                names = get_value(soup=table, selector=".ovw-player-name", attr="text", multiple=True)
                team_aliases = get_value(soup=table, selector=".ovw-player-tag", attr="text", multiple=True)
                agents = get_value(soup=table, selector=".stats-sq.mod-agent.small img", attr="title", multiple=True)
                logging.info(f"Found player info: {names[0]}, {flags[0]}, {team_aliases[0]}, {agents[0]}")
                for mod in ["mod-both", "mod-t", "mod-t"]:
                    stats_list = get_value(soup=table, selector=f".side.{mod}", attr="text", multiple=True)
                    for i, name in enumerate(names):
                        stats = PlayerStats(
                            game_id=game_id,
                            name=name,
                            team_alias=team_aliases[i],
                            nationality=flags[i],
                            agent=agents[i],
                            mod="atk" if mod == "mod-t" else "def" if mod == "mod_ct" else "avg",
                            r=float(stats_list[0 + (12 * (i + 1))]),
                            acs=int(stats_list[1 + (12 * (i + 1))]),
                            k=int(stats_list[2 + (12 * (i + 1))]),
                            d=int(stats_list[3 + (12 * (i + 1))]),
                            a=int(stats_list[4 + (12 * (i + 1))]),
                            kd=int(stats_list[5 + (12 * (i + 1))]),
                            kast=int(stats_list[6 + (12 * (i + 1))]),
                            adr=int(stats_list[7 + (12 * (i + 1))]),
                            hs=int(stats_list[8 + (12 * (i + 1))]),
                            fk=int(stats_list[9 + (12 * (i + 1))]),
                            fd=int(stats_list[10 + (12 * (i + 1))]),
                            fkdf=int(stats_list[11 + (12 * (i + 1))]),
                        )
                        stats_info.append(stats)
                
            logging.info(f"Stats info has been added.")
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_player_info completed in {duration}s")
            return stats_info
        
        except Exception as e:
            logging.error(f"Error occurs whe running scrape_player_info: {e}")
            print(f"Error occurs whe running scrape_player_info: {e}")
            
    def scrape_game_overview(self, overview_url: str) -> list:
        start_time = datetime.now()
        logging.info(f"Initialize scraper_game_overview ...")
        try:
            game_overview = []
            player_info = []
            soup = get_soup(url=overview_url)
            games = get_value(soup=soup, selector=".vm-stats-game", multiple=True)
            for game in games:
                game_id = game.get("data-game-id")
                if game_id == "all":
                    continue

                game_score = get_value(soup=game, selector=".score", attr="text", multiple=True)
                home_score, away_score = int(game_score[0]), int(game_score[1])
                map_duration_container = get_value(soup=game, selector=".map", attr="text")
                if "PICK" in map_duration_container:
                    map_name = map_duration_container.split("PICK")[0]
                    game_duration = map_duration_container.split("PICK")[1] if map_duration_container.split("PICK")[1] != "-" else None
                
                else:
                    map_name = map_duration_container.replace("-", "") if map_duration_container[-1] == "-" else re.split("\d+", map_duration_container)[0]
                    game_duration = map_duration_container.replace(map_name, "") if ":" in map_duration_container else None

                home_atk_score, away_atk_score = None, None
                atk_score = get_value(soup=game, selector=".mod-t", attr="text", multiple=True)
                if atk_score:
                    home_atk_score, away_atk_score = int(atk_score[0]) if atk_score[0] != "" else home_atk_score, int(atk_score[1]) if atk_score[1] != "" else away_atk_score

                home_def_score, away_def_score = None, None
                def_score = get_value(soup=game, selector=".mod-ct", attr="text", multiple=True)
                if def_score:
                    home_def_score, away_def_score = int(def_score[0]) if def_score[0] != "" else home_def_score, int(def_score[1]) if def_score[1] != "" else away_def_score
                
                home_ot_score, away_ot_score = None, None
                ot_score = get_value(soup=game, selector=".mod-ot", attr="text", multiple=True)
                if ot_score:
                    home_ot_score, away_ot_score = int(ot_score[0]) if ot_score[0] != "" else home_ot_score, int(ot_score[1]) if ot_score[1] != "" else away_ot_score
                    if home_ot_score or away_ot_score is not None:
                        home_atk, home_def, away_atk, away_def = 0, 0, 0, 0
                        ot_round_container = get_value(soup=game, selector=".vlr-rounds-row", multiple=True)[-1]
                        for i, ot_round in enumerate(get_value(soup=ot_round_container, selector=".rnd-sq.mod-win", multiple=True)):
                            if "mod-ct" in get_value(soup=game, selector="span", attr="class"):
                                home_def = home_def + 1 if "mod-ct" in ot_round.get("class") and (i + 1) % 2 == 1 else home_def + 0
                                home_atk = home_atk + 1 if "mod-t" in ot_round.get("class") and (i + 1) % 2 == 0 else home_atk + 0
                                away_atk = away_atk + 1 if "mod-t" in ot_round.get("class") and (i + 1) % 2 == 1 else away_atk + 0
                                away_def = away_def + 1 if "mod-ct" in ot_round.get("class") and (i + 1) % 2 == 0 else away_def + 0
                            else:
                                home_def = home_def + 1 if "mod-ct" in ot_round.get("class") and (i + 1) % 2 == 0 else home_def + 0
                                home_atk = home_atk + 1 if "mod-t" in ot_round.get("class") and (i + 1) % 2 == 1 else home_atk + 0
                                away_atk = away_atk + 1 if "mod-t" in ot_round.get("class") and (i + 1) % 2 == 0 else away_atk + 0
                                away_def = away_def + 1 if "mod-ct" in ot_round.get("class") and (i + 1) % 2 == 1 else away_def + 0

                        home_atk_score += home_atk
                        home_def_score += home_def
                        away_atk_score += away_atk
                        away_def_score += away_def
                
                logging.info(f"Found {game_id}, on {map_name} - {game_duration}.")
                logging.info(f"Found game score home ({home_atk_score}/{home_def_score}/{home_ot_score}) {home_score} vs {away_score} ({away_atk_score}/{away_def_score}/{away_ot_score}) away.")
                game_overview.append([game_id, map_name, game_duration, home_score, away_score, home_atk_score, away_atk_score, home_def_score, away_def_score, home_ot_score, away_ot_score])

                stats_info = self.scrape_player_stat(game_id=game_id, soup=game)
                player_info.extend(stats_info)

            logging.info(f"Game overview and player info has been added.")
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_game_overview completed in {duration}s")
            return game_overview, player_info
        
        except Exception as e:
            logging.info(f"Error occurs when running scrape_game_overview: {e}")
            print(f"Error occurs when running scrape_game_overview: {e}")
    
    def scrape_game_economy(self, econ_url: str) -> list:
        start_time = datetime.now()
        logging.info(f"Initialize scraper_game_economy ...")
        try:
            home_econ, away_econ = [], []
            soup = get_soup(url=econ_url)
            games = get_value(soup=soup, selector=".vm-stats-game", multiple=True)
            for game in games:
                if game.get("data-game-id") == "all":
                    continue

                table = get_value(soup=game, selector=".wf-table-inset.mod-econ")
                if not table:
                    home_econ.append(None)
                    away_econ.append(None)
                    continue

                stats = get_value(soup=table, selector=".stats-sq", attr="text", multiple=True)
                cleaned_stat = []
                for stat in stats:
                    if "(" in stat:
                        stat_split = stat.split("(")
                        round = int(stat_split[0])
                        round_win = int(stat_split[1].removesuffix(")"))
                        cleaned_stat.append(round)
                        cleaned_stat.append(round_win)
                    else:
                        cleaned_stat.append(stat)

                home_stats, away_stats= cleaned_stat[:9], cleaned_stat[9:]
                home_econ.append(home_stats)
                away_econ.append(away_stats)
            
            logging.info(f"Home econ and away econ has been added.")
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_game_economy completed in {duration}s")
            return home_econ, away_econ
        
        except Exception as e:
            logging.info(f"Error occurs when running scrape_game_economy: {e}")
            print(f"Error occurs when running scrape_game_economy: {e}")

    def scrape_game_info(self, tab_list: list):
        start_time = datetime.now()
        processed = set()
        queue = list(tab_list) if isinstance(tab_list, (set, list)) else [tab_list]
        print(f"Queue: {queue[0]}, ... {len(queue)} more.")
        try:
            game_info = []
            player_stats = []
            for item in queue:
                match_id, tabs = item[0], item[1]
                econ_tab, overview_tab = tabs[0], tabs[1]
                if overview_tab in processed:
                    logging.info(f"{overview_tab} already processed.")
                    continue

                game_overview, player_info = self.scrape_game_overview(overview_url=overview_tab)
                player_stats.extend(player_info)

                if econ_tab in processed:
                    logging.info(f"{econ_tab} already processed.")
                    continue

                home_econ, away_econ = self.scrape_game_econ(econ_url=econ_tab)
                for i, item in enumerate(game_overview):
                    games = Game(
                        match_id=match_id,
                        game_id=item[0],
                        game_map=item[1],
                        game_duration=item[2],
                        home_score=item[3],
                        away_score=item[4],
                        home_atk_score=item[5],
                        away_atk_score=item[6],
                        home_def_score=item[7],
                        away_def_score=item[8],
                        home_ot_score=item[9],
                        away_ot_score=item[10],
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
                processed.add(overview_tab)
                processed.add(econ_tab)

            logging.info(f"Game info and player stats has been added.")
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraper_game_info completed in {duration}s")
            return game_info, player_stats
        
        except Exception as e:
            logging.info(f"Error occurs when running scrape_game_info: {e}")
            print(f"Error occurs when running scrape_game_info: {e}")

    def run(self, tab_list):
        start_time = datetime.now()

        logging.info(f"Initialize scraper_game_info ...")
        if isinstance(tab_list, str):
            tab_list = load_json(tab_list)
        
        game_info, player_stats = self.scrape_game_info(tab_list=tab_list)
        games_df = pd.DataFrame([asdict(g) for g in game_info])
        path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw\games_raw.csv"
        games_df.to_csv(path, index=False)
        logging.info(f"Data has been save in {path}")

        players_df = pd.DataFrame([asdict(p) for p in player_stats])
        path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw\players_raw.csv"
        players_df.to_csv(path, index=False)
        logging.info(f"Data has been save in {path}")

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Games scraper pipeline completed in {duration}s")
        print("="*50)
        print(f"Games scraper pipeline completed in {duration}s")
        print("="*50)