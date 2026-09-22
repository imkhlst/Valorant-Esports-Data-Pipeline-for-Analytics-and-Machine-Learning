from datetime import datetime
from utils.scraper_utils import *
from entities.player_entities import *
from entities.stats_entities import * # Fix this module
from logger import logging

class PlayerScraper:
    def __init__(self):
        pass

    def scrape_player(
        self,
        url: str,    
    ):
        logging.info("Initialize scrape_player ...")
        try:
            player_id = url.split("/")[-2]
            player_soup = get_soup(url=url)
            nickname = get_value(soup=player_soup, selector=".wf-title", attr="text")
            realname = get_value(soup=player_soup, selector=".player-real-name", attr="text")
            flag = get_value(soup=player_soup, selector=".ge-text-light", attr="text", multiple=True)

            # labels = get_value(soup=player_soup, selector=".wf-label", attr="text", multiple=True)
            # team_info = get_value(soup=player_soup, selector=".wf-card.wf-module-item", attr="text", multiple=True)

            # for i, team_list in enumerate(team_info):
            #     if i == 0 and "Current Teams" in labels:
            #         current_team_id = sort_text(team_list)
            #         join_date = team_list.split(" ", maxsplit= -2)[-1]
            #     else:
            #         if team_list.split("/")[-1].lower() == flag.lower():
            #             continue
            #         else:
            #             past_team_id = team_list.split("/")[-2]
            #             leave_date = team_list
            #             break

            player = Player(
                player_id=player_id,
                player_nickname=nickname,
                player_realname=realname,
                player_nationality=flag[1],
                # status=status,
                # current_team=current_team,
                # join_date=join_date,
                # past_team=past_team,
                # leave_date=leave_date,
                scraped_at=datetime.now()
            )

            logging.info(f"Completed! Found {realname} as {nickname} from {flag}.")

            return player

        except Exception as e:
            logging.error(f"Error occurs whe running scrape_player: {e}")
            save_pipeline(
                status="failed",
                module=["games"]
            )
            raise
    
    def scrape_stat(
        self,
        game_id: str,
        soup: str,
        player_url: set
    ):
        logging.info("Initialize scrape_stat ...")
        try:
            stats_info = []
            player_info = set()
            url_list = set()
            tables = get_value(soup=soup, selector=".ovw-scroll-wrap", multiple=True)
            for table in tables:
                players = get_value(soup=table, selector=".ovw-player a", attr="href", multiple=True)
                for url in players:
                    if url in player_url:
                        continue
                    href = absolute(url=url)
                    player = self.scrape_player(href)
                    player_info.add(player)
                    url_list.add(url)
                
                flags = get_value(soup=table, selector=".flag", attr="title", multiple=True)
                names = get_value(soup=table, selector=".ovw-player-name", attr="text", multiple=True)
                team_aliases = get_value(soup=table, selector=".ovw-player-tag", attr="text", multiple=True)
                agents = get_value(soup=table, selector=".stats-sq.mod-agent.small img", attr="title", multiple=True)
                for mod in ["mod-both", "mod-ct", "mod-t"]:
                    stats_list = get_value(soup=table, selector=f".side.{mod}", attr="text", multiple=True)
                    if len(stats_list) < 60:
                        stats_list.extend([""] * (60 - len(stats_list)))
                    for i, name in enumerate(names):
                        stats = Stats(
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
                            fkfd=int(stats_list[11 + ((len(stats_list) // 5) * i)]) if stats_list[11 + ((len(stats_list) // 5) * i)] != "" else None,
                            scraped_at= datetime.now()
                        )
                        stats_info.append(stats)
                    logging.info(f"Found player info: {names[0]}, {flags[0]}, {team_aliases[0]}, {agents[0]}, {mod}")
                
            logging.info(f"Stats info has been added.")
            return player_info, stats_info, url_list
        
        except Exception as e:
            logging.error(f"Error occurs whe running scrape_player_stat: {e}")
            save_pipeline(
                status="failed",
                module=["games"]
            )
            raise