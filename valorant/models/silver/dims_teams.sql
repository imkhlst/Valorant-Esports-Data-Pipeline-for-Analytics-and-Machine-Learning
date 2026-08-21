SELECT ROW_NUMBER() OVER (ORDER BY team_name) AS team_id, team_name, team_alias, team_region
FROM(
    SELECT DISTINCT
        home_name as team_name,
        home_alias as team_alias,
        t.tour_region as team_region,
    FROM {{ ref('matches') }} m
    JOIN {{ ref('dims_tours') }} t
    ON m.tour_id = t.tour_id
)
WHERE team_region != 'World'