# Data Dictionary

Version : 1.2

## Silver Models

### matches

| Property | Description |
|---|---|
| Purpose | Match-level cleaned and transformed table |
| Grain | One row per match |
| Primary Key | `match_id` |
| Partition | `match_date` |
| Main Dimensions | `match_id`, `home_name`, `away_name` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `tour_id` | string | No | None | Tournament FK | `2379` |
| `match_id` | string | No | `Unique` | Match identifier | `87370` |
| `match_date` | date | No | None | Match calendar date | `2025-04-06` |
| `match_datetime` | datetime | No | None | Match timestamp | `2025-04-06T04:00:00` |
| `bracket` | string | No | None | Match bracket | `Group Stage: Week 3` |
| `home_name` | string | No | None | Home team name | `Paper Rex` |
| `home_alias` | string | No | None | Home team alias | `PRX` |
| `away_name` | string | No | None | Away team name | `BOOM Esports` |
| `away_alias` | string | No | None | Away team alias | `BME` |
| `bo` | string | No | None | Best-of-series match | `Bo3` |
| `patch` | string | Yes | None | Patch version played | `10.06` |
| `home_score` | integer | No | Must be `>= 0` | home team match win score | `1` |
| `away_score` | integer | No | Must be `>= 0` | away team match win score | `2` |
| `home_h2h_win` | integer | No | Must be `>= 0` | home team match win against away team | `3` |
| `away_h2h_win` | integer | No | Must be `>= 0` | away team match win against home team | `3` |
| `home_h2h_score` | integer | No | Must be `>= 0` | home team game win score against away team | `5` |
| `away_h2h_score` | integer | No | Must be `>= 0` | away team game win score against home team | `6` |
| `home_n_last_win` | integer | No | Must be in range `0` and `5` | home team n-last match win recorded | `1` |
| `away_n_last_win` | integer | No | Must be in range `0` and `5` | away team n-last match win recorded | `2` |
| `home_n_last_match` | integer | No |Must be in range `0` and `5` | home team n-last match recorded | `5` |
| `away_n_last_match` | integer | No | Must be in range `0` and `5` | away team n-last match recorded | `5` |
| `home_n_last_wr` | float | No | Must be in range `0` and `1` and can be NULL when denominator `home_n_last_match` is zero | home team n-last match win rate | `0.2` |
| `away_n_last_wr` | float | No | Must be in range `0` and `1` and can be NULL when denominator `away_n_last_match` is zero | away team n-last match win rate | `0.4` |

### games_overview

| Property | Description |
|---|---|
| Purpose | Game-level overview cleaned and transformed table |
| Grain | One row per game |
| Primary Key | `game_id` |
| Partition | `match_date` |
| Main Dimensions | `game_id`, `game_map` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `match_id` | string | No | None | Match FK | `107942` |
| `game_id` | string | No | None | Game identifier | `258358` |
| `match_date` | date | No | None | Match calendar date | `2026-04-08` |
| `match_datetime` | datetime | No | None | Match timestamp | `2026-04-08T11:00:00` |
| `game_map` | string | No | None | Map name played | `Pearl` |
| `game_duration` | integer | No | Must be `>= 0` when present | Duration games in seconds | `3482` |
| `home_score` | integer | No | Must be `>= 0` | Total rounds won by the home team in the game | `14` |
| `away_score` | integer | No | Must be `>= 0` | Total rounds won by the away team in the game | `12` |
| `home_atk_score` | integer | Yes | Must be `>= 0` when present | Number of regulation and overtime-adjusted rounds won by the home team while attacking | `4` |
| `away_atk_score` | integer | Yes | Must be `>= 0` when present | Number of regulation and overtime-adjusted rounds won by the away team while attacking | `3` |
| `home_def_score` | integer | Yes | Must be `>= 0` when present | Number of regulation and overtime-adjusted rounds won by the home team while defending | `10` |
| `away_def_score` | integer | Yes | Must be `>= 0` when present | Number of regulation and overtime-adjusted rounds won by the away team while defending | `9` |
| `home_ot_score` | integer | Yes | Must be `>= 0` when present | Number of overtime rounds won by the home team | `2` |
| `away_ot_score` | integer | Yes | Must be `>= 0` when present | Number of overtime rounds won by the away team | `0` |

### games_economy

