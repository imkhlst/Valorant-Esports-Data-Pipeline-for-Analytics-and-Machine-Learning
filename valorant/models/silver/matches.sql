-- Partitioned update soon
SELECT
    tour_id,
    match_id,
    match_date,
    match_datetime,
    bracket,
    home_name,
    home_alias,
    away_name,
    away_alias,
    bo,
    patch,

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
        WHEN home_h2h_win >= 0
        THEN home_h2h_win
        ELSE NULL
    END AS home_h2h_win,

    CASE
        WHEN away_h2h_win >= 0
        THEN away_h2h_win
        ELSE NULL
    END AS away_h2h_win,

    CASE
        WHEN home_h2h_score >= 0
        THEN home_h2h_score
        ELSE NULL
    END AS home_h2h_score,
    
    CASE
        WHEN away_h2h_score >= 0
        THEN away_h2h_score
        ELSE NULL
    END AS away_h2h_score,

    CASE
        WHEN home_n_last_win BETWEEN 0 AND 5
        THEN home_n_last_win
        ELSE NULL
    END AS home_n_last_win,
    
    CASE
        WHEN away_n_last_win BETWEEN 0 AND 5
        THEN away_n_last_win
        ELSE NULL
    END AS away_n_last_win,

    CASE
        WHEN home_n_last_match BETWEEN 0 AND 5
        THEN home_n_last_match
        ELSE NULL
    END AS home_n_last_match,
    
    CASE
        WHEN away_n_last_match BETWEEN 0 AND 5
        THEN away_n_last_match
        ELSE NULL
    END AS away_n_last_match,
    
    CASE
        WHEN home_n_last_wr BETWEEN 0 AND 1
        THEN home_n_last_wr
        ELSE NULL
    END AS home_n_last_wr,

    CASE
        WHEN away_n_last_wr BETWEEN 0 AND 1
        THEN away_n_last_wr
        ELSE NULL
    END AS away_n_last_wr
FROM {{ ref('stg_matches') }}