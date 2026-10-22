-- Create table if does not exists
CREATE TABLE IF NOT EXISTS `{target_table}` (
    tour_id STRING,
    match_id STRING,
    date STRING,
    patch STRING,
    bracket STRING,
    home_id STRING,
    away_id STRING,
    bo STRING,
    home_score INT64,
    away_score INT64,
    home_h2h_win INT64,
    away_h2h_win INT64,
    home_h2h_score INT64,
    away_h2h_score INT64,
    home_n_last_win INT64,
    away_n_last_win INT64,
    home_n_last_match INT64,
    away_n_last_match INT64,
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
ON target.match_id = source.match_id

WHEN MATCHED
THEN UPDATE SET
    target.tour_id = SAFE_CAST(source.tour_id AS STRING),
    target.date = SAFE_CAST(source.date AS STRING),
    target.bracket = SAFE_CAST(source.bracket AS STRING),
    target.patch = SAFE_CAST(source.patch AS STRING),
    target.home_id = SAFE_CAST(source.home_id AS STRING),
    target.away_id =  SAFE_CAST(source.away_id AS STRING),
    target.bo =  SAFE_CAST(source.bo AS STRING),
    target.home_score = SAFE_CAST(source.home_score AS INT64),
    target.away_score = SAFE_CAST(source.away_score AS INT64),
    target.home_h2h_win = SAFE_CAST(source.home_h2h_win AS INT64),
    target.away_h2h_win = SAFE_CAST(source.away_h2h_win AS INT64),
    target.home_h2h_score = SAFE_CAST(source.home_h2h_score AS INT64),
    target.away_h2h_score = SAFE_CAST(source.away_h2h_score AS INT64),
    target.home_n_last_win = SAFE_CAST(source.home_n_last_win AS INT64),
    target.away_n_last_win = SAFE_CAST(source.away_n_last_win AS INT64),
    target.home_n_last_match = SAFE_CAST(source.home_n_last_match AS INT64),
    target.away_n_last_match = SAFE_CAST(source.away_n_last_match AS INT64),
    target.scraped_at = TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    target.ingested_at = target.ingested_at,
    target.updated_at = CURRENT_TIMESTAMP()

WHEN NOT MATCHED
THEN INSERT (
    tour_id,
    match_id,
    date,
    bracket,
    patch,
    home_id,
    away_id,
    bo,
    home_score,
    away_score,
    home_h2h_win,
    away_h2h_win,
    home_h2h_score,
    away_h2h_score,
    home_n_last_win,
    away_n_last_win,
    home_n_last_match,
    away_n_last_match,
    scraped_at,
    ingested_at,
    updated_at
)
VALUES (
    SAFE_CAST(source.tour_id AS STRING),
    SAFE_CAST(source.match_id AS STRING),
    SAFE_CAST(source.date AS STRING),
    SAFE_CAST(source.bracket AS STRING),
    SAFE_CAST(source.patch AS STRING),
    SAFE_CAST(source.home_id AS STRING),
    SAFE_CAST(source.away_id AS STRING),
    SAFE_CAST(source.bo AS STRING),
    SAFE_CAST(source.home_score AS INT64),
    SAFE_CAST(source.away_score AS INT64),
    SAFE_CAST(source.home_h2h_win AS INT64),
    SAFE_CAST(source.away_h2h_win AS INT64),
    SAFE_CAST(source.home_h2h_score AS INT64),
    SAFE_CAST(source.away_h2h_score AS INT64),
    SAFE_CAST(source.home_n_last_win AS INT64),
    SAFE_CAST(source.away_n_last_win AS INT64),
    SAFE_CAST(source.home_n_last_match AS INT64),
    SAFE_CAST(source.away_n_last_match AS INT64),
    TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)