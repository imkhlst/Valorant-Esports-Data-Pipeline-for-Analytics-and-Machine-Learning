import os
import pandas as pd
import numpy as np
import time
import random
import re
import requests
import json

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
                text = el.get(attr) if attr != "text" or attr != None else el.get_text() if attr == "text" else el

                if text:
                    text = re.sub(r"[\n\t]", "", text).strip()

                results.append(text)

            return results

        else:
            element = soup.select_one(selector)

            if not element:
                return None

            text = element.get(attr) if attr != "text" or attr != None else element.get_text() if attr == "text" else element

            if text:
                text = re.sub(r"[\n\t]", "", text).strip()

            return text

    except Exception as e:
        logging.error(f"get_value error: {e}")
        return None

def get_progress(current_unit: int, total_unit: int, current_progress: int):
    new_progress = round((current_unit + 1) / total_unit, 0)
    if current_progress <= new_progress:
        print(f"{new_progress} of Completion")
        return new_progress

def load_json(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

def save_file(data: list|pd.DataFrame, file_name: str, format: str):
    if format == "json":
        dir_path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\link"
        os.makedirs(dir_path, exist_ok=True)
        file_path = dir_path + f"\{file_name}"
        with open(f"{file_name}.{format}", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        
        logging.info(f"Data has been save in {file_path}.{format}")

    else:
        dir_path = r"E:\Valorant-Esports-Data-Pipeline-for-Analytics-and-Machine-Learning\data\raw"
        os.makedirs(dir_path, exist_ok=True)
        file_path = dir_path + f"\{file_name}"
        data.to_parquet(path=f"{file_path}.{format}", index=False)
        logging.info(f"Data has been save in {file_path}.{format}")