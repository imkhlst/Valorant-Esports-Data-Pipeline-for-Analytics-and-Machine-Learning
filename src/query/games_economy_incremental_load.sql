-- Create table if does not exists
CREATE TABLE IF NOT EXISTS `{target_table}` (
    match_id STRING,
    game_id STRING,
    home_pstl_win INT64,
    away_pstl_win INT64,
    home_eco_round INT64,
    away_eco_round INT64,
    home_eco_win INT64,
    away_eco_win INT64,
    home_semi_eco_round INT64,
    away_semi_eco_round INT64,
    home_semi_eco_win INT64,
    away_semi_eco_win INT64,
    home_semi_buy_round INT64,
    away_semi_buy_round INT64,
    home_semi_buy_win INT64,
    away_semi_buy_win INT64,
    home_full_buy_round INT64,
    away_full_buy_round INT64,
    home_full_buy_win INT64,
    away_full_buy_win INT64,
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
    target.home_pstl_win = SAFE_CAST(source.home_pstl_win AS INT64),
    target.away_pstl_win = SAFE_CAST(source.away_pstl_win AS INT64),
    target.home_eco_round = SAFE_CAST(source.home_eco_round AS INT64),
    target.away_eco_round = SAFE_CAST(source.away_eco_round AS INT64),
    target.home_eco_win = SAFE_CAST(source.home_eco_win AS INT64),
    target.away_eco_win = SAFE_CAST(source.away_eco_win AS INT64),
    target.home_semi_eco_round = SAFE_CAST(source.home_semi_eco_round AS INT64),
    target.away_semi_eco_round = SAFE_CAST(source.away_semi_eco_round AS INT64),
    target.home_semi_eco_win = SAFE_CAST(source.home_semi_eco_win AS INT64),
    target.away_semi_eco_win = SAFE_CAST(source.away_semi_eco_win AS INT64),
    target.home_semi_buy_round = SAFE_CAST(source.home_semi_buy_round AS INT64),
    target.away_semi_buy_round = SAFE_CAST(source.away_semi_buy_round AS INT64),
    target.home_semi_buy_win = SAFE_CAST(source.home_semi_buy_win AS INT64),
    target.away_semi_buy_win = SAFE_CAST(source.away_semi_buy_win AS INT64),
    target.home_full_buy_round = SAFE_CAST(source.home_full_buy_round AS INT64),
    target.away_full_buy_round = SAFE_CAST(source.away_full_buy_round AS INT64),
    target.home_full_buy_win = SAFE_CAST(source.home_full_buy_win AS INT64),
    target.away_full_buy_win = SAFE_CAST(source.away_full_buy_win AS INT64),
    target.scraped_at = TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    target.ingested_at = target.ingested_at,
    target.updated_at = CURRENT_TIMESTAMP()

WHEN NOT MATCHED
THEN INSERT (
    match_id,
    game_id,
    home_pstl_win,
    away_pstl_win,
    home_eco_round,
    away_eco_round,
    home_eco_win,
    away_eco_win,
    home_semi_eco_round,
    away_semi_eco_round,
    home_semi_eco_win,
    away_semi_eco_win,
    home_semi_buy_round,
    away_semi_buy_round,
    home_semi_buy_win,
    away_semi_buy_win,
    home_full_buy_round,
    away_full_buy_round,
    home_full_buy_win,
    away_full_buy_win,
    scraped_at,
    ingested_at,
    updated_at
)
VALUES (
    SAFE_CAST(source.match_id AS STRING),
    SAFE_CAST(source.game_id AS STRING),
    SAFE_CAST(source.home_pstl_win AS INT64),
    SAFE_CAST(source.away_pstl_win AS INT64),
    SAFE_CAST(source.home_eco_round AS INT64),
    SAFE_CAST(source.away_eco_round AS INT64),
    SAFE_CAST(source.home_eco_win AS INT64),
    SAFE_CAST(source.away_eco_win AS INT64),
    SAFE_CAST(source.home_semi_eco_round AS INT64),
    SAFE_CAST(source.away_semi_eco_round AS INT64),
    SAFE_CAST(source.home_semi_eco_win AS INT64),
    SAFE_CAST(source.away_semi_eco_win AS INT64),
    SAFE_CAST(source.home_semi_buy_round AS INT64),
    SAFE_CAST(source.away_semi_buy_round AS INT64),
    SAFE_CAST(source.home_semi_buy_win AS INT64),
    SAFE_CAST(source.away_semi_buy_win AS INT64),
    SAFE_CAST(source.home_full_buy_round AS INT64),
    SAFE_CAST(source.away_full_buy_round AS INT64),
    SAFE_CAST(source.home_full_buy_win AS INT64),
    SAFE_CAST(source.away_full_buy_win AS INT64),
    TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)