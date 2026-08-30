{{ config(
    materialized='view'
) }}

SELECT
    f.player_id,
    p.player_name,
    f.agent_id,
    a.agent_name,
    f.map_id,
    m.map_name,
    COUNT(f.map_id) AS agent_played,
    SUM(is_win) AS total_win,
    1.0 * SUM(is_win) / COUNT(f.map_id) AS agent_wr,
    AVG(r) AS avg_r,
    AVG(acs) AS avg_acs,
    AVG(k) AS avg_k,
    AVG(d) AS avg_d,
    AVG(f.a) AS avg_a,
    AVG(kd) AS avg_kd,
    AVG(kast) AS avg_kast,
    AVG(adr) AS avg_adr,
    AVG(hs) AS avg_hs,
    AVG(fk) AS avg_fk,
    AVG(fd) AS avg_fd,
    AVG(fkfd) AS avg_fkfd
FROM {{ ref('fact_players') }} f
JOIN {{ ref('dims_players') }} p
ON f.player_id = p.player_id
JOIN {{ ref('dims_agents') }} a
ON f.agent_id = a.agent_id
JOIN {{ ref('dims_maps') }} m
ON f.map_id = m.map_id
WHERE mod = 'avg'
GROUP BY
    f.player_id,
    p.player_name,
    f.agent_id,
    a.agent_name,
    f.map_id,
    m.map_name