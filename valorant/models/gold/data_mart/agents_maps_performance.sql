{{ config(
    materialized='view'
) }}

SELECT
    p.agent_id,
    a.agent_name,
    p.map_id,
    dm.map_name,
    COUNT(DISTINCT game_id) AS presence_count,
    m.map_played,
    COUNT(agent_id) AS pick_count,
    SUM(is_win) AS total_win,
    1.0 * COUNT(agent_id) / NULLIF(m.map_played, 0) AS pick_rate,
    1.0 * SUM(is_win) / NULLIF(COUNT(DISTINCT game_id), 0) AS win_rate,
    1.0 * COUNT(DISTINCT game_id) / NULLIF(m.map_played, 0) AS presence_rate
FROM {{ ref('fact_players') }} p
JOIN {{ ref('maps_performance') }} m
ON p.map_id = m.map_id
JOIN {{ ref('dims_agents') }} a
ON p.agent_id = a.agent_id
JOIN {{ ref('dims_maps') }} dm
ON p.map_id = dm.map_id
WHERE mod = 'avg'
GROUP BY
    agent_id,
    p.map_id,
    m.map_played