# Data Mapping

Version: 1.2

## Bronze → Staging

### stg_tours

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| valorant-project-2026.bronze.tours | tour_id | stg_tours | tour_id | STR conversion | Tournament unique identifier |
| valorant-project-2026.bronze.tours | tour_name | stg_tours | tour_name | STR conversion | Official name of the tournament |
| valorant-project-2026.bronze.tours | tour_tag | stg_tours | tour_tag | STR conversion |  Short tag or abbreviation used to identify the tournament |
| valorant-project-2026.bronze.tours | tour_stage | stg_tours | tour_stage | STR conversion |  Competetion stage of the tournament |
| valorant-project-2026.bronze.tours | tour_region | stg_tours | tour_region | STR conversion | Regional scope of the tournament |
| valorant-project-2026.bronze.tours | tour_status | stg_tours | tour_status | STR conversion | Current or recorded status of the tournament |

### stg_matches

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| valorant-project-2026.bronze.matches | tour_id | stg_matches | tour_id | STR conversion | Tournament FK |
| valorant-project-2026.bronze.matches | match_id | stg_matches | match_id | STR conversion | Match unique identifier |
| valorant-project-2026.bronze.matches | date | stg_matches | match_date | DATE conversion | Calendar date on which the match took place |
| valorant-project-2026.bronze.matches | date | stg_matches | match_datetime | Datetime parsing | Date and time when the match took place |
| valorant-project-2026.bronze.matches | bracket | stg_matches | bracket | STR conversion | Tournament bracket or stage position in which the match was played |
| valorant-project-2026.bronze.matches | home_name | stg_matches | home_name | STR conversion | Home team name |
| valorant-project-2026.bronze.matches | home_alias | stg_matches | home_alias | STR conversion | Home team alias |
| valorant-project-2026.bronze.matches | away_name | stg_matches | away_name | STR conversion | Away team name |
| valorant-project-2026.bronze.matches | away_alias | stg_matches | away_alias | STR conversion | Away team alias |
| valorant-project-2026.bronze.matches | bo | stg_matches | bo | STR conversion | Best-of-series match |
| valorant-project-2026.bronze.matches | patch | stg_matches | patch | STR conversion | Patch version played |
| valorant-project-2026.bronze.matches | home_score | stg_matches | home_score | INT conversion | home team match win score |
| valorant-project-2026.bronze.matches | away_score | stg_matches | away_score | INT conversion | away team match win score |
| valorant-project-2026.bronze.matches | home_h2h_win | stg_matches | home_h2h_win | INT conversion | home team match win against away team |
| valorant-project-2026.bronze.matches | away_h2h_win | stg_matches | away_h2h_win | INT conversion | away team match win against home team |
| valorant-project-2026.bronze.matches | home_h2h_score | stg_matches | home_h2h_score | INT conversion | home team match win score against away team |
| valorant-project-2026.bronze.matches | away_h2h_score | stg_matches | away_h2h_score | INT conversion | away team match win score against home team |
| valorant-project-2026.bronze.matches | home_n_last_win | stg_matches | home_n_last_win | INT conversion | home team n-last match win |
| valorant-project-2026.bronze.matches | away_n_last_win | stg_matches | away_n_last_win | INT conversion | away team n-last match win |
| valorant-project-2026.bronze.matches | home_n_last_match | stg_matches | home_n_last_match | INT conversion | home team n-last match recorded |
| valorant-project-2026.bronze.matches | away_n_last_match | stg_matches | away_n_last_match | INT conversion | away team n-last match recorded |
| valorant-project-2026.bronze.matches | home_n_last_wr | stg_matches | home_n_last_wr | FLOAT conversion | home team n-last match win rate |
| valorant-project-2026.bronze.matches | away_n_last_wr | stg_matches | away_n_last_wr | FLOAT conversion | away team n-last match win rate |

### stg_games_overview

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| valorant-project-2026.bronze.games_overview | match_id | stg_games_overview | match_id | STR conversion | Match FK |
| valorant-project-2026.bronze.games_overview | game_id | stg_games_overview | game_id | STR conversion |  Unique identifier of the game |
| valorant-project-2026.bronze.matches | date | stg_games_overview | match_date | DATE conversion | Calendar date on which the match took place |
| valorant-project-2026.bronze.matches | date | stg_games_overview | match_datetime | Datetime parsing | Date and time when the match took place |
| valorant-project-2026.bronze.games_overview | game_map | stg_games_overview | game_map | STR conversion & Missing-value handling | Map on which the game was played |
| valorant-project-2026.bronze.games_overview | game_duration | stg_games_overview | game_duration | Time parsing | Duration of the game in seconds |
| valorant-project-2026.bronze.games_overview | home_score | stg_games_overview | home_score | INT conversion | Total rounds won by the home team in the game |
| valorant-project-2026.bronze.games_overview | away_score | stg_games_overview | away_score | INT conversion | Total rounds won by the away team in the game |
| valorant-project-2026.bronze.games_overview | home_atk_score | stg_games_overview | home_atk_score | INT conversion | Number of regulation and overtime-adjusted rounds won by the home team while attacking |
| valorant-project-2026.bronze.games_overview | away_atk_score | stg_games_overview | away_atk_score | INT conversion | Number of regulation and overtime-adjusted rounds won by the away team while attacking |
| valorant-project-2026.bronze.games_overview | home_def_score | stg_games_overview | home_def_score | INT conversion | Number of regulation and overtime-adjusted rounds won by the home team while defending |
| valorant-project-2026.bronze.games_overview | away_def_score | stg_games_overview | away_def_score | INT conversion | Number of regulation and overtime-adjusted rounds won by the away team while defending |
| valorant-project-2026.bronze.games_overview | home_ot_score | stg_games_overview | home_ot_score | INT conversion | Number of overtime rounds won by the home team |
| valorant-project-2026.bronze.games_overview | away_ot_score | stg_games_overview | away_ot_score | INT conversion | Number of overtime rounds won by the away team |

