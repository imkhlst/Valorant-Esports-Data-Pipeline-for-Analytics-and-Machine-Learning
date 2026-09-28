{{ config(
    materialized = 'table',
    partition_by = {
        "field": "match_date",
        "data_type": "date",
        "granularity": "day"
    }
) }}

WITH round_score AS (
    SELECT DISTINCT
        match_id,
        SUM(home_score) OVER (PARTITION BY match_id) AS home_total_round,
        SUM(away_score) OVER (PARTITION BY match_id) AS away_total_round
    FROM {{ ref('games_overview') }}
)
SELECT
    tour_id,
    m.match_id,
    match_date,
    match_datetime,
    bracket,
    home_id AS home_team_id,
    away_id AS away_team_id,
    bo,
    patch,
    home_score,
    away_score,
    (1.0 * home_score - away_score) / NULLIF(1.0 * home_score + away_score, 0) AS normalized_score_diff,
    r.home_total_round,
    r.away_total_round,
    (1.0 * r.home_total_round - r.away_total_round) / NULLIF(1.0 * r.home_total_round + r.away_total_round, 0) AS normalized_match_round_diff,
    home_h2h_win,
    away_h2h_win,
    (1.0 * home_h2h_win - away_h2h_win) / NULLIF(1.0 * home_h2h_win + away_h2h_win, 0) AS normalized_h2h_win_diff,
    home_h2h_score,
    away_h2h_score,
    (1.0 * home_h2h_score - away_h2h_score) / NULLIF(1.0 * home_h2h_score + away_h2h_score, 0) AS normalized_h2h_game_win_diff,
    home_n_last_win,
    away_n_last_win,
    home_n_last_match,
    away_n_last_match,
    home_n_last_wr,
    away_n_last_wr,
    
    CASE
        WHEN home_score > away_score
        THEN 1
        ELSE 0 
    END AS is_home_win
FROM {{ ref('matches') }} m
JOIN round_score r
ON r.match_id = m.match_id