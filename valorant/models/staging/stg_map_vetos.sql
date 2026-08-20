SELECT
    SAFE_CAST(match_id AS STRING) AS match_id,
    SAFE_CAST(map_name AS STRING) AS map_name,
    SAFE_CAST(team_name AS STRING) AS team_alias,
    SAFE_CAST(action AS STRING) AS action
FROM {{ source('bronze', 'map_vetos') }}