{{ config(
    materialized='view'
) }}

SELECT
    f.agent_id,
    a.agent_name,
    f.map_id,
    m.map_name,
    COUNT(DISTINCT game_id) AS presence_count,
    p.map_played,
    COUNT(f.agent_id) AS pick_count,
    SUM(is_win) AS total_win,
    1.0 * COUNT(f.agent_id) / NULLIF(p.map_played, 0) AS pick_rate,
    1.0 * SUM(is_win) / NULLIF(COUNT(DISTINCT game_id), 0) AS win_rate,
    1.0 * COUNT(DISTINCT game_id) / NULLIF(p.map_played, 0) AS presence_rate
FROM {{ ref('fact_players') }} f
JOIN {{ ref('maps_performance') }} p
ON f.map_id = p.map_id
JOIN {{ ref('dims_agents') }} a
ON f.agent_id = a.agent_id
JOIN {{ ref('dims_maps') }} m
ON f.map_id = m.map_id
WHERE mod = 'avg'
GROUP BY
    f.agent_id,
    a.agent_name,
    f.map_id,
    m.map_name,
    p.map_played