### stg_games_economy

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| valorant-project-2026.bronze.games_economy | match_id | stg_games_economy | match_id | STR conversion | Match FK |
| valorant-project-2026.bronze.games_economy | game_id | stg_games_economy | game_id | STR conversion |  Unique identifier of the game |
| valorant-project-2026.bronze.matches | date | stg_games_economy | match_date | DATE conversion | Calendar date on which the match took place |
| valorant-project-2026.bronze.matches | date | stg_games_economy | match_datetime | Datetime parsing | Date and time when the match took place |
| valorant-project-2026.bronze.games_economy | home_pstl_win | stg_games_economy | home_pstl_win | INT conversion | Number of pistol rounds won by the home team |
| valorant-project-2026.bronze.games_economy | away_pstl_win | stg_games_economy | away_pstl_win | INT conversion | Number of pistol rounds won by the away team |
| valorant-project-2026.bronze.games_economy | home_eco_round | stg_games_economy | home_eco_round | INT conversion | Number of eco rounds played by the home team |
| valorant-project-2026.bronze.games_economy | away_eco_round | stg_games_economy | away_eco_round | INT conversion | Number of eco rounds played by the away team |
| valorant-project-2026.bronze.games_economy | home_eco_win | stg_games_economy | home_eco_win | INT conversion | Number of eco win played by the home team |
| valorant-project-2026.bronze.games_economy | away_eco_win | stg_games_economy | away_eco_win | INT conversion | Number of eco win played by the away team|
| valorant-project-2026.bronze.games_economy | home_semi_eco_round | stg_games_economy | home_semi_eco_round | INT conversion | Number of semi eco rounds played by the home team |
| valorant-project-2026.bronze.games_economy | away_semi_eco_round | stg_games_economy | away_semi_eco_round | INT conversion | Number of semi eco rounds played by the away team |
| valorant-project-2026.bronze.games_economy | home_semi_eco_win | stg_games_economy | home_semi_eco_win | INT conversion | Number of semi eco rounds win by the home team |
| valorant-project-2026.bronze.games_economy | away_semi_eco_win | stg_games_economy | away_semi_eco_win | INT conversion | Number of semi eco rounds win by the away team |
| valorant-project-2026.bronze.games_economy | home_semi_buy_round | stg_games_economy | home_semi_buy_round | INT conversion | Number of semi buy rounds played by the home team |
| valorant-project-2026.bronze.games_economy | away_semi_buy_round | stg_games_economy | away_semi_buy_round | INT conversion | Number of semi buy rounds played by the away team |
| valorant-project-2026.bronze.games_economy | home_semi_buy_win | stg_games_economy | home_semi_buy_win | INT conversion | Number of semi buy win played by the home team |
| valorant-project-2026.bronze.games_economy | away_semi_buy_win | stg_games_economy | away_semi_buy_win | INT conversion | Number of semi buy win played by the away team |
| valorant-project-2026.bronze.games_economy | home_full_buy_round | stg_games_economy | home_full_buy_round | INT conversion | Number of full buy rounds played by the home team |
| valorant-project-2026.bronze.games_economy | away_full_buy_round | stg_games_economy | away_full_buy_round | INT conversion | Number of full buy rounds played by the away team |
| valorant-project-2026.bronze.games_economy | home_full_buy_win | stg_games_economy | home_full_buy_win | INT conversion | Number of full buy win played by the home team |
| valorant-project-2026.bronze.games_economy | away_full_buy_win | stg_games_economy | away_full_buy_win | INT conversion | Number of full buy win played by the away team |

### stg_map_vetos

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| valorant-project-2026.bronze.map_vetos | match_id | stg_map_vetos | match_id | STR conversion | Match FK |
| valorant-project-2026.bronze.map_vetos | map_name | stg_map_vetos | map_name | STR conversion | Name of the map involved in the veto action |
| valorant-project-2026.bronze.map_vetos | team_alias | stg_map_vetos | team_alias | STR conversion | Alias of the team performing the veto action |
| valorant-project-2026.bronze.map_vetos | action | stg_map_vetos | action | STR conversion | Type of map veto action performed |

### stg_players

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| valorant-project-2026.bronze.players | game_id | stg_players | game_id | STR conversion | game FK |
| valorant-project-2026.bronze.players | name | stg_players | player_name | STR conversion | Name of the player |
| valorant-project-2026.bronze.players | team_alias | stg_players | team_alias | STR conversion | Alias of the team represented by the player in the game |
| valorant-project-2026.bronze.players | nationality | stg_players | nationality | STR conversion | Nationality associated with the player |
| valorant-project-2026.bronze.players | agent | stg_players | agent | STR conversion | Agent selected by the player for the game |
| valorant-project-2026.bronze.players | mod | stg_players | mod | STR conversion | Statistical aggregation mode indicating whether the player statistics |
| valorant-project-2026.bronze.players | r | stg_players | r | FLOAT conversion | Player rating for the game |
| valorant-project-2026.bronze.players | acs | stg_players | acs | INT conversion | Average Combat Score (ACS) achieved by the player in the game |
| valorant-project-2026.bronze.players | k | stg_players | k | INT conversion | Number of kills recorded by the player in the game |
| valorant-project-2026.bronze.players | d | stg_players | d | INT conversion | Number of deaths recorded by the player in the game |
| valorant-project-2026.bronze.players | a | stg_players | a | INT conversion | Number of assists recorded by the player in the game |
| valorant-project-2026.bronze.players | kd | stg_players | kd | INT conversion | Kill-to-death diff of the player in the game |
| valorant-project-2026.bronze.players | kast | stg_players | kast | INT conversion | Percentage of rounds in which the player recorded a kill, assist, survived, or was traded|
| valorant-project-2026.bronze.players | adr | stg_players | adr | INT conversion | Average Damage per Round (ADR) achieved by the player|
| valorant-project-2026.bronze.players | hs | stg_players | hs | INT conversion | Percentage of the player's kills that were headshots |
| valorant-project-2026.bronze.players | fk | stg_players | fk | INT conversion | Number of first kills recorded by the player |
| valorant-project-2026.bronze.players | fd | stg_players | fd | INT conversion | Number of first deaths recorded by the player |
| valorant-project-2026.bronze.players | fkfd | stg_players | fkfd | INT conversion | First-kill to first-death diff of the player |


