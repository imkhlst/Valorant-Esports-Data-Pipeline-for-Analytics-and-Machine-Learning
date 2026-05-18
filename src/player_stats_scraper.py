from datetime import datetime
from utils.scraper_utils import *
from entities.player_stats_entities import *
from logger import logging

class PlayerStatsScraper:
    def __init__(self):
        pass

    def scrape_player_stat(self, soup: str):
        start_time = datetime.now()
        logging.info("Initialize scrape_player_info ...")
        try:
            player_overview = []
            player_stats = []
            player_agents = []
            match_id = get_value(soup=soup, selector=".vm-stats-tabnav", attr="data-match_id")
            game_id = get_value(soup=soup, selector="vm-stats-gamesnav-item", attr="data-game-id", multiple=True)
            games = get_value(soup=soup, selector=".wf-table-inset.mod-overview", multiple=True)
            n = 1
            for idx, game in enumerate(games):
                players_flag = get_value(soup=game, selector=".flag", attr="title", multiple=True)
                players_container = get_value(soup=game, selector=".mod-player a", attr="text", multiple=True)
                player_name = [re.sub(r"[\n\t]", "", i.split(" ")[0]) for i in players_container]
                player_team = [re.sub(r"[\n\t]", "", i.split(" ")[1]) for i in players_container]
                agents_container = get_value(soup=soup, selector=".mod-agents")
                agents_list = [get_value(soup=i, selector=".stats-sq.mod-agent img") for i in agents_container]
                if any(len(agent) > 1 for agent in agents_list):
                    for side in ["att", "def", "all"]:
                        if side == "att":
                            player_stats = get_value(soup=game, selector=".mod-t", attr="text")
                        elif side == "def":
                            player_stats = get_value(soup=game, selector=".mod-ct", attr="text")
                        else:
                            player_stats = get_value(soup=game, selector=".mod-both", attr="text")
                        player1_stat = player_stats[:12]
                        player2_stat = player_stats[12:24]
                        player3_stat = player_stats[24:36]
                        player4_stat = player_stats[36:48]
                        player5_stat = player_stats[48:]

                        for i, value in enumerate([player1_stat, player2_stat, player3_stat, player4_stat, player5_stat]):
                            player_overview.append([match_id, np.nan, player_name[i], player_team[i], players_flag[i], side, "all_map"])
                            player_stats.append(value)
                    
                    continue
                
                for side in ["att", "def", "all"]:
                    for i, value in player_name:
                        if side == "att":
                            player_stats = get_value(soup=game, selector=".mod-t", attr="text")
                        elif side == "def":
                            player_stats = get_value(soup=game, selector=".mod-ct", attr="text")
                        else:
                            player_stats = get_value(soup=game, selector=".mod-both", attr="text")
                        player1_stat = player_stats[:12]
                        player2_stat = player_stats[12:24]
                        player3_stat = player_stats[24:36]
                        player4_stat = player_stats[36:48]
                        player5_stat = player_stats[48:]
                        
                        for i, value in enumerate([player1_stat, player2_stat, player3_stat, player4_stat, player5_stat]):
                            player_overview.append([match_id, game_id[n], player_name[i], player_team[i], players_flag[i], side, "per_map"])
                            player_stats.append(value)

                if idx < 2 and idx % 2 == 1:
                    n += 1
                
                agents_name = []
                for agent in agents_list:
                    if len(agent) == 1:
                        agents_title = agent[0].get("title").strip()
                        agents_name.append(agents_title)
                    else:
                        print("Agent does not exists.")

                player_agents.append(agents_name)

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_player_info completed in {duration}s")
            return player_overview, player_stats, player_agents
        
        except Exception as e:
            logging.error(f"Error occurs whe running scrape_player_info: {e}")
            print(f"Error occurs whe running scrape_player_info: {e}")

    def scrape_player_stats_info(self, soup_list: list):
        start_time = datetime.now()
        processed = set()
        queue = list(soup_list) if isinstance(soup_list, (set, list)) else [soup_list]
        print(f"Queue: ... (long list)" if queue else "Queue: None")
        try:
            player_stats_info = []
            player_agents_info = []
            for item in queue:
                if item in processed:
                    logging.info(f"Item already processed.")
                    continue

                overview, stats, agents = self.scrape_player_stat(soup=item)
                player_stats = PlayerStats(
                    match_id=overview[0],
                    game_id=overview[1],
                    name=overview[2],
                    team=overview[3],
                    nationality=overview[4],
                    stat_scope=overview[5],
                    side=overview[6],
                    r=stats[0],
                    acs=stats[1],
                    k=stats[2],
                    d=stats[3],
                    a=stats[4],
                    kd=stats[5],
                    kast=stats[6],
                    adr=stats[7],
                    hs=stats[8],
                    fk=stats[9],
                    fd=stats[10],
                    fkfd=stats[11],
                )
                player_stats_info.append(player_stats)
                player_agents_info.append(agents)

            end_time = datetime.now()
            duration = end_time - start_time
            logging.info(f"scrape_player_stats_info completed in {duration}s")
            return player_stats_info, player_agents_info
        
        except Exception as e:
            logging.info(f"Error occurs when running scrape_player_stats_info: {e}")
            print(f"Error occurs when running scrape_player_stats_info: {e}")
    
    def run(self, soup_list: list):
        start_time = datetime.now()

        logging.info("Initialize scrape_player_stats_info ...")
        player_stats_info, player_agents_info = self.scrape_player_stats_info(soup_list=soup_list)
        player_stats_df = player_stats_info([asdict(ps) for ps in player_stats_info])
        path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw\player_stats_raw.csv"
        player_stats_df.to_csv(path)
        logging.info(f"Data has been save in {path}")

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Player stats scraper pipeline completed in {duration}s")
        print("="*50)
        print(f"Player stats scraper pipeline completed in {duration}s")
        print("="*50)
        return soup_list