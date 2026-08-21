SELECT
    tour_id,
    tour_name,
    tour_tag,

    CASE
        WHEN tour_stage NOT IN (
            'Stage 1',
            'Stage 2',
            'Champions'
        )
        THEN 'Masters'
        ELSE tour_stage
    END AS tour_stage,

    CASE
        WHEN tour_region = 'Masters'
        THEN 'World'
        ELSE tour_region
    END AS tour_region,

    tour_status
FROM {{ ref('stg_tours') }}