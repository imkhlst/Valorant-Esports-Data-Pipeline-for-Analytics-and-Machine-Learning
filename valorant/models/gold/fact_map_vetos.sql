WITH non_decider AS (
    SELECT
        v.match_id,
        m.map_id,
        t.team_id,
        v.action,
        ROW_NUMBER() OVER (PARTITION BY v.match_id, t.team_id, v.action) AS action_order
    FROM {{ ref('stg_map_vetos') }} v
    JOIN {{ ref('dims_teams') }} t
    ON v.team_alias = t.team_alias
    JOIN {{ ref('dims_maps') }} m
    ON v.map_name = m.map_name
    WHERE action != "decider"
),
team_list AS(
    SELECT
        match_id,
        home_team_id,
        away_team_id
    FROM {{ ref('fact_matches') }}
),
decider_home AS(
    SELECT
        v.match_id,
        m.map_id,
        t.home_team_id AS team_id,
        v.action,
        NULL AS action_order
    FROM {{ ref('stg_map_vetos') }} v
    JOIN team_list t
    ON v.match_id = t.match_id
    JOIN {{ ref('dims_maps') }} m
    ON v.map_name = m.map_name
    WHERE v.action = 'decider'
),
decider_away AS(
    SELECT
        v.match_id,
        m.map_id,
        t.away_team_id AS team_id,
        v.action,
        NULL AS action_order
    FROM {{ ref('stg_map_vetos') }} v
    JOIN team_list t
    ON v.match_id = t.match_id
    JOIN {{ ref('dims_maps') }} m
    ON v.map_name = m.map_name
    WHERE v.action = 'decider'
)

SELECT * FROM non_decider

UNION ALL

SELECT * FROM decider_home

UNION ALL

SELECT * FROM decider_away