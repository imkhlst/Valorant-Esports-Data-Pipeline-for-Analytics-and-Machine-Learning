SELECT
    SAFE_CAST(match_id AS INT64) AS match_id,
    SAFE_CAST(map_name AS STRING) AS map_name,
    SAFE_CAST(team_name AS STRING) AS team_alias,
    SAFE_CAST(action AS STRING) AS action,
    SAFE_CAST(scraped_at AS TIMESTAMP) AS scraped_at,
    SAFE_CAST(ingested_at AS TIMESTAMP) AS ingested_at,
    SAFE_CAST(updated_at AS TIMESTAMP) AS updated_at
FROM {{ source('bronze', 'map_vetos') }}