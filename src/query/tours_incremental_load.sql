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

-- Add scraped_at, ingested_at and updated_at column if does not exist
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
    target.tour_name = SAFE_CAST(source.tour_name AS STRING),
    target.tour_tag = SAFE_CAST(source.tour_tag AS STRING),
    target.tour_stage = SAFE_CAST(source.tour_stage AS STRING),
    target.tour_region = SAFE_CAST(source.tour_region AS STRING),
    target.tour_status = SAFE_CAST(source.tour_status AS STRING),
    target.scraped_at = TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
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
    SAFE_CAST(source.tour_id AS STRING),
    SAFE_CAST(source.tour_name AS STRING),
    SAFE_CAST(source.tour_tag AS STRING),
    SAFE_CAST(source.tour_stage AS STRING),
    SAFE_CAST(source.tour_region AS STRING),
    SAFE_CAST(source.tour_status AS STRING),
    TIMESTAMP_MICROS(DIV(source.scraped_at, 1000)),
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
)