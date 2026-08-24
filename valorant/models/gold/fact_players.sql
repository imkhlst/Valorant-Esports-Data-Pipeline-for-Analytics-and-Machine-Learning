WITH statistics AS(
    SELECT
        tour_id,
        match_id,
        game_id,
        map_id,
        p.team_id,
        t.team_alias,
        is_win
    FROM {{ ref('team_games_performance') }} p
    JOIN {{ ref('dims_teams') }} t
    ON p.team_id = t.team_id
)
SELECT
    s.tour_id,
    s.match_id,
    pp.game_id,
    match_date,
    match_datetime,
    s.map_id,
    p.player_id,
    s.team_id,
    ag.agent_id,
    s.is_win,
    mod,
    r,
    acs,
    k,
    d,
    a,
    kd,
    kast,
    adr,
    hs,
    fk,
    fd,
    fkfd
FROM {{ ref('players') }} pp
JOIN statistics s
ON pp.game_id = s.game_id
AND pp.team_alias = s.team_alias
JOIN {{ ref('dims_players') }} p
ON pp.player_name = p.player_name
JOIN {{ ref('dims_agents') }} ag
ON pp.agent = ag.agent_name