| Property | Description |
|---|---|
| Purpose | Game-level economy cleaned and transformed table |
| Grain | One row per game |
| Primary Key | `game_id` |
| Partition | `match_date` |
| Main Dimensions | `game_id` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `match_id` | string | No | None | Match FK | `77172` |
| `game_id` | string | No | None | Game identifier | `178835` |
| `match_date` | date | No | None | Match Calendar date | `2024-07-21` |
| `match_datetime` | datetime | No | None | Match timestamp | `2024-07-21T17:00:00` |
| `home_pstl_win` | integer | Yes | Must be in range `0` and `2` when present | Number of pistol rounds won by the home team | `2` |
| `away_pstl_win` | integer | Yes | Must be in range `0` and `2` when present | Number of pistol rounds won by the away team | `0` |
| `home_eco_round` | integer | Yes | Must be `>= 0` when present | Number of eco rounds won by the home team | `2` |
| `away_eco_round` | integer | Yes | Must be `>= 0` when present | Number of eco rounds won by the away team | `4` |
| `home_eco_win` | integer | Yes | Must be `>= 0` when present | Number of eco win played by the home team | `2` |
| `away_eco_win` | integer | Yes | Must be `>= 0` when present | Number of eco win played by the away team | `1` |
| `home_semi_eco_round` | integer | Yes | Must be `>= 0` when present | Number of semi eco rounds played by the home team | `3` |
| `away_semi_eco_round` | integer | Yes | Must be `>= 0` when present | Number of semi eco rounds played by the away team | `1` |
| `home_semi_eco_win` | integer | Yes | Must be `>= 0` when present | Number of semi eco rounds win by the home team | `2` |
| `away_semi_eco_win` | integer | Yes | Must be `>= 0` when present | Number of semi eco rounds win by the away team | `1` |
| `home_semi_buy_round` | integer | Yes | Must be `>= 0` when present | Number of semi buy rounds played by the home team | `10` |
| `away_semi_buy_round` | integer | Yes | Must be `>= 0` when present | Number of semi buy rounds played by the home team | `1` |
| `home_semi_buy_win` | integer | Yes | Must be `>= 0` when present | Number of semi buy rounds win by the home team | `4` |
| `away_semi_buy_win` | integer | Yes | Must be `>= 0` when present | Number of semi buy rounds win by the away team | `0` |
| `home_full_buy_round` | integer | Yes | Must be `>= 0` when present | Number of full buy rounds played by the home team | `15` |
| `away_full_buy_round` | integer | Yes | Must be `>= 0` when present | Number of full buy rounds played by the away team | `24` |
| `home_full_buy_win` | integer | Yes | Must be `>= 0` when present | Number of full buy rounds win by the home team | `6` |
| `away_full_buy_win` | integer | Yes | Must be `>= 0` when present | Number of semi buy rounds win by the away team | `14` |

### players

| Property | Description |
|---|---|
| Purpose | Player by game-level cleaned and transformed table |
| Grain | One row per player per game |
| Primary Key | None |
| Partition | `match_date` |
| Main Dimensions | `player_name`, `team_alias`, `agent` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `game_id` | string | No | None | Game FK | `196430` |
| `match_date` | date | No | None | Match calendar date | `2024-07-21` |
| `match_datetime` | datetime | No | None | Match timestamp | `2024-07-21T17:00:00` |
| `player_name` | string | No | None | Name of the player | `Jemkin` |
| `team_alias` | string | No | None | Alias of the team represented by the player in the game | `RRQ` |
| `nationality` | string | No | None | Nationality associated with the player | `Russia` |
| `agent` | string | No | None | Agent selected by the player for the game | `Jett` |
| `mod` | integer | No | None | Statistical aggregation mode indicating whether the player statistics | `avg` |
| `r` | integer | Yes | Must be `> 0` when present | Player rating for the game | `1.47` |
| `acs` | integer | Yes | Must be `> 0` when present | Average Combat Score (ACS) achieved by the player in the game | `330` |
| `k` | integer | Yes | Must be `> 0` when present | Number of kills recorded by the player in the game | `29` |
| `d` | integer | Yes | Must be `>= 0` when present | Number of deaths recorded by the player in the game | `19` |
| `a` | integer | Yes | Must be `>= 0` when present | Number of assists recorded by the player in the game | `2` |
| `kd` | integer | Yes | `k - d` when present | Kill-to-death diff of the player in the game | `10` |
| `kast` | integer | Yes | Must be `> 0` when present | Percentage of rounds in which the player recorded a kill, assist, survived, or was traded | `85` |
| `adr` | integer | Yes | Must be `> 0` when present | Average Damage per Round (ADR) achieved by the player | `210` |
| `hs` | integer | Yes | Must be `>= 0` when present | Percentage of the player's kills that were headshots | `30` |
| `fk` | integer | Yes | Must be `>= 0` when present | Number of first kills recorded by the player | `12` |
| `fd` | integer | Yes | Must be `>= 0` when present | Number of first deaths recorded by the player | `1` |
| `fkfd` | integer | Yes | `fk - fd` when present | First-kill to first-death diff of the player | `11` |

