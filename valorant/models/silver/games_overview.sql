WITH duration AS(
    SELECT
        game_id,

        CASE
            WHEN LENGTH(game_duration) = 5
            THEN TIME_DIFF(PARSE_TIME('%M:%S', game_duration), '00:00:00', SECOND) / 60
            WHEN LENGTH(game_duration) = 8
            THEN TIME_DIFF(PARSE_TIME('%H:%M:%S', game_duration), '00:00:00', SECOND) / 60
            ELSE NULL
        END AS game_duration
    FROM {{ source('bronze', 'games_overview')}}
)

SELECT
    SAFE_CAST(o.match_id AS INT64) AS match_id,
    SAFE_CAST(o.game_id AS INT64) AS game_id,

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
        WHEN d.game_duration > 0
        THEN d.game_duration
        ELSE NULL
    END AS game_duration,

    CASE
        WHEN SAFE_CAST(o.home_score AS INT64) >= 0
        THEN SAFE_CAST(o.home_score AS INT64)
        ELSE NULL
    END AS home_score,

    CASE
        WHEN SAFE_CAST(o.away_score AS INT64) >= 0
        THEN SAFE_CAST(o.away_score AS INT64)
        ELSE NULL
    END AS away_score,

    CASE
        WHEN SAFE_CAST(home_atk_score AS INT64) >= 0
        THEN SAFE_CAST(home_atk_score AS INT64)
        ELSE NULL
    END AS home_atk_score,

    CASE
        WHEN SAFE_CAST(away_atk_score AS INT64) >= 0
        THEN SAFE_CAST(away_atk_score AS INT64)
        ELSE NULL
    END AS away_atk_score,

    CASE
        WHEN SAFE_CAST(home_def_score AS INT64) >= 0
        THEN SAFE_CAST(home_def_score AS INT64)
        ELSE NULL
    END AS home_def_score,

    CASE
        WHEN SAFE_CAST(away_def_score AS INT64) >= 0
        THEN SAFE_CAST(away_def_score AS INT64)
        ELSE NULL
    END AS away_def_score,

    CASE
        WHEN SAFE_CAST(home_ot_score AS INT64) >= 0
        THEN SAFE_CAST(home_ot_score AS INT64)
        ELSE NULL
    END AS home_ot_score,

    CASE
        WHEN SAFE_CAST(away_ot_score AS INT64) >= 0
        THEN SAFE_CAST(away_ot_score AS INT64)
        ELSE NULL
    END AS away_ot_score
FROM {{ source('bronze', 'games_overview') }} o
JOIN {{ source('bronze', 'matches') }} m
ON o.match_id = m.match_id
JOIN duration d
ON o.game_id = d.game_id