## Staging → Silver

### matches

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| stg_matches | tour_id | matches | tour_id | Direct mapping | Tournament FK |
| stg_matches | match_id | matches | match_id | Direct mapping | Match identifier |
| stg_matches | match_date | matches | match_date | Direct mapping | Match calendar date |
| stg_matches | match_datetime | matches | match_datetime | Direct mapping | Match timestamp |
| stg_matches | bracket | matches | bracket | Direct mapping | Match bracket |
| stg_matches | home_name | matches | home_name | Direct mapping | Home team name |
| stg_matches | home_alias | matches | home_alias | Direct mapping | Home team alias |
| stg_matches | away_name | matches | away_name | Direct mapping | Away team name |
| stg_matches | away_alias | matches | away_alias | Direct mapping | Away team alias |
| stg_matches | bo | matches | bo | Direct mapping | Best-of-series match |
| stg_matches | patch | matches | patch | Direct mapping | Patch version played |
| stg_matches | home_score | matches | home_score | Domain validation | home team match win score |
| stg_matches | away_score | matches | away_score | Domain validation | away team match win score |
| stg_matches | home_h2h_win | matches | home_h2h_win | Domain validation | home team match win against away team |
| stg_matches | away_h2h_win | matches | away_h2h_win | Domain validation | away team match win against home team |
| stg_matches | home_h2h_score | matches | home_h2h_score | Domain validation | home team game win score against away team |
| stg_matches | away_h2h_score | matches | away_h2h_score | Domain validation | away team game win score against home team |
| stg_matches | home_n_last_win | matches | home_n_last_win | Domain validation | home team n-last match win recorded |
| stg_matches | away_n_last_win | matches | away_n_last_win | Domain validation | away team n-last match win recorded |
| stg_matches | home_n_last_match | matches | home_n_last_match | Domain validation | home team n-last match recorded |
| stg_matches | away_n_last_match | matches | away_n_last_match | Domain validation | away team n-last match recorded |
| stg_matches | home_n_last_wr | matches | home_n_last_wr | Domain validation | home team n-last match win rate |
| stg_matches | away_n_last_wr | matches | away_n_last_wr | Domain validation | away team n-last match win rate |

### games_overview

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| stg_games_overview | match_id | games_overview | match_id | Direct mapping | Match FK |
| stg_games_overview | game_id | games_overview | game_id | Direct mapping |  Unique identifier of the game |
| stg_games_overview | date | games_overview | match_date | Direct mapping | Calendar date on which the match took place |
| stg_games_overview | date | games_overview | match_datetime | Direct mapping | Date and time when the match took place |
| stg_games_overview | game_map | games_overview | game_map | Direct mapping | Map on which the game was played |
| stg_games_overview | game_duration | games_overview | game_duration | Domain validation | Duration of the game in seconds |
| stg_games_overview | home_score | games_overview | home_score | Domain validation | Total rounds won by the home team in the game |
| stg_games_overview | away_score | games_overview | away_score | Domain validation | Total rounds won by the away team in the game |
| stg_games_overview | home_atk_score | games_overview | home_atk_score | Domain validation | Number of regulation and overtime-adjusted rounds won by the home team while attacking |
| stg_games_overview | away_atk_score | games_overview | away_atk_score | Domain validation | Number of regulation and overtime-adjusted rounds won by the away team while attacking |
| stg_games_overview | home_def_score | games_overview | home_def_score | Domain validation | Number of regulation and overtime-adjusted rounds won by the home team while defending |
| stg_games_overview | away_def_score | games_overview | away_def_score | Domain validation | Number of regulation and overtime-adjusted rounds won by the away team while defending |
| stg_games_overview | home_ot_score | games_overview | home_ot_score | Domain validation | Number of overtime rounds won by the home team |
| stg_games_overview | away_ot_score | games_overview | away_ot_score | Domain validation | Number of overtime rounds won by the away team |

