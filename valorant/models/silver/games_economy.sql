SELECT
    match_id,
    game_id,
    match_date,
    match_datetime,
    
    CASE
        WHEN home_pstl_win BETWEEN 0 AND 2
        THEN home_pstl_win
        ELSE NULL
    END AS home_pstl_win,

    CASE
        WHEN away_pstl_win BETWEEN 0 AND 2
        THEN away_pstl_win
        ELSE NULL
    END AS away_pstl_win,

    CASE
        WHEN home_eco_round >= 0
        THEN home_eco_round
        ELSE NULL
    END AS home_eco_round,

    CASE
        WHEN away_eco_round >= 0
        THEN away_eco_round
        ELSE NULL
    END AS away_eco_round,

    CASE
        WHEN home_eco_win >= 0
        THEN home_eco_win
        ELSE NULL
    END AS home_eco_win,

    CASE
        WHEN away_eco_win >= 0
        THEN away_eco_win
        ELSE NULL
    END AS away_eco_win,

    CASE
        WHEN home_semi_eco_round >= 0
        THEN home_semi_eco_round
        ELSE NULL
    END AS home_semi_eco_round,

    CASE
        WHEN away_semi_eco_round >= 0
        THEN away_semi_eco_round
        ELSE NULL
    END AS away_semi_eco_round,

    CASE
        WHEN home_semi_eco_win >= 0
        THEN home_semi_eco_win
        ELSE NULL
    END AS home_semi_eco_win,

    CASE
        WHEN away_semi_eco_win >= 0
        THEN away_semi_eco_win
        ELSE NULL
    END AS away_semi_eco_win,

    CASE
        WHEN home_semi_buy_round >= 0
        THEN home_semi_buy_round
        ELSE NULL
    END AS home_semi_buy_round,

    CASE
        WHEN away_semi_buy_round >= 0
        THEN away_semi_buy_round
        ELSE NULL
    END AS away_semi_buy_round,

    CASE
        WHEN home_semi_buy_win >= 0
        THEN home_semi_buy_win
        ELSE NULL
    END AS home_semi_buy_win,

    CASE
        WHEN away_semi_buy_win >= 0
        THEN away_semi_buy_win
        ELSE NULL
    END AS away_semi_buy_win,

    CASE
        WHEN home_full_buy_round >= 0
        THEN home_full_buy_round
        ELSE NULL
    END AS home_full_buy_round,

    CASE
        WHEN away_full_buy_round >= 0
        THEN away_full_buy_round
        ELSE NULL
    END AS away_full_buy_round,

    CASE
        WHEN home_full_buy_win >= 0
        THEN home_full_buy_win
        ELSE NULL
    END AS home_full_buy_win,

    CASE
        WHEN away_full_buy_win >= 0
        THEN away_full_buy_win
        ELSE NULL
    END AS away_full_buy_win
FROM {{ ref('stg_games_economy') }}