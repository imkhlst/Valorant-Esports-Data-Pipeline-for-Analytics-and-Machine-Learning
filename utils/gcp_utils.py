from logger import logging
from pathlib import Path
from google.cloud import storage, bigquery
from constants.gcp_constants import *
from constants.scraper_constants import FILE_NAME

def create_bucket(
        bucket_name: str = BUCKET_NAME,
        location: str = LOCATION
):
    logging.info(f"Creating a new Storage bucket ...")
    client = storage.Client()

    bucket = client.bucket(bucket_name)
    bucket.location = location
    new_bucket = client.create_bucket(bucket)

    logging.info(f"Success! created bucket {bucket_name} in {location}")

def create_dataset(
        dataset_name: str | list = DATASET_NAME,
        project_id: str = PROJECT_ID,
        location: str = LOCATION
):
    logging.info(f"Creating a new BigQuery dataset ...")
    client = bigquery.Client(project_id=project_id)
    
    if isinstance(dataset_name, list):
        for i in dataset_name:
            dataset_id = f"{project_id}.{i}"
            dataset = bigquery.Dataset(dataset_id)
            dataset.location = location

            client.create_dataset(dataset)
            logging.info(f"Created dataset {dataset_id} in {location}")

    else:
        dataset_id = f"{project_id}.{dataset_name}"
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = location

        client.create_dataset(dataset)
        logging.info(f"Success! created dataset {dataset_id} in {location}")

def upload_data(
        file_name: str | list = FILE_NAME,
        bucket_name: str = BUCKET_NAME,
        blob_name: str = BLOB_NAME,
        local_data_dir_path: str = LOCAL_DATA_DIR_PATH
):
    logging.info(f"Uploading data into storage bucket ...")
    client = storage.Client()
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
        file_name: str | list = FILE_NAME,
        project_id: str = PROJECT_ID,
        dataset_name: str | list = DATASET_NAME,
        gcs_data_dir_path: str = GCS_DATA_DIR_PATH
):
    logging.info(f"Loading table into BigQuery dataset ...")
    client = bigquery.Client(project_id=project_id)
    job_config = bigquery.LoadJobConfig(
            autodetect=True,
            source_format=bigquery.SourceFormat.PARQUET,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
        )
    
    if isinstance(file_name, list):
        for i in file_name:
            table_id = f"{project_id}.{dataset_name[0]}.{i}"
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
        table_id = f"{project_id}.{dataset_name[0]}.{file_name}"
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