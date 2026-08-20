SELECT
    SAFE_CAST(tour_id AS STRING) AS tour_id,
    SAFE_CAST(match_id AS STRING) AS match_id,

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
    SAFE_CAST(home_score AS INT64) AS home_score,
    SAFE_CAST(away_score AS INT64) AS away_score,
    SAFE_CAST(home_h2h_win AS INT64) AS home_h2h_win,
    SAFE_CAST(away_h2h_win AS INT64) AS away_h2h_win,
    SAFE_CAST(home_h2h_score AS INT64) AS home_h2h_score,
    SAFE_CAST(away_h2h_score AS INT64) AS away_h2h_score,
    SAFE_CAST(home_n_last_win AS INT64) AS home_n_last_win,
    SAFE_CAST(away_n_last_win AS INT64) AS away_n_last_win,
    SAFE_CAST(home_n_last_match AS INT64) AS home_n_last_match,
    SAFE_CAST(away_n_last_match AS INT64) AS away_n_last_match,
    SAFE_CAST(home_n_last_wr AS FLOAT64) AS home_n_last_wr,
    SAFE_CAST(away_n_last_wr AS FLOAT64) AS away_n_last_wr
FROM {{ source('bronze', 'matches') }}