### dims_tours

| Property | Description |
|---|---|
| Purpose | Tournament dimension table |
| Grain | One row per tournament |
| Primary Key | `tour_id` |
| Partition | None |
| Main Dimensions | None |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `tour_id` | string | No | `Unique` | Tournament unique identifier | `2283` |
| `tour_name` | string | No | None | Official name of the tournament | `Valorant Champions 2025` |
| `tour_tag` | string | No | None | Short tag or abbreviation used to identify the tournament | `Valorant Champions Tour 2025` |
| `tour_stage` | string | No | None | Competetion stage of the tournament | `Champions` |
| `tour_region` | string | No | None | Regional scope of the tournament | `World` |
| `tour_status` | string | No | None | Current or recorded status of the tournament | `Completed` |

### dims_teams

| Property | Description |
|---|---|
| Purpose | Team dimension table |
| Grain | One row per team |
| Primary Key | `team_id` |
| Partition | None |
| Main Dimensions | None |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `team_id` | Integer | No | `Unique` | Surrogate identifier uniquely assigned to each team | `11` |
| `team_name` | string | No | None | Standardized full name of the team | `Dragon Ranger Gaming` |
| `team_alias` | string | No | None | Standardized short alias used to identify the team in source data | `DRG` |
| `team_region` | string | No | None | Competitive region associated with the team | `China` |

### dims_players

| Property | Description |
|---|---|
| Purpose | Player dimension table |
| Grain | One row per player |
| Primary Key | `player_id` |
| Partition | None |
| Main Dimensions | None |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `player_id` | Integer | No | `Unique` | Surrogate identifier uniquely assigned to each player | `11` |
| `player_name` | string | No | None | Standardized name of the player | `Akeman` |
| `player_nationality` | string | No | None | Nationality associated with the player | `China` |

### dims_maps

| Property | Description |
|---|---|
| Purpose | Map dimension table |
| Grain | One row per map |
| Primary Key | `map_id` |
| Partition | None |
| Main Dimensions | None |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `map_id` | Integer | No | `Unique` | Surrogate identifier uniquely assigned to each map | `1` |
| `map_name` | string | No | None | Standardized name of the map | `Abyss` |

### dims_agents

| Property | Description |
|---|---|
| Purpose | Agent dimension table |
| Grain | One row per agent |
| Primary Key | `agents_id` |
| Partition | None |
| Main Dimensions | None |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `agent_id` | Integer | No | `Unique` | Surrogate identifier uniquely assigned to each agent | `5` |
| `agent_name` | string | No | None | Standardized name of the agent | `Clove` |

## Gold Models

### fact_matches

