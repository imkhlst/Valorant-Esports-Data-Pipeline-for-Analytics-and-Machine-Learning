SELECT
    game_id,
    player_name,
    team_alias,
    nationality,
    agent,
    mod,

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
        WHEN SAFE_CAST(kd AS INT64) == (SAFE_CAST(k AS INT64) - SAFE_CAST(d AS INT64))
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
        WHEN SAFE_CAST(fkfd AS INT64) == (SAFE_CAST(fk AS INT64) - SAFE_CAST(fd AS INT64))
        THEN SAFE_CAST(fkfd AS INT64)
        ELSE NULL
    END AS fkfd
FROM {{ ref('stg_players') }}