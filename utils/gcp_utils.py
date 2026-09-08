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
    
    if not isinstance(dataset_name, list):
        
        dataset_name = [dataset_name]

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
    if isinstance(file_name, list):
        for i in file_name:
            blob = bucket.blob(f"{blob_name}/{i}.parquet")
            blob.upload_from_filename(f"{Path(local_data_dir_path)}/{i}.parquet")
            logging.info(f"Uploaded {i} into {bucket_name}")

    else:
        blob = bucket.blob(f"{blob_name}/{file_name}.parquet")
        blob.upload_from_filename(f"{Path(local_data_dir_path)}/{file_name}.parquet")
        logging.info(f"Success! uploaded {file_name} into {bucket_name}")

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
    
    if isinstance(file_name, list):
        for i in file_name:
            table_id = f"{project_id}.{dataset_name}.{i}"
            gcs_uri = f"gs://{gcs_data_dir_path}/{i}.parquet"

            logging.info(f"Starting load job for {gcs_uri} ...")

            load_job = client.load_table_from_uri(
                gcs_uri,
                table_id,
                job_config=job_config
            )

            load_job.result()
            
            destination_table = client.get_table(table_id)
            print(f"Success! Loaded {destination_table.num_rows} rows into {table_id}")

    else:
        table_id = f"{project_id}.{dataset_name}.{file_name}"
        gcs_uri = f"gs://{gcs_data_dir_path}/{file_name}.parquet"

        logging.info(f"Starting load job for {gcs_uri} ...")

        load_job = client.load_table_from_uri(
            gcs_uri,
            table_id,
            job_config=job_config
        )

        load_job.result()
        
        destination_table = client.get_table(table_id)
        print(f"Success! Loaded {destination_table.num_rows} rows into {table_id}")