SELECT
    f.tour_id,
    o.match_id,
    o.game_id,    
    o.match_date,
    o.match_datetime,
    f.home_team_id,
    f.away_team_id,
    m.map_id,
    game_duration,

    o.home_score,
    o.away_score,
    o.home_score + o.away_score AS total_round,
    (1.0 * o.home_score - o.away_score) / NULLIF(o.home_score + o.away_score, 0) AS normalized_score_diff,

    home_atk_score,
    away_atk_score,
    (1.0 * home_atk_score / NULLIF(home_atk_score + away_def_score, 2)) / NULLIF(1.0 * away_atk_score / NULLIF(away_atk_score + home_def_score, 0), 0) AS atk_wr_ratio,

    home_def_score,
    away_def_score,
    (1.0 * home_def_score / NULLIF(home_def_score + away_atk_score, 2)) / NULLIF(1.0 * away_def_score / NULLIF(away_def_score + home_atk_score, 0), 0) AS def_wr_ratio,
    
    home_ot_score,
    away_ot_score,
    (1.0 * home_ot_score - away_ot_score) / NULLIF(home_ot_score + away_ot_score, 0) AS normalized_ot_score_diff,

    e.home_pstl_win,
    e.away_pstl_win,
    e.home_pstl_win - e.away_pstl_win AS pstl_win_diff,

    e.home_eco_round,
    e.away_eco_round,
    e.home_eco_win,
    e.away_eco_win,
    (1.0 * e.home_eco_win / NULLIF(e.home_eco_round, 0)) - (1.0 * e.away_eco_win / NULLIF(e.away_eco_round, 0)) AS eco_wr_diff,
    
    e.home_semi_eco_round,
    e.away_semi_eco_round,
    e.home_semi_eco_win,
    e.away_semi_eco_win,
    (1.0 * e.home_semi_eco_win / NULLIF(e.home_semi_eco_round, 0)) - (1.0 * e.away_semi_eco_win / NULLIF(e.away_semi_eco_round, 0)) AS semi_eco_wr_diff,
    
    e.home_semi_buy_round,
    e.away_semi_buy_round,
    e.home_semi_buy_win,
    e.away_semi_buy_win,
    (1.0 * e.home_semi_buy_win / NULLIF(e.home_semi_buy_round, 0)) - (1.0 * e.away_semi_buy_win / NULLIF(e.away_semi_buy_round, 0)) AS semi_buy_wr_diff,
    
    e.home_full_buy_round,
    e.away_full_buy_round,
    e.home_full_buy_win,
    e.away_full_buy_win,
    (1.0 * e.home_full_buy_win / NULLIF(e.home_full_buy_round, 0)) - (1.0 * e.away_full_buy_win / NULLIF(e.away_full_buy_round, 0)) AS full_buy_wr_diff,
    
    CASE
        WHEN o.home_score > o.away_score
        THEN 1
        ELSE 0 
    END AS is_home_win
FROM {{ ref('games_overview') }} o
INNER JOIN {{ ref('games_economy') }} e
ON o.game_id = e.game_id
JOIN {{ ref('fact_matches') }} f
ON o.match_id = f.match_id
JOIN {{ ref('dims_maps') }} m
ON o.game_map = m.map_name