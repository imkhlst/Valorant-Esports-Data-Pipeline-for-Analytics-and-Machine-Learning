SELECT
    SAFE_CAST(player_id AS INT64) AS player_id,
    SAFE_CAST(player_nickname AS STRING) AS nick_name,
    SAFE_CAST(player_realname AS STRING) AS real_name,
    SAFE_CAST(player_nationality AS STRING) AS nationality,
    SAFE_CAST(scraped_at AS TIMESTAMP) AS scraped_at,
    SAFE_CAST(ingested_at AS TIMESTAMP) AS ingested_at,
    SAFE_CAST(updated_at AS TIMESTAMP) AS updated_at
FROM {{ source('bronze', 'players') }}
