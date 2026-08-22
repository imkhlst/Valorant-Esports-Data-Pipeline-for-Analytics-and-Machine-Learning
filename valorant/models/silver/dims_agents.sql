SELECT ROW_NUMBER() OVER(ORDER BY agent_name) AS agent_id, agent_name
FROM(
    SELECT DISTINCT agent AS agent_name
    FROM {{ ref('players') }}
)