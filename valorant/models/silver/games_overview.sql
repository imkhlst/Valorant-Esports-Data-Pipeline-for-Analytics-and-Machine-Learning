SELECT
    match_id,
    game_id,
    match_date,
    match_datetime,
    game_map,
    
    CASE
        WHEN game_duration > 0
        THEN game_duration
        ELSE NULL
    END AS game_duration,

    CASE
        WHEN home_score >= 0
        THEN home_score
        ELSE NULL
    END AS home_score,

    CASE
        WHEN away_score >= 0
        THEN away_score
        ELSE NULL
    END AS away_score,

    CASE
        WHEN home_atk_score >= 0
        THEN home_atk_score
        ELSE NULL
    END AS home_atk_score,

    CASE
        WHEN away_atk_score >= 0
        THEN away_atk_score
        ELSE NULL
    END AS away_atk_score,

    CASE
        WHEN home_def_score >= 0
        THEN home_def_score
        ELSE NULL
    END AS home_def_score,

    CASE
        WHEN away_def_score >= 0
        THEN away_def_score
        ELSE NULL
    END AS away_def_score,

    CASE
        WHEN home_ot_score >= 0
        THEN home_ot_score
        ELSE NULL
    END AS home_ot_score,

    CASE
        WHEN away_ot_score >= 0
        THEN away_ot_score
        ELSE NULL
    END AS away_ot_score
FROM {{ ref('stg_games_overview') }}