### games_economy

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| stg_games_economy | match_id | games_economy | match_id | Direct mapping | Match FK |
| stg_games_economy | game_id | games_economy | game_id | Direct mapping |  Unique identifier of the game |
| stg_games_economy | date | games_economy | match_date | Direct mapping | Calendar date on which the match took place |
| stg_games_economy | date | games_economy | match_datetime | Direct mapping | Date and time when the match took place |
| stg_games_economy | home_pstl_win | games_economy | home_pstl_win | Domain validation | Number of pistol rounds won by the home team |
| stg_games_economy | away_pstl_win | games_economy | away_pstl_win | Domain validation | Number of pistol rounds won by the away team |
| stg_games_economy | home_eco_round | games_economy | home_eco_round | Domain validation | Number of eco rounds played by the home team |
| stg_games_economy | away_eco_round | games_economy | away_eco_round | Domain validation | Number of eco rounds played by the away team |
| stg_games_economy | home_eco_win | games_economy | home_eco_win | Domain validation | Number of eco win played by the home team |
| stg_games_economy | away_eco_win | games_economy | away_eco_win | Domain validation | Number of eco win played by the away team|
| stg_games_economy | home_semi_eco_round | games_economy | home_semi_eco_round | Domain validation | Number of semi eco rounds played by the home team |
| stg_games_economy | away_semi_eco_round | games_economy | away_semi_eco_round | Domain validation | Number of semi eco rounds played by the away team |
| stg_games_economy | home_semi_eco_win | games_economy | home_semi_eco_win | Domain validation | Number of semi eco rounds win by the home team |
| stg_games_economy | away_semi_eco_win | games_economy | away_semi_eco_win | Domain validation | Number of semi eco rounds win by the away team |
| stg_games_economy | home_semi_buy_round | games_economy | home_semi_buy_round | Domain validation | Number of semi buy rounds played by the home team |
| stg_games_economy | away_semi_buy_round | games_economy | away_semi_buy_round | Domain validation | Number of semi buy rounds played by the away team |
| stg_games_economy | home_semi_buy_win | games_economy | home_semi_buy_win | Domain validation | Number of semi buy win played by the home team |
| stg_games_economy | away_semi_buy_win | games_economy | away_semi_buy_win | Domain validation | Number of semi buy win played by the away team |
| stg_games_economy | home_full_buy_round | games_economy | home_full_buy_round | Domain validation | Number of full buy rounds played by the home team |
| stg_games_economy | away_full_buy_round | games_economy | away_full_buy_round | Domain validation | Number of full buy rounds played by the away team |
| stg_games_economy | home_full_buy_win | games_economy | home_full_buy_win | Domain validation | Number of full buy win played by the home team |
| stg_games_economy | away_full_buy_win | games_economy | away_full_buy_win | Domain validation | Number of full buy win played by the away team |

### players

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| stg_players | game_id | players | game_id | Direct mapping | Game FK |
| stg_game_overview | date | players | match_date | Direct mapping | Match calendar date |
| stg_game_overview | datetime | players | match_dateime | Direct mapping | Match timestamp |
| stg_players | name | players | player_name | Direct mapping | Name of the player |
| stg_players | team_alias | players | team_alias | Direct mapping | Alias of the team represented by the player in the game |
| stg_players | nationality | players | nationality | Direct mapping | Nationality associated with the player |
| stg_players | agent | players | agent | Direct mapping | Agent selected by the player for the game |
| stg_players | mod | players | mod | Direct mapping | Statistical aggregation mode indicating whether the player statistics |
| stg_players | r | players | r | Domain validation | Player rating for the game |
| stg_players | acs | players | acs | Domain validation | Average Combat Score (ACS) achieved by the player in the game |
| stg_players | k | players | k | Domain validation | Number of kills recorded by the player in the game |
| stg_players | d | players | d | Domain validation | Number of deaths recorded by the player in the game |
| stg_players | a | players | a | Domain validation | Number of assists recorded by the player in the game |
| stg_players | kd | players | kd | Domain validation | Kill-to-death diff of the player in the game |
| stg_players | kast | players | kast | Domain validation | Percentage of rounds in which the player recorded a kill, assist, survived, or was traded |
| stg_players | adr | players | adr | Domain validation | Average Damage per Round (ADR) achieved by the player |
| stg_players | hs | players | hs | Domain validation | Percentage of the player's kills that were headshots |
| stg_players | fk | players | fk | Domain validation | Number of first kills recorded by the player |
| stg_players | fd | players | fd | Domain validation | Number of first deaths recorded by the player |
| stg_players | fkfd | players | fkfd | Domain validation | First-kill to first-death diff of the player |

### dims_tours

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| stg_tours | tour_id | dims_tours | tour_id | Direct mapping | Tournament unique identifier |
| stg_tours | tour_name | dims_tours | tour_name | Direct mapping | Official name of the tournament |
| stg_tours | tour_tag | dims_tours | tour_tag | Direct mapping | Short tag or abbreviation used to identify the tournament |
| stg_tours | tour_stage | dims_tours | tour_stage | Domain validation | Competetion stage of the tournament |
| stg_tours | tour_region | dims_tours | tour_region | Domain validation | Regional scope of the tournament |
| stg_tours | tour_status | dims_tours | tour_status | Direct mapping | Current or recorded status of the tournament |

### dims_teams

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| matches | team_name | dims_teams | team_id | Window function | Surrogate identifier uniquely assigned to each team |
| matches | team_name | dims_teams | team_name | Unique direct mapping | Standardized full name of the team |
| matches | team_alias | dims_teams | team_alias | Direct mapping | Standardized short alias used to identify the team in source data |
| dims_tours | tour_region | dims_teams | tour_region | Dimension lookup | Competitive region associated with the team |

### dims_players

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| players | player_name | dims_players | player_id | Window function | Surrogate identifier uniquely assigned to each player |
| players | player_name | dims_players | player_name | Unique direct mapping | Standardized name of the player |
| players | nationality | dims_players | player_nationality | Direct mapping | Nationality associated with the player |

### dims_maps

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| stg_map_vetos | map_name | dims_map_vetos | map_id | Window function | Surrogate identifier uniquely assigned to each map |
| stg_map_vetos | map_name | dims_map_vetos | map_name | Unique direct mapping | Standardized name of the map |

### dims_agents

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| players | agent_name | dims_agents | agent_id | Window function | Surrogate identifier uniquely assigned to each agent |
| players | agent_name | dims_agents | agent_name | Unique direct mapping | Standardized name of the agent |

## Silver → Gold