| Property | Description |
|---|---|
| Purpose | Match-level fact table |
| Grain | One row per match |
| Primary Key | `match_id` |
| Partition | `match_date` |
| Main Dimensions | `match_id`, `home_team_id`, `away_team_id` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `tour_id` | string | No | None | Tournament FK | `1998` |
| `match_id` | string | No | `Unique` | Match identifier | `71902` |
| `match_date` | date | No | None | Match calendar date | `2024-04-04` |
| `match_datetime` | datetime | No | None | Match timestamp | `2025-04-06T11:00:00` |
| `bracket` | string | No | None | Match bracket | `Regular Season: Week 1` |
| `home_team_id` | integer | No | None | Team FK | `49` |
| `away_team_id` | integer | No | None | Team FK | `36` |
| `bo` | string | No | None | Best-of-series match | `Bo3` |
| `patch` | string | Yes | None | Patch version played | `8.05` |
| `home_score` | integer | No | Must be `>= 0` | Home team score | `0` |
| `away_score` | integer | No | Must be `>= 0` | Away team score | `2` |
| `normalized_score_diff` | float | Yes | Must be in range `-1` and `1` | Normalized difference between home and away match scores | `2` |
| `home_total_round` | integer | No | Must be `>= 0` | Home team total game round score | `13` |
| `away_total_round` | integer | No | Must be `>= 0` | Away team total game round score | `26` |
| `normalized_match_round_diff` | float | Yes | Must be in range `-1` and `1` | Normalized home score diff againts away score | `-0.33333...` |
| `home_h2h_win` | integer | No | Must be `>= 0` | home team match win against away team | `0` |
| `away_h2h_win` | integer | No | Must be `>= 0` | away team match win against home team | `2` |
| `normalized_h2h_win_diff` | float | Yes | Must be in range `-1` and `1` | Normalized home team head-to-head match win rate against home team | `-1.0` |
| `home_h2h_score` | integer | No | Must be `>= 0` | Home team game win score against away team | `0` |
| `away_h2h_score` | integer | No | Must be in range `-1` and `1` | Away team game win score against home team | `4` |
| `normalized_h2h_game_win_diff` | float | Yes | Must be in range `-1` and `1` | Normalized home team head-to-head game win score rate against away team | `-1.0` |
| `home_n_last_win` | integer | No | Must be in range `0` and `5` | home team n-last match win recorded | `3` |
| `away_n_last_win` | integer | No | Must be in range `0` and `5` | away team n-last match win recorded | `4` |
| `home_n_last_match` | integer | No |Must be in range `0` and `5` | home team n-last match recorded | `5` |
| `away_n_last_match` | integer | No | Must be in range `0` and `5` | away team n-last match recorded | `5` |
| `home_n_last_wr` | float | Yes | Must be in range `0` and `1` and can be NULL when denominator `home_n_last_match` is zero | home team n-last match win rate | `0.6` |
| `away_n_last_wr` | float | Yes | Must be in range `0` and `1` and can be NULL when denominator `away_n_last_match` is zero | away team n-last match win rate | `0.8` |
| `is_home_win` | integer | No | Must be in range `0` and `1` and can be NULL when denominator `away_n_last_match` is zero | away team n-last match win rate | `0` |

### fact_games

