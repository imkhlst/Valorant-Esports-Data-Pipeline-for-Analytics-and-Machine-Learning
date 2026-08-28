SELECT ROW_NUMBER() OVER (ORDER BY player_name) AS player_id, player_name, player_nationality
FROM(
    SELECT DISTINCT
        player_name,
        nationality as player_nationality
    FROM {{ ref('players') }}
)