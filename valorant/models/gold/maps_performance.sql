{{ config(
    materialized='view'
) }}

WITH team_pick_ban AS(
    SELECT
        map_id,

        SUM(
            CASE
                WHEN action = 'pick'
                THEN 1
                ELSE 0
            END
        ) AS pick_count,

        SUM(
            CASE
                WHEN action = 'ban'
                THEN 1
                ELSE 0
            END
        ) AS ban_count
    FROM {{ ref('fact_map_vetos') }}
    GROUP BY map_id
),
map_count AS(
    SELECT
        map_id,
        COUNT(DISTINCT match_id) AS map_played,
        SUM(is_ot) AS ot_played,
        AVG(game_duration) AS avg_game_duration
    FROM {{ ref('team_games_performance') }}
    GROUP BY map_id
),
match_count AS (
    SELECT
        map_id,
        SUM(total_round) AS total_round,
        SUM(home_atk_score + away_atk_score) AS atk_side_score,
        SUM(home_def_score + away_def_score) AS def_side_score,
        (SELECT COUNT(DISTINCT match_id) FROM {{ ref('fact_games') }}) AS total_matches
    FROM {{ ref('fact_games') }}
    GROUP BY map_id
)

SELECT
    m.map_id,
    map_played,
    ot_played,

    p.pick_count,
    p.ban_count,

    1.0 * p.pick_count / NULLIF(c.total_round, 0) AS pick_rate,
    1.0 * p.ban_count / NULLIF(c.total_round, 0) AS ban_rate,
    1.0 * p.pick_count / NULLIF(p.pick_count + p.ban_count, 0) AS map_pick_preference,
    
    avg_game_duration,
    1.0 * c.atk_side_score / NULLIF(c.total_round, 0) AS atk_side_ratio,
    1.0 * c.def_side_score / NULLIF(c.total_round, 0) AS def_side_ratio

FROM map_count m
LEFT JOIN team_pick_ban p
ON m.map_id = p.map_id
JOIN match_count c
ON m.map_id = c.map_id