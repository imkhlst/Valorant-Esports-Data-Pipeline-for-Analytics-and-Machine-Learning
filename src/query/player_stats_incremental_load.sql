-- Create table if does not exists
CREATE TABLE IF NOT EXISTS `{target_table}` (
    game_id STRING,
    name STRING,
    team_alias STRING,
    nationality STRING,
    agent STRING,
    mod STRING,
    r INT64,
    acs INT64,
    k INT64,
    d INT64,
    a INT64,
    kd INT64,
    kast INT64,
    adr INT64,
    hs INT64,
    fk INT64,
    fd INT64,
    fkfd INT64,
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
    target.team_alias = SAFE_CAST(source.team_alias AS STRING),
    target.nationality = SAFE_CAST(source.nationality AS STRING),
    target.agent = SAFE_CAST(source.agent AS STRING),
    target.r = SAFE_CAST(source.r AS INT64),
    target.acs = SAFE_CAST(source.acs AS INT64),
    target.k = SAFE_CAST(source.k AS INT64),
    target.d = SAFE_CAST(source.d AS INT64),
    target.a = SAFE_CAST(source.a AS INT64),
    target.kd = SAFE_CAST(source.kd AS INT64),
    target.kast = SAFE_CAST(source.kast AS INT64),
    target.adr = SAFE_CAST(source.adr AS INT64),
    target.hs = SAFE_CAST(source.hs AS INT64),
    target.fk = SAFE_CAST(source.fk AS INT64),
    target.fd = SAFE_CAST(source.fd AS INT64),
    target.fkfd = SAFE_CAST(source.fkfd AS INT64),
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
    SAFE_CAST(source.game_id AS STRING),
    SAFE_CAST(source.name AS STRING),
    SAFE_CAST(source.team_alias AS STRING),
    SAFE_CAST(source.nationality AS STRING),
    SAFE_CAST(source.agent AS STRING),
    SAFE_CAST(source.mod AS STRING),
    SAFE_CAST(source.r AS INT64),
    SAFE_CAST(source.acs AS INT64),
    SAFE_CAST(source.k AS INT64),
    SAFE_CAST(source.d AS INT64),
    SAFE_CAST(source.a AS INT64),
    SAFE_CAST(source.kd AS INT64),
    SAFE_CAST(source.kast AS INT64),
    SAFE_CAST(source.adr AS INT64),
    SAFE_CAST(source.hs AS INT64),
    SAFE_CAST(source.fk AS INT64),
    SAFE_CAST(source.fd AS INT64),
    SAFE_CAST(source.fkfd AS INT64),
    TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)