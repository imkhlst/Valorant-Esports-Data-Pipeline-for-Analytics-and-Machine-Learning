SELECT ROW_NUMBER() OVER (ORDER BY map_name) AS map_id, map_name
FROM(
    SELECT DISTINCT map_name
    FROM {{ ref('map_vetos') }}
)