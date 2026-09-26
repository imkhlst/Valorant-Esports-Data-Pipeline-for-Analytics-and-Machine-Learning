-- Create table if does not exists
CREATE TABLE IF NOT EXISTS `{target_table}` (
    tour_id STRING,
    match_id STRING,
    date STRING,
    patch STRING,
    bracket STRING,
    home_name STRING,
    home_alias STRING,
    away_name STRING,
    away_alias STRING,
    bo STRING,
    home_score INT64,
    away_score INT64,
    home_h2h_win INT64,
    away_h2h_win INT64,
    home_h2h_score INT64,
    away_h2h_score INT64,
    home_last_win INT64,
    away_last_win INT64,
    home_last_match INT64,
    away_last_match INT64,
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
    target.tour_id = source.tour_id,
    target.date = source.date,
    target.bracket = source.bracket,
    target.patch = source.patch,
    target.home_name = source.home_name,
    target.away_name = source.away_name,
    target.bo = source.bo,
    target.home_score = source.home_score,
    target.away_score = source.away_score,
    target.home_h2h_win = source.home_h2h_win,
    target.away_h2h_win = source.away_h2h_win,
    target.home_h2h_score = source.home_h2h_score,
    target.away_h2h_score = source.away_h2h_score,
    target.home_last_win = source.home_last_win,
    target.away_last_win = source.away_last_win,
    target.home_last_match = source.home_last_match,
    target.away_last_match = source.away_last_match,
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
    home_name,
    away_name,
    bo,
    home_score,
    away_score,
    home_h2h_win,
    away_h2h_win,
    home_h2h_score,
    away_h2h_score,
    home_last_win,
    away_last_win,
    home_last_match,
    away_last_match,
    scraped_at,
    ingested_at,
    updated_at
)
VALUES (
    source.tour_id,
    source.match_id,
    source.date,
    source.bracket,
    source.patch,
    source.home_name,
    source.away_name,
    source.bo,
    source.home_score,
    source.away_score,
    source.home_h2h_win,
    source.away_h2h_win,
    source.home_h2h_score,
    source.away_h2h_score,
    source.home_last_win,
    source.away_last_win,
    source.home_last_match,
    source.away_last_match,
    TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)