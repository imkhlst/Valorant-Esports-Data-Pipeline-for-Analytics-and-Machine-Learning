SELECT
    SAFE_CAST(o.match_id AS STRING) AS match_id,
    SAFE_CAST(game_id AS STRING) AS game_id,

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

    SAFE_CAST(NULLIF(game_map, '-') AS STRING) AS game_map,

    CASE
        WHEN LENGTH(game_duration) = 5
        THEN TIME_DIFF(PARSE_TIME('%M:%S', game_duration), '00:00:00', SECOND)
        WHEN LENGTH(game_duration) = 8
        THEN TIME_DIFF(PARSE_TIME('%H:%M:%S', game_duration), '00:00:00', SECOND)
        ELSE NULL
    END AS game_duration,

    SAFE_CAST(o.home_score AS INT64) AS home_score,
    SAFE_CAST(o.away_score AS INT64) AS away_score,
    SAFE_CAST(home_atk_score AS INT64) AS home_atk_score,
    SAFE_CAST(away_atk_score AS INT64) AS away_atk_score,
    SAFE_CAST(home_def_score AS INT64) AS home_def_score,
    SAFE_CAST(away_def_score AS INT64) AS away_def_score,
    SAFE_CAST(home_ot_score AS INT64) AS home_ot_score,
    SAFE_CAST(away_ot_score AS INT64) AS away_ot_score
FROM {{ source('bronze', 'games_overview') }} o
JOIN {{ source('bronze', 'matches') }} m
ON o.match_id = m.match_id