{{ config(
    materialized='view'
) }}

WITH team_pick_ban AS(
    SELECT
        team_id,
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
    GROUP BY
        team_id,
        map_id
),
team_map_count AS(
    SELECT
        team_id,
        map_id,
        COUNT(*) AS map_played,
        SUM(is_ot) AS ot_played,
        SUM(is_win) AS maps_win,
        AVG(game_duration) AS avg_game_duration,
        AVG(normalized_score_diff) AS avg_normalized_score_diff,
        AVG(atk_wr) AS avg_atk_wr,
        AVG(def_wr) AS avg_def_wr,
        AVG(pstl_wr) AS avg_pstl_wr,
        AVG(eco_wr) AS avg_eco_wr,
        AVG(semi_eco_wr) AS avg_semi_eco_wr,
        AVG(semi_buy_wr) AS avg_semi_buy_wr,
        AVG(full_buy_wr) AS avg_full_buy_wr
    FROM {{ ref('team_games_performance') }}
    GROUP BY
        team_id,
        map_id
),
team_count AS (
    SELECT
        team_id,
        COUNT(DISTINCT match_id) AS total_matches
    FROM {{ ref('team_games_performance') }}
    GROUP BY team_id
)

SELECT
    m.team_id,
    m.map_id,
    map_played,
    ot_played,
    1.0 * ot_played / NULLIF(map_played) AS ot_rate,
    maps_win,

    1.0 * maps_win / map_played AS map_wr,

    p.pick_count,
    p.ban_count,

    1.0 * p.pick_count / NULLIF(c.total_matches, 0) AS pick_rate,
    1.0 * p.ban_count / NULLIF(c.total_matches, 0) AS ban_rate,
    1.0 * p.pick_count / NULLIF(p.pick_count + p.ban_count, 0) AS map_pick_preference,

    avg_game_duration,
    avg_normalized_score_diff,
    avg_atk_wr,
    avg_def_wr,
    avg_pstl_wr,
    avg_eco_wr,
    avg_semi_eco_wr,
    avg_semi_buy_wr,
    avg_full_buy_wr
FROM team_map_count m
LEFT JOIN team_pick_ban p
ON m.team_id = p.team_id
AND m.map_id = p.map_id
JOIN team_count c
ON m.team_id = c.team_id