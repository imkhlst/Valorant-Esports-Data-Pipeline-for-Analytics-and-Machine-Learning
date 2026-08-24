SELECT
    match_id,
    home_n_last_win,
    away_n_last_win,
    home_n_last_match,
    away_n_last_match
FROM {{ ref('stg_matches') }}
WHERE home_n_last_win > home_n_last_match
OR away_n_last_win > away_n_last_match