| Property | Description |
|---|---|
| Purpose | Match-level fact table |
| Grain | One row per game |
| Primary Key | `game_id` |
| Partition | `match_date` |
| Main Dimensions | `game_id`, `home_team_id`, `away_team_id` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `tour_id` | string | No | None | Tournament FK | `2004` |
| `match_id` | string | No | None | Match FK | `71657` |
| `game_id` | string | No | `Unique` | Unique identifier of the game | `163433` |
| `match_date` | date | No | None | Match calendar date | `2024-05-04` |
| `match_datetime` | datetime | No | None | Match timestamp | `2024-05-04T19:20:00` |
| `home_team_id` | integer | No | None | Team FK | `30` |
| `away_team_id` | integer | No | None | Team FK | `32` |
| `map_id` | integer | No | None | Map FK | `4` |
| `game_duration` | integer | Yes | Must be `>= 0` when present | Duration of the game in seconds | `3456` |
| `home_score` | integer | No | Must be `>= 0` | Total rounds won by the home team in the game | `14` |
| `away_score` | integer | No | Must be `>= 0` | Total rounds won by the away team in the game | `12` |
| `total_round` | integer | No | Must be `>= 0` | Total number of rounds played in the game | `26` |
| `normalized_score_diff` | float | Yes | Must be in range `-1` and `1` | Normalized difference between home and away round scores | `0.07692...` |
| `home_atk_score` | integer | No | Must be `>= 0` | Number of rounds won by the home team while attacking | `5` |
| `away_atk_score` | integer | No | Must be `>= 0` | Number of rounds won by the away team while attacking | `4` |
| `atk_wr_ratio` | float | Yes | Must be in range `-1` and `1` | Ratio comparing the attacking-side win rates of the home and away teams | `1.25` |
| `home_def_score` | integer | No | Must be `>= 0` | Number of rounds won by the home team while defending | `9` |
| `away_def_score` | integer | No | Must be `>= 0` | Number of rounds won by the away team while defending | `8` |
| `def_wr_ratio` | float | Yes | Must be in range `-1` and `1` | Ratio comparing the defending-side win rates of the home and away teams | `1.125` |
| `home_ot_score` | integer | Yes | Must be `>= 0` when present | Number of overtime rounds won by the home team | `2` |
| `away_ot_score` | integer | Yes | Must be `>= 0` when present | Number of overtime rounds won by the away team | `0` |
| `normalized_ot_score_diff` | float | Yes | Must be in range `-1` and `1` | Rate representing the relative overtime round performance between the home and away teams | `1.0` |
| `home_pstl_win` | integer | Yes | Must be in range `0` and `2` when present | Number of pistol rounds won by the home team | `0` |
| `away_pstl_win` | integer | Yes | Must be in range `0` and `2` when present | Number of pistol rounds won by the away team | `2` |
| `pstl_win_diff` | integer | Yes | Must be in range `-2` and `2` when present | Difference between the number of pistol rounds won by the home and away teams | `-2` |
| `home_eco_round` | integer | Yes |Must be `>= 0` | Number of eco rounds played by the home team | `4` |
| `away_eco_round` | integer | Yes | Must be `>= 0` | Number of eco rounds played by the away team | `2` |
| `home_eco_win` | integer | Yes |Must be `>= 0` | Number of eco rounds won by the home team | `1` |
| `away_eco_win` | integer | Yes | Must be `>= 0` | Number of eco rounds won by the away team | `2` |
| `eco_wr_diff` | float | Yes | Must be in range `-1` and `1` | Relative difference in eco-round win rate between the home and away teams | `-0.75` |
| `home_semi_eco_round` | integer | Yes |Must be `>= 0` | Number of semi eco rounds played by the home team | `1` |
| `away_semi_eco_round` | integer | Yes | Must be `>= 0` | Number of semi eco rounds played by the away team | `1` |
| `home_semi_eco_win` | integer | Yes |Must be `>= 0` | Number of semi eco rounds win by the home team | `1` |
| `away_semi_eco_win` | integer | Yes | Must be `>= 0` | Number of semi eco rounds win by the away team | `0` |
| `semi_eco_wr_diff` | float | Yes | Must be in range `-1` and `1` | Relative difference in semi-eco-round win rate between the home and away teams | `1.0` |
| `home_semi_buy_round` | integer | Yes |Must be `>= 0` | Number of semi buy rounds played by the home team | `1` |
| `away_semi_buy_round` | integer | Yes | Must be `>= 0` | Number of semi buy rounds played by the away team | `9` |
| `home_semi_buy_win` | integer | Yes |Must be `>= 0` | Number of semi buy rounds win by the home team | `1` |
| `away_semi_buy_win` | integer | Yes | Must be `>= 0` | Number of semi buy rounds win by the away team | `4` |
| `semi_buy_wr_diff` | float | Yes | Must be in range `-1` and `1` | Relative difference in semi-buy-round win rate between the home and away teams | `0.5555...` |
| `home_full_buy_round` | integer | Yes |Must be `>= 0` | Number of full buy rounds played by the home team | `20` |
| `away_full_buy_round` | integer | Yes | Must be `>= 0` | Number of full buy rounds played by the away team | `14` |
| `home_full_buy_win` | integer | Yes |Must be `>= 0` | Number of full buy rounds win by the home team | `11` |
| `away_full_buy_win` | integer | Yes | Must be `>= 0` | Number of full buy rounds win by the home team | `6` |
| `full_buy_wr_diff` | float | Yes | Must be in range `-1` and `1` | Relative difference in full-buy-round win rate between the home and away teams | `0.1214...` |
| `is_home_win` | integer | No | Must be in range `0` and `1` and can be NULL when denominator `away_n_last_match` is zero | Boolean represent home team win status | `1` |

### fact_map_vetos

| Property | Description |
|---|---|
| Purpose | Map vetos order by game fact table |
| Grain | One row per map vetos order by game |
| Primary Key | None |
| Partition | None |
| Main Dimensions | `match_id`, `team_id`, `map_id` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `match_id` | string | No | None | Match FK | `102885` |
| `map_id` | integer | No | None | Map FK | `1` |
| `team_id` | integer | No | None | Team FK | `45` |
| `action` | string | No | None | Type of map veto action performed | `ban` |
| `action_order` | integer | No | None | Sequential order of the veto action for a team and action type | `1` |

