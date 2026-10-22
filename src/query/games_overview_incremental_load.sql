-- Create table if does not exists
CREATE TABLE IF NOT EXISTS `{target_table}` (
    match_id STRING,
    game_id STRING,
    game_map STRING,
    game_duration STRING,
    home_score INT64,
    away_score INT64,
    home_atk_score INT64,
    away_atk_score INT64,
    home_def_score INT64,
    away_def_score INT64,
    home_ot_score INT64,
    away_ot_score INT64,
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

WHEN MATCHED
THEN UPDATE SET
    target.match_id = SAFE_CAST(source.match_id AS STRING),
    target.game_map = SAFE_CAST(source.game_map AS STRING),
    target.game_duration = SAFE_CAST(source.game_duration AS STRING),
    target.home_score = SAFE_CAST(source.home_score AS INT64),
    target.away_score = SAFE_CAST(source.away_score AS INT64),
    target.home_atk_score = SAFE_CAST(source.home_atk_score AS INT64),
    target.away_atk_score = SAFE_CAST(source.away_atk_score AS INT64),
    target.home_def_score = SAFE_CAST(source.home_def_score AS INT64),
    target.away_def_score = SAFE_CAST(source.away_def_score AS INT64),
    target.home_ot_score = SAFE_CAST(source.home_ot_score AS INT64),
    target.away_ot_score = SAFE_CAST(source.away_ot_score AS INT64),
    target.scraped_at = TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    target.ingested_at = target.ingested_at,
    target.updated_at = CURRENT_TIMESTAMP()

WHEN NOT MATCHED
THEN INSERT (
    match_id,
    game_id,
    game_map,
    game_duration,
    home_score,
    away_score,
    home_atk_score,
    away_atk_score,
    home_def_score,
    away_def_score,
    home_ot_score,
    away_ot_score,
    scraped_at,
    ingested_at,
    updated_at
)
VALUES (
    SAFE_CAST(source.match_id AS STRING),
    SAFE_CAST(source.game_id AS STRING),
    SAFE_CAST(source.game_map AS STRING),
    SAFE_CAST(source.game_duration AS STRING),
    SAFE_CAST(source.home_score AS INT64),
    SAFE_CAST(source.away_score AS INT64),
    SAFE_CAST(source.home_atk_score AS INT64),
    SAFE_CAST(source.away_atk_score AS INT64),
    SAFE_CAST(source.home_def_score AS INT64),
    SAFE_CAST(source.away_def_score AS INT64),
    SAFE_CAST(source.home_ot_score AS INT64),
    SAFE_CAST(source.away_ot_score AS INT64),
    TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)
