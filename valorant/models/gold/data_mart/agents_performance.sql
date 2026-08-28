{{ config(
    materialized='view'
) }}

SELECT
    agent_id,
    COUNT(*) AS pick_count,
    COUNT(DISTINCT game_id) AS total_games,
    1.0 * COUNT(*) / NULLIF(COUNT(DISTINCT game_id), 0) AS pick_rate,
    1.0 * SUM(is_win) / NULLIF(COUNT(*), 0) AS win_rate,
FROM {{ ref('fact_players') }}
WHERE mod = 'avg'
GROUP BY
    agent_id