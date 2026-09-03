SELECT
    SAFE_CAST(tour_id AS INT64) AS tour_id,
    SAFE_CAST(tour_name AS STRING) AS tour_name,
    SAFE_CAST(tour_tag AS STRING) AS tour_tag,

    CASE
        WHEN SAFE_CAST(tour_stage AS STRING) NOT IN (
            'Stage 1',
            'Stage 2',
            'Champions'
        )
        THEN 'Masters'
        ELSE SAFE_CAST(tour_stage AS STRING)
    END AS tour_stage,

    CASE
        WHEN SAFE_CAST(tour_region AS STRING) = 'Masters'
        THEN 'World'
        ELSE SAFE_CAST(tour_region AS STRING)
    END AS tour_region,

    SAFE_CAST(tour_status AS STRING) AS tour_status
FROM {{ source('bronze', 'tours') }}