### fact_players

| Property | Description |
|---|---|
| Purpose | Player by game-level cleaned and transformed table |
| Grain | One row per player per game |
| Primary Key | None |
| Partition | `match_date` |
| Main Dimensions | `game_id`, `player_id`, `team_id`, `agent_id` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `tour_id` | string | No | None | Tournament FK | `1658` |
| `match_id` | string | No | None | Match FK | `59970` |
| `game_id` | string | No | None | Game FK | `134551` |
| `match_date` | date | No | None | Match calendar date | `2024-05-04` |
| `match_datetime` | datetime | No | None | Match timestamp | `2024-05-04T19:20:00` |
| `map_id` | integer | No | None | Map FK | `10` |
| `player_id` | integer | No | None | Player FK | `66` |
| `team_id` | integer | No | None | Team FK | `1` |
| `agent_id` | integer | No | None | Agent FK | `10` |
| `is_win` | integer | No | None | Binary indicator equal to 1 when the player's team won the game | `1` |
| `mod` | integer | No | None | Statistical aggregation mode indicating whether the player statistics | `atk` |
| `r` | integer | Yes | Must be `> 0` when present | Player rating for the game | `1.09` |
| `acs` | integer | Yes | Must be `> 0` when present | Average Combat Score (ACS) achieved by the player in the game | `164` |
| `k` | integer | Yes | Must be `> 0` when present | Number of kills recorded by the player in the game | `8` |
| `d` | integer | Yes | Must be `>= 0` when present | Number of deaths recorded by the player in the game | `10` |
| `a` | integer | Yes | Must be `>= 0` when present | Number of assists recorded by the player in the game | `4` |
| `kd` | integer | Yes | `k - d` when present | Kill-to-death diff of the player in the game | `-2` |
| `kast` | integer | Yes | Must be `> 0` when present | Percentage of rounds in which the player recorded a kill, assist, survived, or was traded | `62` |
| `adr` | integer | Yes | Must be `> 0` when present | Average Damage per Round (ADR) achieved by the player | `131` |
| `hs` | integer | Yes | Must be `>= 0` when present | Percentage of the player's kills that were headshots | `33` |
| `fk` | integer | Yes | Must be `>= 0` when present | Number of first kills recorded by the player | `0` |
| `fd` | integer | Yes | Must be `>= 0` when present | Number of first deaths recorded by the player | `0` |
| `fkfd` | integer | Yes | `fk - fd` when present | First-kill to first-death diff of the player | `0` |

### team_games_performance

| Property | Description |
|---|---|
| Purpose | team by game-level performance view |
| Grain | One row per team per game |
| Primary Key | None |
| Partition | None |
| Main Dimensions | `game_id`, `map_id`, `team_id` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `tour_id` | string | No | None | Tournament FK | `2004` |
| `match_id` | string | No | None | Match FK | `71657` |
| `game_id` | string | No | None | Game FK | `163433` |
| `map_id` | integer | No | None | Map FK | `4` |
| `team_id` | integer | No | None | Team FK | `30` |
| `is_ot` | integer | No | Must be in range `0` and `1` | Binary indicator equal to 1 when the game went to overtime | `1` |
| `is_win` | integer | No | Must be in range `0` and `1` | Binary indicator equal to 1 when the team won the game | `1` |
| `game_duration` | integer | Yes | Must be `>= 0` when present | Duration of the game in seconds | `3456` |
| `normalized_score_diff` | float | No | Must be in range `-1` and `1` | Normalized score difference from the perspective of the team | `0.08` |
| `atk_wr` | float | Yes | Must be in range `0` and `1` | Attacking-side round win rate of the team | `0.38` |
| `def_wr` | float | Yes | Must be in range `0` and `1` | Defending-side round win rate of the team | `0.69` |
| `pstl_wr` | float | Yes | Must be in range `0` and `1` | Pistol-round win rate of the team | `0.0` |
| `eco_wr` | float | Yes | Must be in range `0` and `1` | Eco-round win rate of the team | `0.25` |
| `semi_eco_wr` | float | Yes | Must be in range `0` and `1` | Semi-eco-round win rate of the team | `1.0` |
| `semi_buy_wr` | float | Yes | Must be in range `0` and `1` | Semi-buy-round win rate of the team | `1.0` |
| `full_buy_wr` | float | Yes | Must be in range `0` and `1` | Full-buy-round win rate of the team | `0.55` |

