{{ config(
    materialized='view'
) }}

SELECT
    f.agent_id,
    a.agent_name,
    COUNT(*) AS pick_count,
    COUNT(DISTINCT game_id) AS total_games,
    1.0 * COUNT(*) / NULLIF(COUNT(DISTINCT game_id), 0) AS pick_rate,
    1.0 * SUM(is_win) / NULLIF(COUNT(*), 0) AS win_rate,
FROM {{ ref('fact_players') }} f
JOIN {{ ref('dims_agents') }} a
ON f.agent_id = a.agent_id
WHERE mod = 'avg'
GROUP BY
    f.agent_id,
    a.agent_name