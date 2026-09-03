SELECT
    match_id,
    home_n_last_win,
    away_n_last_win,
    home_n_last_match,
    away_n_last_match
FROM {{ ref('matches') }}
WHERE home_n_last_win > home_n_last_match
OR away_n_last_win > away_n_last_match