### team_maps_performance

| Property | Description |
|---|---|
| Purpose | team by game-level performance view |
| Grain | One row per team per game |
| Primary Key | None |
| Partition | None |
| Main Dimensions | `team_id`, `map_id` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `team_id` | string | No | None | Tournament FK | `30` |
| `map_id` | integer | No | None | Map FK | `4` |
| `map_played` | integer | No | None | Total map played by team | `6` |
| `ot_played` | integer | No | Must be in range `0` and `1` | Total Overtime played on the map by team | `1` |
| `ot_rate` | float | No | Must be in range `0` and `1` | Overtime rate played on the map by team | `` |
| `maps_win` | integer | No | Must be in range `0` and `1` | Total win on the map by team | `3` |
| `map_wr` | integer | Yes | Must be `>= 0` when present | Map win rate by team on the map | `0.5` |
| `pick_count` | integer | No | Must be in range `-1` and `1` | Total map pick by team over total team matches | `2` |
| `ban_count` | integer | No | Must be in range `0` and `1` | Total map ban by team over total team matches | `3` |
| `pick_rate` | float | Yes | Must be in range `0` and `1` | Map pick rate by team | `0.04` |
| `ban_rate` | float | Yes | Must be in range `0` and `1` | Map ban rate by team | `0.1` |
| `map_pick_preference` | float | Yes | Must be in range `0` and `1` | Map pick rate by team when the map is not picked by opponent and banned by both team | `0.29` |
| `avg_game_duration` | float | Yes | Must be in range `0` and `1` | Duration aggregation of game on the map by team | `2938.33` |
| `avg_normalized_score_diff` | float | Yes | Must be in range `0` and `1` | Normalized aggregation score difference from the perspective of the team | `0.01` |
| `avg_atk_wr` | float | Yes | Must be in range `0` and `1` | Aggregation of attacking-side round win rate of the team on the map | `0.46` |
| `avg_def_wr` | float | Yes | Must be in range `0` and `1` | Aggregation of defending-side round win rate of the team on the map | `0.54` |
| `avg_pstl_wr` | float | Yes | Must be in range `0` and `1` | Aggregation of pistol-round win rate of the team on the map | `0.33` |
| `avg_eco_wr` | float | Yes | Must be in range `0` and `1` | Aggregation of eco-round win rate of the team on the map | `0.32` |
| `avg_semi_eco_wr` | float | Yes | Must be in range `0` and `1` | Aggregation of semi-eco-round win rate of the team on the map | `0.3` |
| `avg_semi_buy_wr` | float | Yes | Must be in range `0` and `1` | Aggregation of semi-buy-round win rate of the team on the map | `0.63` |
| `avg_full_buy_wr` | float | Yes | Must be in range `0` and `1` | Aggregation of full-buy-round win rate of the team on the map | `0.57` |

### maps_performance

| Property | Description |
|---|---|
| Purpose | team by game-level performance view |
| Grain | One row per team per game |
| Primary Key | None |
| Partition | None |
| Main Dimensions | `map_id` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `map_id` | integer | No | None | Map FK | `4` |
| `map_played` | integer | No | None | Total map played | `172` |
| `ot_played` | integer | No | Must be in range `0` and `1` | Total overtime played on the map | `24` |
| `ot_rate` | float | No | Must be in range `0` and `1` | Overtime rate played on the map | `` |
| `pick_count` | integer | No | Must be in range `-1` and `1` | total map pick over total matches | `139` |
| `ban_count` | integer | No | Must be in range `0` and `1` | total map ban over total matches | `341` |
| `pick_rate` | float | Yes | Must be in range `0` and `1` | Map pick rate over total matches played | `0.11` |
| `ban_rate` | float | Yes | Must be in range `0` and `1` | Map ban rate over total matches played | `0.27` |
| `map_pick_preference` | float | Yes | Must be in range `0` and `1` | Map pick rate by team when the map is not banned by both team | `0.29` |
| `avg_game_duration` | float | Yes | Must be in range `0` and `1` | Duration aggregation of game on the map by team | `2813.5` |
| `atk_side_ratio` | float | Yes | Must be in range `0` and `1` | Attacking-side win ratio on the map | `0.5` |
| `def_side_ratio` | float | Yes | Must be in range `0` and `1` | Defending-side win ratio on the map | `0.5` |