### fact_matches

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| matches | tour_id | fact_matches | tour_id | Direct mapping | Tournament FK |
| matches | match_id | fact_matches | match_id | Direct mapping | Match identifier |
| matches | match_date | fact_matches | match_date | Direct mapping | Match calendar date |
| matches | match_datetime | fact_matches | match_datetime | Direct mapping | Match timestamp |
| matches | bracket | fact_matches | bracket | Direct mapping | Match bracket |
| dims_teams | team_id | fact_matches | home_team_id | Dimension Lookup | Team FK |
| dims_teams | team_id | fact_matches | away_team_id | Dimension Lookup | Team FK |
| matches | bo | fact_matches | bo | Direct mapping | Best-of-series match |
| matches | patch | fact_matches | patch | Direct mapping | Patch version played |
| matches | home_score | fact_matches | home_score | Direct mapping | Home team score |
| matches | away_score | fact_matches | away_score | Direct mapping | Away team score |
| matches | home_score & away_score | fact_matches | normalized_score_diff | Normalization | Normalized difference between home and away match scores |
| games_overview | home_score | fact_matches | home_total_round | Aggregation (SUM) + Join | Home team total game round score |
| games_overview | away_score | fact_matches | away_total_round | Aggregation (SUM) + Join | Away team total game round score |
| games_overview | home_score & away_score | fact_matches | normalized_match_round_diff | Aggregation (SUM) + Join + Normalization | Normalized home score diff againts away score |
| matches | home_h2h_win | fact_matches | home_h2h_win | Direct mapping | home team match win against away team |
| matches | away_h2h_win | fact_matches | away_h2h_win | Direct mapping | away team match win against home team |
| matches | home_h2h_win & away_h2h_win | fact_matches | normalized_h2h_win_diff | Normalization | Normalized home team head-to-head match win rate against home team |
| matches | home_h2h_score | fact_matches | home_h2h_score | Direct mapping | Home team game win score against away team |
| matches | away_h2h_score | fact_matches | away_h2h_score | Direct mapping | Away team game win score against home team |
| matches | home_h2h_score & away_h2h_score | fact_matches | normalized_h2h_game_win_diff | Normalization | Normalized home team head-to-head game win score rate against away team |
| matches | home_n_last_win | fact_matches | home_n_last_win | Direct mapping | Home team n-last match win recorded |
| matches | away_n_last_win | fact_matches | away_n_last_win | Direct mapping | Away team n-last match win recorded |
| matches | home_n_last_match | fact_matches | home_n_last_match | Direct mapping | Home team n-last match recorded |
| matches | away_n_last_match | fact_matches | away_n_last_match | Direct mapping | Away team n-last match recorded |
| matches | home_n_last_wr | fact_matches | home_n_last_wr | Direct mapping | Home team n-last match win rate |
| matches | away_n_last_wr | fact_matches | away_n_last_wr | Direct mapping | Away team n-last match win rate |
| matches | home_score & away_score | fact_matches | is_home_win | Business logic | Boolean represent home team win status |

### fact_games

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| fact_matches | tour_id | fact_games | tour_id | Direct mapping | Tournament FK |
| games_overview | match_id | fact_games | match_id | Direct mapping | Match FK |
| games_overview | game_id | fact_games | game_id | Direct mapping | Unique identifier of the game |
| games_overview | match_date | fact_games | match_date | Direct mapping | Calendar date on which the match containing the game took place |
| games_overview | match_datetime | fact_games | match_datetime | Direct mapping | Date and time at which the match containing the game took place |
| fact_matches | home_team_id | fact_games | home_team_id | Direct mapping | Team FK |
| fact_matches | away_team_id | fact_games | away_team_id | Direct mapping | Team FK |
| dims_maps | map_id | fact_games | map_id | Dimension lookup | Map FK |
| games_overview | game_duration | fact_games | game_duration | Direct mapping | Duration of the game in seconds |
| games_overview | home_score | fact_games | home_score | Direct mapping | Total rounds won by the home team in the game |
| games_overview | away_score | fact_games | away_score | Direct mapping | Total rounds won by the away team in the game |
| games_overview | home_score & away_score | fact_games | total_round | Derived metric | Total number of rounds played in the game |
| games_overview | home_score & away_score | fact_games | normalized_score_diff | Normalization | Normalized difference between home and away round scores |
| games_overview | home_atk_score | fact_games | home_atk_score | Direct mapping | Number of rounds won by the home team while attacking |
| games_overview | away_atk_score | fact_games | away_atk_score | Direct mapping | Number of rounds won by the away team while attacking |
| games_overview | home_atk_score, home_def_score, away_atk_score, away_def_score | fact_games | atk_wr_ratio | Derived metric | Ratio comparing the attacking-side win rates of the home and away teams |
| games_overview | home_def_score | fact_games | home_def_score | Direct mapping | Number of rounds won by the home team while defending |
| games_overview | away_def_score | fact_games | away_def_score | Direct mapping | Number of rounds won by the away team while defending |
| games_overview | home_atk_score, home_def_score, away_atk_score, away_def_score | fact_games | def_wr_ratio | Derived metric | Ratio comparing the defending-side win rates of the home and away teams |
| games_overview | home_ot_score | fact_games | home_ot_score | Direct mapping | Number of overtime rounds won by the home team |
| games_overview | away_ot_score | fact_games | away_ot_score | Direct mapping | Number of overtime rounds won by the away team |
| games_overview | home_ot_score & away_ot_score | fact_games | normalized_ot_score_diff | Normalization | Rate representing the relative overtime round performance between the home and away teams |
| games_economy | home_pstl_win | fact_games | home_pstl_win | Direct mapping | Number of pistol rounds won by the home team |
| games_economy | away_pstl_win | fact_games | away_pstl_win | Direct mapping | Number of pistol rounds won by the away team |
| games_economy | home_pstl_win & away_pstl_win | fact_games | pstl_win_diff | Derived metric | Difference between the number of pistol rounds won by the home and away teams |
| games_economy | home_eco_round | fact_games | home_eco_round | Direct mapping | Number of eco rounds played by the home team |
| games_economy | away_eco_round | fact_games | away_eco_round | Direct mapping | Number of eco rounds played by the away team |
| games_economy | home_eco_win | fact_games | home_eco_win | Direct mapping | Number of eco rounds won by the home team |
| games_economy | away_eco_win | fact_games | away_eco_win | Direct mapping | Number of eco rounds won by the away team |
| games_economy | home_eco_round, home_eco_win, away_eco_round, away_eco_win | fact_games | eco_wr_diff | Derived metric | Relative difference in eco-round win rate between the home and away teams |
| games_economy | home_semi_eco_round | fact_games | home_semi_eco_round | Direct mapping | Number of semi eco rounds played by the home team |
| games_economy | away_semi_eco_round | fact_games | away_semi_eco_round | Direct mapping | Number of semi eco rounds played by the away team |
| games_economy | home_semi_eco_win | fact_games | home_semi_eco_win | Direct mapping | Number of semi eco won played by the home team |
| games_economy | away_semi_eco_win | fact_games | away_semi_eco_win | Direct mapping | Number of semi eco won played by the away team |
| games_economy | home_semi_eco_round, home_semi_eco_win, away_semi_eco_round, away_semi_eco_win | fact_games | semi_eco_wr_diff | Derived metric | Relative difference in semi-eco-round win rate between the home and away teams |
| games_economy | home_semi_buy_round | fact_games | home_semi_buy_round | Direct mapping | Number of semi buy rounds played by the home team |
| games_economy | away_semi_buy_round | fact_games | away_semi_buy_round | Direct mapping | Number of semi buy rounds played by the away team |
| games_economy | home_semi_buy_win | fact_games | home_semi_buy_win | Direct mapping | Number of semi buy won played by the home team |
| games_economy | away_semi_buy_win | fact_games | away_semi_buy_win | Direct mapping | Number of semi buy won played by the away team |
| games_economy | home_semi_buy_round, home_semi_buy_win, away_semi_buy_round, away_semi_buy_win | fact_games | semi_buy_wr_diff | Derived metric | Relative difference in semi-buy-round win rate between the home and away teams |
| games_economy | home_full_buy_round | fact_games | home_full_buy_round | Direct mapping | Number of full buy rounds played by the home team |
| games_economy | away_full_buy_round | fact_games | away_full_buy_round | Direct mapping | Number of full buy rounds played by the away team |
| games_economy | home_full_buy_win | fact_games | home_full_buy_win | Direct mapping | Number of full buy won played by the home team |
| games_economy | away_full_buy_win | fact_games | away_full_buy_win | Direct mapping | Number of full buy won played by the away team |
| games_economy | home_full_buy_round, home_full_buy_win, away_full_buy_round, away_full_buy_win | fact_games | full_buy_wr_diff | Derived metric | Relative difference in full-buy-round win rate between the home and away teams |
| games_overview | home_score & away_score | fact_matches | is_home_win | Business logic | Boolean represent home team win status |

