-- Create table if does not exists
CREATE TABLE IF NOT EXISTS `{target_table}` (
    player_id STRING,
    player_nickname STRING,
    player_realname STRING,
    player_nationality STRING,
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
ON target.player_id = source.player_id

WHEN MATCHED
THEN UPDATE SET
    target.player_nickname = SAFE_CAST(source.player_nickname AS STRING),
    target.player_realname = SAFE_CAST(source.player_realname AS STRING),
    target.player_nationality = SAFE_CAST(source.player_nationality AS STRING),
    target.scraped_at = TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    target.ingested_at = target.ingested_at,
    target.updated_at = CURRENT_TIMESTAMP()

WHEN NOT MATCHED
THEN INSERT (
    player_id,
    player_nickname,
    player_realname,
    player_nationality,
    scraped_at,
    ingested_at,
    updated_at
)
VALUES (
    SAFE_CAST(source.player_id AS STRING),
    SAFE_CAST(source.player_nickname AS STRING),
    SAFE_CAST(source.player_realname AS STRING),
    SAFE_CAST(source.player_nationality AS STRING),
    TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)