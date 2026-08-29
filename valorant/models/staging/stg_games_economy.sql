SELECT
    SAFE_CAST(e.match_id AS INT64) AS match_id,
    SAFE_CAST(game_id AS INT64) AS game_id,
    
    SAFE.PARSE_DATETIME(
        '%Y-%m-%d %H:%M:%S',
        m.date 
    ) AS match_datetime,

    DATE(
        SAFE.PARSE_DATETIME(
            '%Y-%m-%d %H:%M:%S',
            m.date
        ) 
    ) AS match_date,

    SAFE_CAST(home_pstl_win AS INT64) AS home_pstl_win,
    SAFE_CAST(away_pstl_win AS INT64) AS away_pstl_win,
    SAFE_CAST(home_eco_round AS INT64) AS home_eco_round,
    SAFE_CAST(away_eco_round AS INT64) AS away_eco_round,
    SAFE_CAST(home_eco_win AS INT64) AS home_eco_win,
    SAFE_CAST(away_eco_win AS INT64) AS away_eco_win,
    SAFE_CAST(home_semi_eco_round AS INT64) AS home_semi_eco_round,
    SAFE_CAST(away_semi_eco_round AS INT64) AS away_semi_eco_round,
    SAFE_CAST(home_semi_eco_win AS INT64) AS home_semi_eco_win,
    SAFE_CAST(away_semi_eco_win AS INT64) AS away_semi_eco_win,
    SAFE_CAST(home_semi_buy_round AS INT64) AS home_semi_buy_round,
    SAFE_CAST(away_semi_buy_round AS INT64) AS away_semi_buy_round,
    SAFE_CAST(home_semi_buy_win AS INT64) AS home_semi_buy_win,
    SAFE_CAST(away_semi_buy_win AS INT64) AS away_semi_buy_win,
    SAFE_CAST(home_full_buy_round AS INT64) AS home_full_buy_round,
    SAFE_CAST(away_full_buy_round AS INT64) AS away_full_buy_round,
    SAFE_CAST(home_full_buy_win AS INT64) AS home_full_buy_win,
    SAFE_CAST(away_full_buy_win AS INT64) AS away_full_buy_win
FROM {{ source('bronze', 'games_economy') }} e
JOIN {{ source('bronze', 'matches') }} m
ON m.match_id = e.match_id