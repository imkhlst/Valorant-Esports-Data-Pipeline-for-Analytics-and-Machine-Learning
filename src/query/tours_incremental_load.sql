-- Create table if does not exists
CREATE TABLE IF NOT EXISTS `{target_table}` (
    tour_id STRING,
    tour_name STRING,
    tour_tag STRING,
    tour_stage STRING,
    tour_region STRING,
    tour_status STRING,
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
ON target.tour_id = source.tour_id

WHEN MATCHED
THEN UPDATE SET
    target.tour_name = source.tour_name,
    target.tour_tag = source.tour_tag,
    target.tour_stage = source.tour_stage,
    target.tour_region = source.tour_region,
    target.tour_status = source.tour_status,
    target.scraped_at = source.scraped_at,
    target.ingested_at = target.ingested_at,
    target.updated_at = CURRENT_TIMESTAMP()

WHEN NOT MATCHED
THEN INSERT (
    tour_id,
    tour_name,
    tour_tag,
    tour_stage,
    tour_region,
    tour_status,
    scraped_at,
    ingested_at,
    updated_at
)
VALUES (
    source.tour_id,
    source.tour_name,
    source.tour_tag,
    source.tour_stage,
    source.tour_region,
    source.tour_status,
    source.scraped_at,
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)