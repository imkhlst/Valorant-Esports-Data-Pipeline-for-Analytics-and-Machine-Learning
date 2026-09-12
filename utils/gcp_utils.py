import pandas as pd
from logger import logging
from pathlib import Path
from google.cloud import storage, bigquery
from constants.gcp_constants import *
from constants.scraper_constants import FILE_NAME

def create_bucket(
        bucket_name: str = BUCKET_NAME,
        project_id: str = PROJECT_ID,
        location: str = LOCATION
):
    logging.info(f"Checking Storage bucket {bucket_name} ...")

    client = storage.Client(project=project_id)
    bucket = client.bucket(bucket_name)

    if bucket.exists():
        logging.info(f"Bucket {bucket_name} already exists.")
        return bucket

    logging.info(f"Bucket {bucket_name} does not exists. Creating ...")
    
    bucket.location = location
    new_bucket = client.create_bucket(bucket)

    logging.info(f"Success! created bucket {bucket_name} in {location}")
    return new_bucket

def create_dataset(
        dataset_name: str | list = DATASET_NAME,
        project_id: str = PROJECT_ID,
        location: str = LOCATION
):
    client = bigquery.Client(project=project_id)
    dataset_name = dataset_name if isinstance(dataset_name, list) else [dataset_name]

    for i in dataset_name:
        dataset_id = f"{project_id}.{i}"
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = location

        try:
            logging.info(f"Checking BigQuery dataset ...")

            client.get_dataset(dataset_id)

            logging.info(f"Dataset {dataset_id} already exists.")

            return dataset
        
        except Exception:
            logging.info(f"Dataset {dataset_id} does not exists. Creating ...")

            new_dataset = client.create_dataset(dataset)

            logging.info(f"Created dataset {dataset_id} in {location}")

            return new_dataset

def upload_data(
        file_name: str | list = FILE_NAME,
        bucket_name: str = BUCKET_NAME,
        blob_name: str = BLOB_NAME,
        project_id: str = PROJECT_ID,
        local_data_dir_path: str = LOCAL_DATA_DIR_PATH
):
    logging.info(f"Uploading data into storage bucket ...")
    client = storage.Client(project=project_id)
    bucket = client.bucket(bucket_name)

    file_name = file_name if isinstance(file_name, list) else [file_name]

    for i in file_name:
        blob = bucket.blob(f"{blob_name}/{i}.parquet")
        blob.upload_from_filename(f"{Path(local_data_dir_path)}/{i}.parquet")
        logging.info(f"Success! Uploaded {i} into {bucket_name}")

def load_table(
        dataset_name: str,
        file_name: str | list = FILE_NAME,
        project_id: str = PROJECT_ID,
        gcs_data_dir_path: str = GCS_DATA_DIR_PATH
):
    logging.info(f"Loading table into BigQuery dataset ...")
    client = bigquery.Client(project=project_id)
    job_config = bigquery.LoadJobConfig(
            autodetect=True,
            source_format=bigquery.SourceFormat.PARQUET,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
        )

    file_name = file_name if isinstance(file_name, list) else [file_name]

    for name in file_name:
        table_id = f"{project_id}.{dataset_name}.staging_{name}"
        gcs_uri = f"gs://{gcs_data_dir_path}/{name}.parquet"

        logging.info(f"Starting load job for {gcs_uri} ...")

        load_job = client.load_table_from_uri(
            gcs_uri,
            table_id,
            job_config=job_config
        )

        load_job.result()
        
        destination_table = client.get_table(table_id)
        print(f"Success! Loaded {destination_table.num_rows} rows into {table_id}")

def merge_table(
        dataset_name: str,
        file_name: str | list = FILE_NAME,
        project_id: str = PROJECT_ID
):
    logging.info(f"Merging table from staging into bronze ...")
    client = bigquery.Client(project=project_id)

    try:
        file_name = file_name if isinstance(file_name, list) else [file_name]
        
        for name in file_name:
            logging.info(f"Start merging table {name} ...")

            sql = Path(f"src/query/{name}_incremental_load.sql").read_text()

            sql = sql.format(
                source_table=f"{project_id}.{dataset_name}.staging_{file_name}",
                target_table=f"{project_id}.{dataset_name}.bronze_{file_name}"
            )

            client.query(sql).result()

            logging.info(f"Successfully merged table {name}.")

    except Exception as e:
        logging.error(f"Failed merge table: {e}")
        raise