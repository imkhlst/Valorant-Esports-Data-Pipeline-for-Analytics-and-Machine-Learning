from utils.scraper_utils import *
from entities.game_entities import *
from entities.player_stats_entities import *
from logger import logging

class GamesScraper:
    def __init__(self):
        pass

    def scrape_player_stat(self, game_id: str,  soup: str):
        start_time = datetime.now()
        logging.info("Initialize scrape_player_stat ...")
        try:
            stats_info = []
            tables = get_value(soup=soup, selector=".ovw-scroll-wrap", multiple=True)
            for table in tables:
                flags = get_value(soup=table, selector=".flag", attr="title", multiple=True)
                names = get_value(soup=table, selector=".ovw-player-name", attr="text", multiple=True)
                team_aliases = get_value(soup=table, selector=".ovw-player-tag", attr="text", multiple=True)
                agents = get_value(soup=table, selector=".stats-sq.mod-agent.small img", attr="title", multiple=True)
                for mod in ["mod-both", "mod-ct", "mod-t"]:
                    stats_list = get_value(soup=table, selector=f".side.{mod}", attr="text", multiple=True)
                    if len(stats_list) < 60:
                        stats_list.extend([""] * (60 - len(stats_list)))
                    for i, name in enumerate(names):
                        stats = PlayerStats(
                            game_id=game_id,
                            name=name,
                            team_alias=team_aliases[i],
                            nationality=flags[i],
                            agent=agents[i],
                            mod="atk" if mod == "mod-t" else "def" if mod == "mod-ct" else "avg",
                            r=float(stats_list[0 + ((len(stats_list) // 5) * i)]) if stats_list[0 + ((len(stats_list) // 5) * i)] != "" else None,
                            acs=int(stats_list[1 + ((len(stats_list) // 5) * i)].replace(",", "")) if stats_list[1 + ((len(stats_list) // 5) * i)] != "" else None,
                            k=int(stats_list[2 + ((len(stats_list) // 5) * i)]) if stats_list[2 + ((len(stats_list) // 5) * i)] != "" else None,
                            d=int(stats_list[3 + ((len(stats_list) // 5) * i)]) if stats_list[3 + ((len(stats_list) // 5) * i)] != "" else None,
                            a=int(stats_list[4 + ((len(stats_list) // 5) * i)]) if stats_list[4 + ((len(stats_list) // 5) * i)] != "" else None,
                            kd=int(stats_list[5 + ((len(stats_list) // 5) * i)]) if stats_list[5 + ((len(stats_list) // 5) * i)] != "" else None,
                            kast=int(stats_list[6 + ((len(stats_list) // 5) * i)].replace("%", "")) if stats_list[6 + ((len(stats_list) // 5) * i)] != "" else None,
                            adr=int(stats_list[7 + ((len(stats_list) // 5) * i)].replace(",", "")) if stats_list[7 + ((len(stats_list) // 5) * i)] != "" else None,
                            hs=int(stats_list[8 + ((len(stats_list) // 5) * i)].replace("%", "")) if stats_list[8 + ((len(stats_list) // 5) * i)] != "" else None,
                            fk=int(stats_list[9 + ((len(stats_list) // 5) * i)]) if stats_list[9 + ((len(stats_list) // 5) * i)] != "" else None,
                            fd=int(stats_list[10 + ((len(stats_list) // 5) * i)]) if stats_list[10 + ((len(stats_list) // 5) * i)] != "" else None,
                            fkfd=int(stats_list[11 + ((len(stats_list) // 5) * i)]) if stats_list[11 + ((len(stats_list) // 5) * i)] != "" else None
                        )
                        stats_info.append(stats)
                    logging.info(f"Found player info: {names[0]}, {flags[0]}, {team_aliases[0]}, {agents[0]}, {mod}")
                
            logging.info(f"Stats info has been added.")
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_player_stat completed in {duration}s")
            return stats_info
        
        except Exception as e:
            logging.error(f"Error occurs whe running scrape_player_stat: {e}")
            print(f"Error occurs whe running scrape_player_stat: {e}")
            
    def scrape_game_overview(self, match_id: str, overview_url: str) -> list:
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
                overview = GameOverview(
                    match_id=match_id,
                    game_id=game_id,
                    game_map=map_name,
                    game_duration=game_duration,
                    home_score=home_score,
                    away_score=away_score,
                    home_atk_score=home_atk_score,
                    away_atk_score=away_atk_score,
                    home_def_score=home_def_score,
                    away_def_score=away_def_score,
                    home_ot_score=home_ot_score,
                    away_ot_score=away_ot_score
                )
                game_overview.append(overview)

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
    
    def scrape_game_economy(self, match_id: str, econ_url: str) -> list:
        start_time = datetime.now()
        logging.info(f"Initialize scraper_game_economy ...")
        try:
            game_econ = []
            soup = get_soup(url=econ_url)
            games = get_value(soup=soup, selector=".vm-stats-game", multiple=True)
            for game in games:
                game_id = game.get("data-game-id")
                if game_id == "all":
                    continue
                
                table = get_value(soup=game, selector=".wf-table-inset.mod-econ")
                if not table:
                    econ = GameEconomy(
                        match_id=match_id,
                        game_id=game_id
                    )
                    game_econ.append(econ)
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
                econ = GameEconomy(
                    match_id=match_id,
                    game_id=game_id,
                    home_pstl_win=int(home_stats[0]),
                    away_pstl_win=int(away_stats[0]),
                    home_eco_round=int(home_stats[1]),
                    away_eco_round=int(away_stats[1]),
                    home_eco_win=int(home_stats[2]),
                    away_eco_win=int(away_stats[2]),
                    home_semi_eco_round=int(home_stats[3]),
                    away_semi_eco_round=int(away_stats[3]),
                    home_semi_eco_win=int(home_stats[4]),
                    away_semi_eco_win=int(away_stats[4]),
                    home_semi_buy_round=int(home_stats[5]),
                    away_semi_buy_round=int(away_stats[5]),
                    home_semi_buy_win=int(home_stats[6]),
                    away_semi_buy_win=int(away_stats[6]),
                    home_full_buy_round=int(home_stats[7]),
                    away_full_buy_round=int(away_stats[7]),
                    home_full_buy_win=int(home_stats[8]),
                    away_full_buy_win=int(away_stats[8])
                )
                game_econ.append(econ)
            
            logging.info(f"Home econ and away econ has been added.")
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_game_economy completed in {duration}s")
            return game_econ
        
        except Exception as e:
            logging.info(f"Error occurs when running scrape_game_economy: {e}")
            print(f"Error occurs when running scrape_game_economy: {e}")

    def scrape_game_info(self, tab_list: list):
        start_time = datetime.now()
        processed = set()
        queue = list(tab_list) if isinstance(tab_list, (set, list)) else [tab_list]
        print(f"Queue: {queue[0]}, ... {len(queue)} more.")
        try:
            game_overview = []
            game_economy = []
            player_stats = []
            progress = 0
            for i, item in enumerate(queue):
                match_id, tabs = item[0], item[1]
                econ_tab, overview_tab = tabs[0], tabs[1]
                if overview_tab in processed:
                    logging.info(f"{overview_tab} already processed.")
                    continue

                overview, player_info = self.scrape_game_overview(match_id=match_id, overview_url=overview_tab)
                player_stats.extend(player_info)

                if econ_tab in processed:
                    logging.info(f"{econ_tab} already processed.")
                    continue

                game_econ = self.scrape_game_economy(match_id=match_id, econ_url=econ_tab)
                game_overview.extend(overview)
                game_economy.extend(game_econ)
                
                progress = get_progress(i, len(queue), progress)
                processed.add(overview_tab)
                processed.add(econ_tab)

            logging.info(f"Game info and player stats has been added.")
            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scraper_game_info completed in {duration}s")
            return game_overview, game_economy, player_stats
        
        except Exception as e:
            logging.info(f"Error occurs when running scrape_game_info: {e}")
            print(f"Error occurs when running scrape_game_info: {e}")

    def run(self, tab_list):
        start_time = datetime.now()

        logging.info(f"Initialize scraper_game_info ...")
        if isinstance(tab_list, str):
            tab_list = load_json(tab_list)
        
        game_overview, game_economy, player_stats = self.scrape_game_info(tab_list=tab_list)
        games_overview_df = pd.DataFrame([asdict(o) for o in game_overview])
        save_file(data=games_overview_df, file_name="games_overview", format="parquet")

        games_economy_df = pd.DataFrame([asdict(o) for o in game_economy])
        save_file(data=games_economy_df, file_name="games_economy", format="parquet")

        players_df = pd.DataFrame([asdict(p) for p in player_stats])
        save_file(data=players_df, file_name="players", format="parquet")

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Games scraper pipeline completed in {duration}s")
        print("="*50)
        print(f"Games scraper pipeline completed in {duration}s")
        print("="*50)