### fact_map_vetos

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| stg_map_vetos | match_id | fact_map_vetos | match_id | Direct mapping | Match FK |
| dims_maps | map_id | fact_map_vetos | map_id | Dimension lookup | Map FK |
| dims_teams | team_id | fact_map_vetos | team_id | Dimension lookup | Team FK |
| fact_matches | home_team_id | fact_map_vetos | team_id | Direct mapping + Join | Team FK |
| fact_matches | away_team_id | fact_map_vetos | team_id | Direct mapping + Join | Team FK |
| stg_map_vetos | action | fact_map_vetos | action | Direct mapping | Type of map veto action performed |
| stg_map_vetos | match_id, map_id, team_id, action | fact_map_vetos | action_order | Window function | Sequential order of the veto action for a team and action type |

### fact_players

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| team_games_performance | tour_id | fact_players | tour_id | Direct mapping | Tournament FK |
| team_games_performance | match_id | fact_players | match_id | Direct mapping | Match FK |
| players | game_id | fact_players | game_id | Direct mapping | Game FK |
| match_date | date | No | None | Match calendar date |
| match_datetime | datetime | No | None | Match timestamp |
| team_games_performance | map_id | fact_players | map_id | Direct mapping + CTE | Map FK |
| dims_players | player_id | fact_players | player_id | Dimension lookup | Player FK |
| team_games_performance | team_id | fact_players | team_id | Direct mapping + Join | Team FK |
| dims_agents | agent_id | fact_players | agent_id | Dimension lookup | Agent FK |
| team_games_performance | is_win | fact_players | is_win | Direct mapping | Binary indicator equal to 1 when the player's team won the game |
| players | mod | fact_players | mod | Direct mapping | Statistical aggregation mode indicating whether the player statistics |
| players | r | fact_players | r | Direct mapping | Player rating for the game |
| players | acs | fact_players | acs | Direct mapping | Average Combat Score (ACS) achieved by the player in the game |
| players | k | fact_players | k | Direct mapping | Number of kills recorded by the player in the game |
| players | d | fact_players | d | Direct mapping | Number of deaths recorded by the player in the game |
| players | a | fact_players | a | Direct mapping | Number of assists recorded by the player in the game |
| players | kd | fact_players | kd | Direct mapping | Kill-to-death diff of the player in the game |
| players | kast | fact_players | kast | Direct mapping | Percentage of rounds in which the player recorded a kill, assist, survived, or was traded |
| players | adr | fact_players | adr | Direct mapping | Average Damage per Round (ADR) achieved by the player |
| players | hs | fact_players | hs | Direct mapping | Percentage of the player's kills that were headshots |
| players | fk | fact_players | fk | Direct mapping | Number of first kills recorded by the player |
| players | fd | fact_players | fd | Direct mapping | Number of first deaths recorded by the player |
| players | fkfd | fact_players | fkfd | Direct mapping | First-kill to first-death diff of the player |

