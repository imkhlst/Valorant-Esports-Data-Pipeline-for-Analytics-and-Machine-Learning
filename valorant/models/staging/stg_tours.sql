SELECT
    SAFE_CAST(tour_id AS INT64) AS tour_id,
    SAFE_CAST(tour_name AS STRING) AS tour_name,
    SAFE_CAST(tour_tag AS STRING) AS tour_tag,
    SAFE_CAST(tour_stage AS STRING) AS tour_stage,
    SAFE_CAST(tour_region AS STRING) AS tour_region,
    SAFE_CAST(tour_status AS STRING) AS tour_status
FROM {{ source('bronze', 'tours') }}