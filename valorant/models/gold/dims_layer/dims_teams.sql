WITH region AS (
    SELECT
        home_id AS team_id,
        t.tour_region AS team_region
    FROM {{ ref('matches') }} m
    JOIN {{ ref('dims_tours') }} t
    ON m.tour_id = t.tour_id
    WHERE t.tour_region != 'World'
    UNION DISTINCT
    SELECT
        away_id AS team_id,
        t.tour_region AS team_region
    FROM {{ ref('matches') }} m
    JOIN {{ ref('dims_tours') }} t
    ON m.tour_id = t.tour_id
    WHERE t.tour_region != 'World'
)

SELECT
    SAFE_CAST(t.team_id AS INT64) AS team_id,
    SAFE_CAST(t.team_name AS STRING) AS team_name,
    SAFE_CAST(team_alias AS STRING) AS team_alias,
    SAFE_CAST(team_country AS STRING) AS team_country,
    r.team_region AS team_region,
    SAFE_CAST(t.scraped_at AS TIMESTAMP) AS scraped_at,
    SAFE_CAST(t.ingested_at AS TIMESTAMP) AS ingested_at,
    SAFE_CAST(t.updated_at AS TIMESTAMP) AS updated_at
FROM {{ source('bronze', 'teams') }} t
JOIN region r
ON r.team_id = SAFE_CAST(t.team_id AS INT64)