SELECT
    SAFE_CAST(p.game_id AS INT64) AS game_id,
    o.match_date,
    o.match_datetime,
    SAFE_CAST(name AS STRING) AS player_name,
    SAFE_CAST(team_alias AS STRING) AS team_alias,
    SAFE_CAST(nationality AS STRING) AS nationality,
    SAFE_CAST(agent AS STRING) AS agent,
    SAFE_CAST(mod AS STRING) AS mod,

    CASE
        WHEN SAFE_CAST(r AS FLOAT64) > 0
        THEN SAFE_CAST(r AS FLOAT64)
        ELSE NULL
    END AS r,

    CASE
        WHEN SAFE_CAST(acs AS INT64) BETWEEN 1 AND 1000
        THEN SAFE_CAST(acs AS INT64)
        ELSE NULL
    END AS acs,
    
    CASE
        WHEN SAFE_CAST(k AS INT64) >= 0
        THEN SAFE_CAST(k AS INT64)
        ELSE NULL
    END AS k,

    CASE
        WHEN SAFE_CAST(d AS INT64) >= 0
        THEN SAFE_CAST(d AS INT64)
        ELSE NULL
    END AS d,
    
    CASE
        WHEN SAFE_CAST(a AS INT64) >= 0
        THEN SAFE_CAST(a AS INT64)
        ELSE NULL
    END AS a,

    CASE
        WHEN SAFE_CAST(kd AS INT64) = (SAFE_CAST(k AS INT64) - SAFE_CAST(d AS INT64))
        THEN SAFE_CAST(kd AS INT64)
        ELSE NULL
    END AS kd,

    CASE
        WHEN SAFE_CAST(kast AS INT64) BETWEEN 1 AND 100
        THEN SAFE_CAST(kast AS INT64)
        ELSE NULL
    END AS kast,

    CASE
        WHEN SAFE_CAST(adr AS INT64) > 0
        THEN SAFE_CAST(adr AS INT64)
        ELSE NULL
    END AS adr,

    CASE
        WHEN SAFE_CAST(hs AS INT64) BETWEEN 0 AND 100
        THEN SAFE_CAST(hs AS INT64)
        ELSE NULL
    END AS hs,

    CASE
        WHEN SAFE_CAST(fk AS INT64) >= 0
        THEN SAFE_CAST(fk AS INT64)
        ELSE NULL
    END AS fk,

    CASE
        WHEN SAFE_CAST(fd AS INT64) >= 0
        THEN SAFE_CAST(fd AS INT64)
        ELSE NULL
    END AS fd,

    CASE
        WHEN SAFE_CAST(fkfd AS INT64) = (SAFE_CAST(fk AS INT64) - SAFE_CAST(fd AS INT64))
        THEN SAFE_CAST(fkfd AS INT64)
        ELSE NULL
    END AS fkfd
FROM {{ source('bronze', 'players') }} p
JOIN {{ ref('games_overview') }} o
ON SAFE_CAST(p.game_id AS INT64) = o.game_id