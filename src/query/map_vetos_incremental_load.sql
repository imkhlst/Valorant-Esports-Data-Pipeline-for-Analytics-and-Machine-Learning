-- Create table if does not exists
CREATE TABLE IF NOT EXISTS `{target_table}` (
    match_id STRING,
    map_name STRING,
    team_name STRING,
    action STRING,
    scraped_at TIMESTAMP,
    ingested_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Add ingested_at and updated_at column if does not exist
ALTER TABLE `{target_table}`
ADD COLUMN IF NOT EXISTS scraped_at TIMESTAMP,
ADD COLUMN IF NOT EXISTS ingested_at TIMESTAMP,
ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP;

-- Merge table from source (staging) and target (bronze)
MERGE `{target_table}` AS target
USING `{source_table}` AS source
ON target.game_id = source.game_id
AND target.map_name = source.map_name
AND target.team_name = source.team_name

WHEN MATCHED
THEN UPDATE SET
    target.match_id = source.match_id,
    target.action = source.action,
    target.scraped_at = source.scraped_at,
    target.ingested_at = target.ingested_at,
    target.updated_at = CURRENT_TIMESTAMP()

WHEN NOT MATCHED
THEN INSERT (
    match_id,
    map_name,
    team_name,
    action,
    scraped_at,
    ingested_at,
    updated_at
)
VALUES (
    source.match_id,
    source.map_name,
    source.team_name,
    source.action,
    source.scraped_at,
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)