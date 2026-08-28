{{ config(
    materialized='view'
) }}

SELECT
    player_id,
    agent_id,
    map_id,
    COUNT(map_id) AS agent_played,
    SUM(is_win) AS total_win,
    1.0 * SUM(is_win) / COUNT(map_id) AS agent_wr,
    AVG(r) AS avg_r,
    AVG(acs) AS avg_acs,
    AVG(k) AS avg_k,
    AVG(d) AS avg_d,
    AVG(a) AS avg_a,
    AVG(kd) AS avg_kd,
    AVG(kast) AS avg_kast,
    AVG(adr) AS avg_adr,
    AVG(hs) AS avg_hs,
    AVG(fk) AS avg_fk,
    AVG(fd) AS avg_fd,
    AVG(fkfd) AS avg_fkfd
FROM {{ ref('fact_players') }}
WHERE mod = 'avg'
GROUP BY
    player_id,
    agent_id,
    map_id