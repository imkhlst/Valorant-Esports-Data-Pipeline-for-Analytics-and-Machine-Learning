{{ config(
    materialized='view'
) }}

SELECT
    match_date,
    f.tour_id,
    tu.tour_name,
    tu.tour_region,
    match_id,
    game_id,
    f.map_id,
    m.map_name,
    home_team_id AS team_id,
    te.team_name,
    
    CASE
        WHEN home_ot_score + away_ot_score > 0
        THEN 1
        ELSE 0
    END AS is_ot,

    is_home_win AS is_win,
    game_duration,
    
    home_atk_score * 1.0 / NULLIF(home_atk_score + away_def_score, 0) AS atk_wr,
    home_def_score * 1.0 / NULLIF(home_def_score + away_atk_score, 0) AS def_wr,
    home_pstl_win * 1.0 / NULLIF(home_pstl_win + away_pstl_win, 0) AS pstl_wr,
    home_eco_win * 1.0 / NULLIF(home_eco_round, 0) AS eco_wr,
    home_semi_eco_win * 1.0 / NULLIF(home_semi_eco_round, 0) AS semi_eco_wr,
    home_semi_buy_win * 1.0 / NULLIF(home_semi_buy_round, 0) AS semi_buy_wr,
    home_full_buy_win * 1.0 / NULLIF(home_full_buy_round, 0) AS full_buy_wr
FROM {{ ref('fact_games') }} f 
JOIN {{ ref('dims_tours') }} tu
ON f.tour_id = tu.tour_id
JOIN {{ ref('dims_maps') }} m
ON f.map_id = m.map_id
JOIN {{ ref('dims_teams') }} te
ON f.home_team_id = te.team_id
UNION ALL
SELECT
    match_date,
    f.tour_id,
    tu.tour_name,
    tu.tour_region,
    match_id,
    game_id,
    f.map_id,
    m.map_name,
    away_team_id AS team_id,
    te.team_name,
    
    CASE
        WHEN home_ot_score + away_ot_score > 0
        THEN 1
        ELSE 0
    END AS is_ot,

    CASE
        WHEN is_home_win = 1
        THEN 0
        ELSE 1
    END AS is_win,

    game_duration,
    
    away_atk_score * 1.0 / NULLIF(home_def_score + away_atk_score, 0),
    away_def_score * 1.0 / NULLIF(home_atk_score + away_def_score, 0),
    away_pstl_win * 1.0 / NULLIF(home_pstl_win + away_pstl_win, 0),
    away_eco_win * 1.0 / NULLIF(away_eco_round, 0),
    away_semi_eco_win * 1.0 / NULLIF(away_semi_eco_round, 0),
    away_semi_buy_win * 1.0 / NULLIF(away_semi_buy_round, 0),
    away_full_buy_win * 1.0 / NULLIF(away_full_buy_round, 0)
FROM {{ ref('fact_games') }} f 
JOIN {{ ref('dims_tours') }} tu
ON f.tour_id = tu.tour_id
JOIN {{ ref('dims_maps') }} m
ON f.map_id = m.map_id
JOIN {{ ref('dims_teams') }} te
ON f.away_team_id = te.team_id