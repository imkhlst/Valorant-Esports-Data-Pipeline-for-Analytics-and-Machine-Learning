{{ config(
    materialized='view'
) }}

SELECT
    tour_id,
    match_id,
    game_id,
    map_id,
    home_team_id AS team_id,
    
    CASE
        WHEN home_ot_score + away_ot_score > 0
        THEN 1
        ELSE 0
    END AS is_ot,

    is_home_win AS is_win,
    game_duration,
    normalized_score_diff,
    
    home_atk_score * 1.0 / NULLIF(home_atk_score + away_def_score, 0) AS atk_wr,
    home_def_score * 1.0 / NULLIF(home_def_score + away_atk_score, 0) AS def_wr,
    home_pstl_win * 1.0 / NULLIF(home_pstl_win + away_pstl_win, 0) AS pstl_wr,
    home_eco_win * 1.0 / NULLIF(home_eco_round, 0) AS eco_wr,
    home_semi_eco_win * 1.0 / NULLIF(home_semi_eco_round, 0) AS semi_eco_wr,
    home_semi_buy_win * 1.0 / NULLIF(home_semi_buy_round, 0) AS semi_buy_wr,
    home_full_buy_win * 1.0 / NULLIF(home_full_buy_round, 0) AS full_buy_wr
FROM {{ ref('fact_games') }}
UNION ALL
SELECT
    tour_id,
    match_id,
    game_id,
    map_id,
    away_team_id AS team_id,
    
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
    normalized_score_diff * (-1.0) AS normalized_score_diff,
    
    away_atk_score * 1.0 / NULLIF(home_def_score + away_atk_score, 0),
    away_def_score * 1.0 / NULLIF(home_atk_score + away_def_score, 0),
    away_pstl_win * 1.0 / NULLIF(home_pstl_win + away_pstl_win, 0),
    away_eco_win * 1.0 / NULLIF(away_eco_round, 0),
    away_semi_eco_win * 1.0 / NULLIF(away_semi_eco_round, 0),
    away_semi_buy_win * 1.0 / NULLIF(away_semi_buy_round, 0),
    away_full_buy_win * 1.0 / NULLIF(away_full_buy_round, 0)
FROM {{ ref('fact_games') }}