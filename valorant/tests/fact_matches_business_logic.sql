SELECT
    match_id,
    home_score,
    away_score,
    is_home_win
FROM {{ ref('fact_matches') }}
WHERE
    (home_score > away_score AND is_home_win != 1)
    OR
    (away_score > home_score AND is_home_win != 0)