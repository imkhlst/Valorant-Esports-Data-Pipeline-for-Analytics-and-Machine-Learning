# Data Mapping

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
| valorant-project-2026.bronze.games_economy | away_eco_win | stg_games_economy | away_eco_win | INT conversion | Number of eco win played by the away team. |
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

## Staging → Silver

### matches

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| stg_matches | tour_id | matches | tour_id | Direct mapping | Tournament FK |
| stg_matches | match_id | matches | match_id | Direct mapping | Match identifier |
| stg_matches | match_date | matches | match_date | Direct mapping | Calendar date |
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

### dims_tours

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| stg_tours | tour_id | dims_tours | tour_id | Direct mapping | Tournament unique identifier |
| stg_tours | tour_name | dims_tours | tour_name | Direct mapping | Official name of the tournament |
| stg_tours | tour_tag | dims_tours | tour_tag | Direct mapping |  Short tag or abbreviation used to identify the tournament |
| stg_tours | tour_stage | dims_tours | tour_stage | Domain validation |  Competetion stage of the tournament |
| stg_tours | tour_region | dims_tours | tour_region | Domain validation | Regional scope of the tournament |
| stg_tours | tour_status | dims_tours | tour_status | Direct mapping | Current or recorded status of the tournament |

## Silver → Gold

### fact_matches

| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| matches | tour_id | fact_matches | tour_id | Direct mapping | Tournament FK |
| matches | match_id | fact_matches | match_id | Direct mapping | Match identifier |
| matches | match_date | fact_matches | match_date | Direct mapping | Calendar date |
| matches | match_datetime | fact_matches | match_datetime | Direct mapping | Match timestamp |
| matches | bracket | fact_matches | bracket | Direct mapping | Match bracket |
| dims_tours | team_id | fact_matches | home_team_id | Dimension Lookup | Home team FK |
| dims_tours | team_id | fact_matches | away_team_id | DImension Lookup | Away team FK |
| matches | bo | fact_matches | bo | Direct mapping | Best-of-series match |
| matches | patch | fact_matches | patch | Direct mapping | Patch version played |
| matches | home_score | fact_matches | home_score | Direct mapping | Home team score |
| matches | away_score | fact_matches | away_score | Direct mapping | Away team score |
| games_overview | home_score | fact_matches | home_total_round | Derived metric | Home team total game round score |
| games_overview | away_score | fact_matches | away_total_round | Derived metric | Away team total game round score |
| games_overview | home_score & away_score | fact_matches | score_diff_ratio | Derived metric | home score diff againts away score |
| matches | home_h2h_win | fact_matches | home_h2h_win | Direct mapping | home team match win against away team |
| matches | away_h2h_win | fact_matches | away_h2h_win | Direct mapping | away team match win against home team |
| matches | home_h2h_win & away_h2h_win | fact_matches | h2h_win_ratio | Derived metric | Home team head-to-head match win ratio against home team |
| matches | home_h2h_score | fact_matches | home_h2h_score | Direct mapping | Home team game win score against away team |
| matches | away_h2h_score | fact_matches | away_h2h_score | Direct mapping | Away team game win score against home team |
| matches | home_h2h_score & away_h2h_score | fact_matches | h2h_game_win_ratio | Derived metric | Home team head-to-head game win score ratio against away team |
| matches | home_n_last_win | fact_matches | home_n_last_win | Direct mapping | Home team n-last match win recorded |
| matches | away_n_last_win | fact_matches | away_n_last_win | Direct mapping | Away team n-last match win recorded |
| matches | home_n_last_match | fact_matches | home_n_last_match | Direct mapping | Home team n-last match recorded |
| matches | away_n_last_match | fact_matches | away_n_last_match | Direct mapping | Away team n-last match recorded |
| matches | home_n_last_wr | fact_matches | home_n_last_wr | Direct mapping | Home team n-last match win rate |
| matches | away_n_last_wr | fact_matches | away_n_last_wr | Direct mapping | Away team n-last match win rate |
| matches | home_score & away_score | fact_matches | is_home_win | Business logic | Boolean represent home team win status |