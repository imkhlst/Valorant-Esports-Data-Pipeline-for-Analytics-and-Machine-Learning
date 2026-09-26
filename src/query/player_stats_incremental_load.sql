-- Create table if does not exists
CREATE TABLE IF NOT EXISTS `{target_table}` (
    game_id STRING,
    name STRING,
    team_alias STRING,
    nationality STRING,
    agent STRING,
    mod STRING,
    r FLOAT64,
    acs FLOAT64,
    k FLOAT64,
    d FLOAT64,
    a FLOAT64,
    kd FLOAT64,
    kast FLOAT64,
    adr FLOAT64,
    hs FLOAT64,
    fk FLOAT64,
    fd FLOAT64,
    fkfd FLOAT64,
    scraped_at TIMESTAMP,
    ingested_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Add scraped_at, ingested_at and updated_at column if does not exist
ALTER TABLE `{target_table}`
ADD COLUMN IF NOT EXISTS scraped_at TIMESTAMP,
ADD COLUMN IF NOT EXISTS ingested_at TIMESTAMP,
ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP;

-- Merge table from source (staging) and target (bronze)
MERGE `{target_table}` AS target
USING `{source_table}` AS source
ON target.game_id = source.game_id
AND target.name = source.name
AND target.mod = source.mod

WHEN MATCHED
THEN UPDATE SET
    target.team_alias = source.team_alias,
    target.nationality = source.nationality,
    target.agent = source.agent,
    target.r = source.r,
    target.acs = source.acs,
    target.k = source.k,
    target.d = source.d,
    target.a = source.a,
    target.kd = source.kd,
    target.kast = source.kast,
    target.adr = source.adr,
    target.hs = source.hs,
    target.fk = source.fk,
    target.fd = source.fd,
    target.fkfd = source.fkfd,
    target.scraped_at = TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    target.ingested_at = target.ingested_at,
    target.updated_at = CURRENT_TIMESTAMP()

WHEN NOT MATCHED
THEN INSERT (
    game_id,
    name,
    team_alias,
    nationality,
    agent,
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
    fkfd,
    scraped_at,
    ingested_at,
    updated_at
)
VALUES (
    source.game_id,
    source.name,
    source.team_alias,
    source.nationality,
    source.agent,
    source.mod,
    source.r,
    source.acs,
    source.k,
    source.d,
    source.a,
    source.kd,
    source.kast,
    source.adr,
    source.hs,
    source.fk,
    source.fd,
    source.fkfd,
    TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)