### team_games_performance

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| fact_games | tour_id | team_games_performance | tour_id | Direct mapping | Tournament FK |
| fact_games | match_id | team_games_performance | match_id | Direct mapping | Match FK |
| fact_games | game_id | team_games_performance | game_id | Direct mapping | Game FK |
| fact_games | map_id | team_games_performance | map_id | Direct mapping | Map FK |
| fact_games | home_team_id | team_games_performance | team_id | Role normalization | Team FK |
| fact_games | away_team_id | team_games_performance | team_id | Role normalization | Team FK |
| fact_games | home_ot_score & away_ot_score | team_games_performance | is_ot | Business logic | Binary indicator equal to 1 when the game went to overtime |
| fact_games | is_home_win | team_games_performance | is_win | Direct mapping & Domain validation | Binary indicator equal to 1 when the team won the game |
| fact_games | game_duration | team_games_performance | game_duration | Direct mapping | Duration of the game in seconds |
| fact_games | normalized_score_diff | team_games_performance | normalized_score_diff | Direct mapping & Negation transformation | Normalized score difference from the perspective of the team |
| fact_games | home_atk_score & away_def_score | team_games_performance | atk_wr | Derived metric | Attacking-side round win rate of the team |
| fact_games | away_atk_score & home_def_score | team_games_performance | atk_wr | Derived metric | Attacking-side round win rate of the team |
| fact_games | home_def_score & away_atk_score | team_games_performance | def_wr | Derived metric | Defending-side round win rate of the team |
| fact_games | away_def_score & home_atk_score | team_games_performance | def_wr | Derived metric | Defending-side round win rate of the team |
| fact_games | home_pstl_win & away_pstl_win | team_games_performance | pstl_wr | Direct mapping | Pistol-round win rate of the team |
| fact_games | home_eco_round & home_eco_win | team_games_performance | eco_wr | Derived metric | Eco-round win rate of the team |
| fact_games | away_eco_round & away_eco_win | team_games_performance | eco_wr | Derived metric | Eco-round win rate of the team |
| fact_games | home_semi_eco_round & home_semi_eco_win | team_games_performance | semi_eco_wr | Derived metric | Semi-eco-round win rate of the team |
| fact_games | away_semi_eco_round & away_semi_eco_win | team_games_performance | semi_eco_wr | Derived metric | Semi-eco-round win rate of the team |
| fact_games | home_semi_buy_round & home_semi_buy_win | team_games_performance | semi_buy_wr | Derived metric | Semi-buy-round win rate of the team |
| fact_games | away_semi_buy_round & away_semi_buy_win | team_games_performance | semi_buy_wr | Derived metric | Semi-buy-round win rate of the team |
| fact_games | home_full_buy_round & home_full_buy_win | team_games_performance | full_buy_wr | Derived metric | Full-buy-round win rate of the team |
| fact_games | away_full_buy_round & away_full_buy_win | team_games_performance | full_buy_wr | Derived metric | Full-buy-round win rate of the team |

### team_maps_performance 

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| team_games_performance | team_id | team_maps_performance | team_id | Direct mapping | Tournament FK |
| team_games_performance | map_id | team_maps_performance | map_id | Direct mapping | Match FK |
| team_games_performance | All source model columns | team_maps_performance | map_played | Aggregation (COUNT) | Total map played by team |
| team_games_performance | is_ot | team_maps_performance | ot_played | Aggregation (SUM) | Total Overtime played on the map by team |
| team_games_performance| All source model columns & is_ot | maps_performance | ot_rate | Aggregation (SUM & COUNT DISTINCT) + Derived metric | Overtime rate played on the map by team |
| team_games_performance | is_win | team_maps_performance | maps_win | Aggregation (SUM) | Total win on the map by team |
| team_games_performance | is_win & All source model columns | team_maps_performance | map_wr | Aggregation (COUNT & SUM) + Derived metric | Map win rate by team on the map |
| fact_map_vetos | action | team_maps_performance | pick_count | Business logic + Aggregation (SUM) | Total map pick by team over total team matches |
| fact_map_vetos | action | team_maps_performance | ban_count | Business logic + Aggregation (SUM) | Total map ban by team over total team matches |
| fact_map_vetos & team_games_performance | action & match_id | team_maps_performance | pick_rate | Business logic + Aggregation (COUNT) | Map pick rate by team |
| fact_map_vetos & team_games_performance | action & match_id | team_maps_performance | ban_rate | Business logic + Aggregation (COUNT) | Map ban rate by team |
| team_games_performance | action | team_maps_performance | map_pick_preference | Business logic + Derived metric | Map pick rate by team when the map is not picked by opponent and banned by both team |
| team_games_performance | game_duration | team_games_performance | avg_game_duration | Aggregation (AVG) | Duration aggregation of game on the map by team |
| team_games_performance | normalized_score_diff | team_games_performance | avg_normalized_score_diff | Aggregation (AVG) | Normalized aggregation score difference from the perspective of the team |
| team_games_performance | atk_wr | team_games_performance | avg_atk_wr | Aggregation (AVG) | Aggregation of attacking-side round win rate of the team on the map |
| team_games_performance | def_wr | team_games_performance | avg_def_wr | Aggregation (AVG) | Aggregation of defending-side round win rate of the team on the map |
| team_games_performance | pstl_wr | team_games_performance | avg_pstl_wr | Aggregation (AVG) | Aggregation of pistol-round win rate of the team on the map |
| team_games_performance | eco_wr | team_games_performance | avg_eco_wr | Aggregation (AVG) | Aggregation eco-round win rate of the team on the map |
| team_games_performance | semi_eco_wr | team_games_performance | avg_semi_eco_wr | Aggregation (AVG) | Aggregation semi-eco-round win rate of the team on the map |
| team_games_performance | semi_buy_wr | team_games_performance | avg_semi_buy_wr | Aggregation (AVG) | Aggregation semi-buy-round win rate of the team on the map |
| team_games_performance | full_buy_wr | team_games_performance | avg_full_buy_wr | Aggregation (AVG) | Aggregation full-buy-round win rate of the team on the map |

