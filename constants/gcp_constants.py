BUCKET_NAME = "valorant-raw-data"

DATASET_NAME = [
    "bronze",
    "dbt_dev",
    "dbt_ci",
    "dbt_prod"
]

LOCATION = "asia-southeast2"

PROJECT_ID = "valorant-project-2026"

LOCAL_DATA_DIR_PATH = r"data\raw"

BLOB_NAME = "raw"

GCS_DATA_DIR_PATH = f"{BUCKET_NAME}/{BLOB_NAME}"