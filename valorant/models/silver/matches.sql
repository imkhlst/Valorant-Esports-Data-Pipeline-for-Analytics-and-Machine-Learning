-- Partitioned update soon
SELECT
    SAFE_CAST(tour_id AS INT64) AS tour_id,
    SAFE_CAST(match_id AS INT64) AS match_id,
    
    DATE(
        SAFE.PARSE_DATETIME(
            '%Y-%m-%d %H:%M:%S',
            date
        ) 
    ) AS match_date,
    
    SAFE.PARSE_DATETIME(
        '%Y-%m-%d %H:%M:%S',
        date 
    ) AS match_datetime,
    
    SAFE_CAST(bracket AS STRING) AS bracket,
    SAFE_CAST(home_name AS STRING) AS home_name,
    SAFE_CAST(home_alias AS STRING) AS home_alias,
    SAFE_CAST(away_name AS STRING) AS away_name,
    SAFE_CAST(away_alias AS STRING) AS away_alias,
    SAFE_CAST(bo AS STRING) AS bo,
    SAFE_CAST(patch AS STRING) AS patch,

    CASE
        WHEN SAFE_CAST(home_score AS INT64) >= 0
        THEN SAFE_CAST(home_score AS INT64)
        ELSE NULL
    END AS home_score,

    CASE
        WHEN SAFE_CAST(away_score AS INT64) >= 0
        THEN SAFE_CAST(away_score AS INT64)
        ELSE NULL
    END AS away_score,

    CASE
        WHEN SAFE_CAST(home_h2h_win AS INT64) >= 0
        THEN SAFE_CAST(home_h2h_win AS INT64)
        ELSE NULL
    END AS home_h2h_win,

    CASE
        WHEN SAFE_CAST(away_h2h_win AS INT64) >= 0
        THEN SAFE_CAST(away_h2h_win AS INT64)
        ELSE NULL
    END AS away_h2h_win,

    CASE
        WHEN SAFE_CAST(home_h2h_score AS INT64) >= 0
        THEN SAFE_CAST(home_h2h_score AS INT64)
        ELSE NULL
    END AS home_h2h_score,
    
    CASE
        WHEN SAFE_CAST(away_h2h_score AS INT64) >= 0
        THEN SAFE_CAST(away_h2h_score AS INT64)
        ELSE NULL
    END AS away_h2h_score,

    CASE
        WHEN SAFE_CAST(home_n_last_win AS INT64) BETWEEN 0 AND 5
        THEN SAFE_CAST(home_n_last_win AS INT64)
        ELSE NULL
    END AS home_n_last_win,
    
    CASE
        WHEN SAFE_CAST(away_n_last_win AS INT64) BETWEEN 0 AND 5
        THEN SAFE_CAST(away_n_last_win AS INT64)
        ELSE NULL
    END AS away_n_last_win,

    CASE
        WHEN SAFE_CAST(home_n_last_match AS INT64) BETWEEN 0 AND 5
        THEN SAFE_CAST(home_n_last_match AS INT64)
        ELSE NULL
    END AS home_n_last_match,
    
    CASE
        WHEN SAFE_CAST(away_n_last_match AS INT64) BETWEEN 0 AND 5
        THEN SAFE_CAST(away_n_last_match AS INT64)
        ELSE NULL
    END AS away_n_last_match,
    
    CASE
        WHEN home_n_last_win / NULLIF(home_n_last_match, 0) BETWEEN 0 AND 1
        THEN home_n_last_win / NULLIF(home_n_last_match, 0)
        ELSE NULL
    END AS home_n_last_wr,

    CASE
        WHEN away_n_last_win / NULLIF(away_n_last_match, 0) BETWEEN 0 AND 1
        THEN away_n_last_win / NULLIF(away_n_last_match, 0)
        ELSE NULL
    END AS away_n_last_wr
FROM {{ source('bronze', 'matches') }}