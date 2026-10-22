-- Create table if does not exists
CREATE TABLE IF NOT EXISTS `{target_table}` (
    team_id STRING,
    team_name STRING,
    team_alias STRING,
    team_country STRING,
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
ON target.team_id = source.team_id

WHEN MATCHED
THEN UPDATE SET
    target.team_name = SAFE_CAST(source.team_name AS STRING),
    target.team_alias = SAFE_CAST(source.team_alias AS STRING),
    target.team_country = SAFE_CAST(source.team_country AS STRING),
    target.scraped_at = TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    target.ingested_at = target.ingested_at,
    target.updated_at = CURRENT_TIMESTAMP()

WHEN NOT MATCHED
THEN INSERT (
    team_id,
    team_name,
    team_alias,
    team_country,
    scraped_at,
    ingested_at,
    updated_at
)
VALUES (
    SAFE_CAST(source.team_id AS STRING),
    SAFE_CAST(source.team_name AS STRING),
    SAFE_CAST(source.team_alias AS STRING),
    SAFE_CAST(source.team_country AS STRING),
    TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)