### maps_performance

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| team_games_performance | map_id | maps_performance | map_id | Direct mapping | Match FK |
| team_games_performance | match_id | maps_performance | map_played | Aggregation (COUNT DISTINCT) | Total map played |
| team_games_performance | is_ot | maps_performances | ot_played | Aggregation (SUM) | Total overtime played on the map |
| team_games_performance| match_id & is_ot | maps_performance | ot_rate | Aggregation (SUM & COUNT DISTINCT) + Derived metric | Overtime rate played on the map |
| fact_map_vetos | action | maps_performances | pick_count | Business logic + Aggregation (SUM) | total map pick |
| fact_map_vetos | action | maps_performances | ban_count | Business logic + Aggregation (SUM) | total map ban |
| fact_map_vetos & fact_games | action & match_id | maps_performance | pick_rate | Business logic + Aggregation (COUNT DISTINCT) + Derived metric | Map pick rate over total matches played |
| fact_map_vetos & fact_games | action & match_id | maps_performance | ban_rate | Business logic + Aggregation (COUNT DISTINCT) + Derived metric | Map ban rate over total matches played |
| team_games_performance | action | maps_performance | map_pick_preference | Business logic + Derived metric | Map pick rate by team when the map is not banned by both team |
| team_games_performance | game_duration | maps_performance | avg_game_duration | Aggregation (AVG) | Duration aggregation of game on the map by team |
| fact_games | home_atk_score & away_atk_score | maps_performance | atk_side_ratio | Aggregation (SUM) + Derived metric| Attacking-side win ratio on the map|
| fact_games | home_def_score & away_def_score | maps_performance | def_side_ratio | Aggregation (SUM) + Derived metric| Defending-side win ratio on the map |

### players_agents_maps_performance

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| fact_players | player_id | players_agents_maps_performance | player_id | Direct mapping | Player FK |
| fact_players | agent_id | players_agents_maps_performance | agent_id | Direct mapping | Agent FK |
| fact_players | map_id | players_agents_maps_performance | map_id | Direct mapping | Map FK |
| fact_players | map_id | players_agents_maps_performance | agent_played | Aggregation (COUNT) | Total agent played |
| fact_players | is_win | players_agents_maps_performance | total_win | Aggregation (SUM) | Total win with the agent played |
| fact_players | is_win & map_id | players_agents_maps_performance | agent_wr | Aggregation (SUM & COUNT) + Derived metric | Agent win rate |
| fact_players | r | players_agents_maps_performance | avg_r | Aggregation (AVG) | Average player rating |
| fact_players | acs | players_agents_maps_performance | avg_acs | Aggregation (AVG) | Average player ACS |
| fact_players | k | players_agents_maps_performance | avg_k | Aggregation (AVG) | Average player kills |
| fact_players | d | players_agents_maps_performance | avg_d | Aggregation (AVG) | Average player deaths |
| fact_players | a | players_agents_maps_performance | avg_a | Aggregation (AVG) | Average player assists |
| fact_players | kd | players_agents_maps_performance | avg_kd | Aggregation (AVG) | Average kill-to-death diff of the player in the game |
| fact_players | kast | players_agents_maps_performance | avg_kast | Aggregation (AVG) | Average percentage of rounds in which the player recorded a kill, assist, survived, or was traded |
| fact_players | adr | players_agents_maps_performance | avg_adr | Aggregation (AVG) | Average ADR achieved by the player |
| fact_players | hs | players_agents_maps_performance | avg_hs | Aggregation (AVG) | Average percentage of the player's kills that were headshots |
| fact_players | fk | players_agents_maps_performance | avg_fk | Aggregation (AVG) | Average player first kills |
| fact_players | fd | players_agents_maps_performance | avg_fd | Aggregation (AVG) | Average player first deaths |
| fact_players | fkfd | players_agents_maps_performance | avg_fkfd | Aggregation (AVG) | Average first kill-to-first death diff of the player in the game |

### agents_maps_performance

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| fact_players | agent_id | agents_maps_performance | agent_id | Direct mapping | Agent FK |
| fact_players | map_id | agents_maps_performance | map_id | Direct mapping | Map FK |
| fact_players | game_id | agents_maps_performance | presence_count | Aggregation (COUNT DISTINCT) | Total agent presence on the map |
| maps_performance | map_played | agents_maps_performance | map_played | Aggregation (SUM) | Total map played with the agent |
| fact_players | agent_id | agents_maps_performance | pick_count | Aggregation (COUNT) | Total agent pick on the map |
| fact_players | is_win | agents_maps_performance | total_win | Aggregation (SUM) | Total agent win on the map |
| fact_players & maps_performance | agent_id & map_played | agents_maps_performance | pick_rate | Aggregation (COUNT) + Derived metric | Agent pick rate on the map |
| fact_players | is_win & game_id | agents_maps_performance | win_rate | Aggregation (SUM & COUNT DISTINCT) + Derived metric | Agent win rate on the map |
| fact_players & maps_performance | game_id & map_played | agents_maps_performance | presence_rate | Aggregation (COUNT DISTINCT) + Derived metric | Agent presence rate on the map |

### agents_performance

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| fact_players | agent_id | agents_maps_performance | agent_id | Direct mapping | Agent FK |
| fact_players | All source model columns | agents_maps_performance | pick_count | Aggregation (COUNT) | Total agent pick on the map |
| maps_performance | game_id | agents_maps_performance | total_games | Aggregation (COUNT & COUNT DISTINCT) + Derived metric| Total map played with the agent |
| fact_players | All source model columns & game_id | agents_maps_performance | pick_rate | Aggregation (SUM & COUNT DISTINCT) + Derived metric | Agent pick rate on the map |
| fact_players | is_win & All source model columns | agents_maps_performance | win_rate | Aggregation (SUM & COUNT) + Derived metric | Agent win rate on the map |
