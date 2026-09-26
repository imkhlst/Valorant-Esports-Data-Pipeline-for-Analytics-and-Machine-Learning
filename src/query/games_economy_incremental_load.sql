-- Create table if does not exists
CREATE TABLE IF NOT EXISTS `{target_table}` (
    match_id STRING,
    game_id STRING,
    home_pstl_win FLOAT64,
    away_pstl_win FLOAT64,
    home_eco_round FLOAT64,
    away_eco_round FLOAT64,
    home_eco_win FLOAT64,
    away_eco_win FLOAT64,
    home_semi_eco_round FLOAT64,
    away_semi_eco_round FLOAT64,
    home_semi_eco_win FLOAT64,
    away_semi_eco_win FLOAT64,
    home_semi_buy_round FLOAT64,
    away_semi_buy_round FLOAT64,
    home_semi_buy_win FLOAT64,
    away_semi_buy_win FLOAT64,
    home_full_buy_round FLOAT64,
    away_full_buy_round FLOAT64,
    home_full_buy_win FLOAT64,
    away_full_buy_win FLOAT64,
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

WHEN MATCHED
THEN UPDATE SET
    target.match_id = source.match_id,
    target.home_pstl_win = source.home_pstl_win,
    target.away_pstl_win = source.away_pstl_win,
    target.home_eco_round = source.home_eco_round,
    target.away_eco_round = source.away_eco_round,
    target.home_eco_win = source.home_eco_win,
    target.away_eco_win = source.away_eco_win,
    target.home_semi_eco_round = source.home_semi_eco_round,
    target.away_semi_eco_round = source.away_semi_eco_round,
    target.home_semi_eco_win = source.home_semi_eco_win,
    target.away_semi_eco_win = source.away_semi_eco_win,
    target.home_semi_buy_round = source.home_semi_buy_round,
    target.away_semi_buy_round = source.away_semi_buy_round,
    target.home_semi_buy_win = source.home_semi_buy_win,
    target.away_semi_buy_win = source.away_semi_buy_win,
    target.home_full_buy_round = source.home_full_buy_round,
    target.away_full_buy_round = source.away_full_buy_round,
    target.home_full_buy_win = source.home_full_buy_win,
    target.away_full_buy_win = source.away_full_buy_win,
    target.scraped_at = source.scraped_at,
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
    source.match_id,
    source.game_id,
    source.home_pstl_win,
    source.away_pstl_win,
    source.home_eco_round,
    source.away_eco_round,
    source.home_eco_win,
    source.away_eco_win,
    source.home_semi_eco_round,
    source.away_semi_eco_round,
    source.home_semi_eco_win,
    source.away_semi_eco_win,
    source.home_semi_buy_round,
    source.away_semi_buy_round,
    source.home_semi_buy_win,
    source.away_semi_buy_win,
    source.home_full_buy_round,
    source.away_full_buy_round,
    source.home_full_buy_win,
    source.away_full_buy_win,
    source.scraped_at,
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)