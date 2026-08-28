{{ config(
    materialized='view'
) }}

SELECT
    f.tour_id,
    t.tour_name,
    t.tour_region,
    match_id,
    match_date,
    match_datetime,
    bracket,
    home_team_id AS team_id,
    bo,
    patch,
    home_score AS score,
    home_total_round AS total_round,
    home_h2h_win AS h2h_win,
    home_h2h_score AS h2h_score,
    home_n_last_win AS n_last_win,
    home_n_last_match AS n_last_match,
    home_n_last_wr AS n_last_match_wr,
    is_home_win AS is_win
FROM {{ ref('fact_matches') }} f
JOIN {{ ref('dims_tours') }} t
ON f.tour_id = t.tour_id
UNION ALL
SELECT
    f.tour_id,
    t.tour_name,
    t.tour_region
    match_id,
    match_date,
    match_datetime,
    bracket,
    away_team_id,
    bo,
    patch,
    away_score,
    away_total_round,
    away_h2h_win,
    away_h2h_score,
    away_n_last_win,
    away_n_last_match,
    away_n_last_wr,

    CASE
        WHEN is_win = 1
        THEN 0
        ELSE 1
    END AS is_win
FROM {{ ref('fact_matches') }} f
JOIN {{ ref('dims_tours') }} t
ON f.tour_id = t.tour_id