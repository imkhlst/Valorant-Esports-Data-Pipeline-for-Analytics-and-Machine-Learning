from pathlib import Path

BUCKET_NAME = "valorant-data"

DATASET_NAME = [
    "bronze",
    "dbt_dev",
    "dbt_ci",
    "dbt_prod"
]

LOCATION = "asia-southeast2"

PROJECT_ID = "valorant-project-2026"

LOCAL_DATA_DIR_PATH = Path("data") / "raw"

BLOB_NAME = "raw"

GCS_DATA_DIR_PATH = f"{BUCKET_NAME}/{BLOB_NAME}"