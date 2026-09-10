import os
import pandas as pd
import numpy as np
import time
import random
import re
import requests
import json
import pyarrow

from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from constants.scraper_constants import *
from logger import logging

def absolute(url: str, BASE_URL: str = BASE_URL):
    return urljoin(base=BASE_URL, url=url)

def get_soup(
        url: str,
        headers: dict = None,
        retry: int = 3,
        delay_range: set = (5, 10)) -> None:
    session = requests.session()
    session.headers.update(headers=headers)
    for attempt in range(retry):
        try:
                response = session.get(url=url, timeout=10)
                response.raise_for_status()
                if response.status_code == 429:
                    time.sleep(300)
                    continue

                time.sleep(random.uniform(25, 30))
                return BeautifulSoup(response.content, "html.parser")
        except Exception as e:
            print(f"Attempt {attempt + 1} Failed: {e}")
            time.sleep(random.uniform(*delay_range))
    
    print(f"failed to get soup for {url} after {retry} attempts.")
    return None

def get_value(
    soup,
    selector,
    attr=None,
    multiple=False
):
    try:
        if multiple:
            elements = soup.select(selector)
            results = []
            for el in elements:
                text = el.get(attr) if attr != "text" and attr != None else el.get_text() if attr == "text" else el
                if attr == "text":
                    text = re.sub(r"[\n\t]", "", text).strip()

                results.append(text)

            return results

        else:
            element = soup.select_one(selector)
            if not element:
                return None

            text = element.get(attr) if attr != "text" and attr != None else element.get_text() if attr == "text" else element
            if attr == "text":
                text = re.sub(r"[\n\t]", "", text).strip()

            return text

    except Exception as e:
        logging.error(f"get_value error: {e}")
        return None

def get_progress(current_unit: int, total_unit: int, current_progress: int):
    new_progress = int((current_unit + 1) / total_unit)
    if current_progress < new_progress:
        if new_progress // 10 == 0:
            print(f"{new_progress}% of Completion")
        return new_progress
        
    else:
        return 0

def load_json(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

def save_file(data: list|pd.DataFrame, file_name: str, format: str):
    new_data = data

    if format == "json":
        if not isinstance(data, list):
            new_data = list(data)
        dir_path = Path("data") / "link"
        os.makedirs(dir_path, exist_ok=True)
        file_path = dir_path / f"{file_name}.{format}"

        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as file:
                old_data = json.load(file)

        old_data.add(new_data)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(old_data, file, indent=2)
        
        logging.info(f"Data has been save in {file_path}")

    else:
        if not isinstance(data, pd.DataFrame):
            new_data = pd.DataFrame(data)
        dir_path = Path("data") / "raw"
        os.makedirs(dir_path, exist_ok=True)
        file_path = dir_path / f"{file_name}.{format}"

        if file_path.exists():
            old_df = pd.read_parquet(file_path)
            new_df = new_data

            new_data = pd.concat(
                [old_df, new_df],
                ignore_index=True
            )

        new_data.to_parquet(path=file_path, index=False)
        logging.info(f"Data has been save in {file_path}")

def save_pipeline( status: str, module: str, completed: bool = False, file_path: str = "data/checkpoint/pipeline_state.json"):
    state = {
        "status": status,
        "module": module,
        "completed": completed
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(state, file, indent=2)