### players_agents_maps_performance

| Property | Description |
|---|---|
| Purpose | player by agent and map performance view |
| Grain | One row per player per agent per map |
| Primary Key | None |
| Partition | None |
| Main Dimensions | `player_id`, `map_id`, `agent_id` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `player_id` | integer | No | None | Player FK | `1` |
| `agent_id` | integer | No | None | Agent FK | `17` |
| `map_id` | integer | No | None | Map FK | `9` |
| `agent_played` | integer | No | Must be `>= 0` | Total agent played | `6` |
| `total_win` | integer | No | Must be `>= 0` | Total win with the agent played | `1` |
| `agent_wr` | float | No | Must be in range `0` and `1` | Agent win rate | `0.17` |
| `avg_r` | float | Yes | Must be in range `0` and `1` | Average player rating | `0.87` |
| `avg_acs` | float | Yes | Must be in range `0` and `1` | Average player ACS | `159.00` |
| `avg_k` | float | Yes | Must be in range `0` and `1` | Average player kills | `12.50` |
| `avg_d` | float | Yes | Must be in range `0` and `1` | Average player deaths | `15.33` |
| `avg_a` | float | Yes | Must be in range `0` and `1` | Average player assists | `8.17` |
| `avg_kd` | float | Yes | Must be in range `0` and `1` | Average kill-to-death diff of the player in the game | `-2.83` |
| `avg_kast` | float | Yes | Must be in range `0` and `1` | Average percentage of rounds in which the player recorded a kill, assist, survived, or was traded | `66.5` |
| `avg_adr` | float | Yes | Must be in range `0` and `1` | Average ADR achieved by the player | `101.67` |
| `avg_hs` | float | Yes | Must be in range `0` and `1` | Average percentage of the player's kills that were headshots | `25.83` |
| `avg_fk` | float | Yes | Must be in range `0` and `1` | Average player first kills | `1.17` |
| `avg_fd` | float | Yes | Must be in range `0` and `1` | Average player first deaths | `2.17` |
| `avg_fkfd` | float | Yes | Must be in range `0` and `1` | Average first kill-to-first death diff of the player in the game | `-1.0` |

### agents_maps_performance

| Property | Description |
|---|---|
| Purpose | agent by map-level performance view |
| Grain | One row per agent per map |
| Primary Key | None |
| Partition | None |
| Main Dimensions | `map_id`, `agent_id` |


| Column | Data Type | Nullable | Business Rule | Description | Example |
|---|---|---|---|---|---|
| `agent_id` | integer | No | None | Agent FK | `16` |
| `map_id` | integer | No | None | Map FK | `6` |
| `presence_count` | integer | No | Must be `>= 0` | Total agent presence on the map | `103` |
| `map_played` | integer | No | Must be `>= 0` | Total map played with the agent | `138` |
| `pick_count` | integer | No | Must be `>= 0` | Total agent pick on the map | `160` |
| `total_win` | integer | No | Must be `>= 0` | Total agent win on the map | `88` |
| `pick_rate` | float | Yes | Must be in range `0` and `1` | Agent pick rate on the map | `1.16` |
| `win_rate` | float | Yes | Must be in range `0` and `1` | Agent win rate on the map | `0.85` |
| `presence_rate` | float | Yes | Must be in range `0` and `1` | Agent presence rate on the map | `0.75` |

### agents_performance

| Property | Description |
|---|---|
| Purpose | agent performance view |
| Grain | One row per agent |
| Primary Key | None |
| Partition | None |
| Main Dimensions | `agent_id` |


| Source Model | Source Field | Target Model | Target Field | Transformation | Description |
|---|---|---|---|---|---|
| `agent_id` | integer | No | None | Agent FK | `17` |
| `pick_count` | integer | No | Must be `>= 0` | Total agent pick on the map | `6` |
| `total_games` | integer | No | Must be `>= 0` | Total map played with the agent | `6` |
| `pick_rate` | float | Yes | Must be in range `0` and `1` | Agent pick rate on the map | `1.0` |
| `win_rate` | float | Yes | Must be in range `0` and `1` | Agent win rate on the map | `0.17` |
