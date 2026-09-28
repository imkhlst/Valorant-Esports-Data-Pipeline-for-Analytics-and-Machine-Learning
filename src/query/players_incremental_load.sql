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
    target.player_nickname = source.player_nickname,
    target.player_realname = source.player_realname,
    target.player_nationality = source.player_nationality,
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
    source.player_id,
    source.player_nickname,
    source.player_realname,
    source.player_nationality,
    TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)