import pandas as pd
import numpy as np
import time
import random
import re
import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from constants.scraper_contants import *
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
        selector: str,
        select_option: bool = False):
    list_result = []
    try:
        if select_option == True:
            container = soup.select_one(selector)
        else:
            container = soup.select(selector)

        # Need to fix
        if not container:
            logging.warning(f"{selector} does not exist.")
        elif len(container) > 1:
            for i in range(len(container)):
                value = container[i].get_text().strip()
                if "\n" or "\t" in value:
                    value = re.sub(r"[\n\t]", "", value)
                list_result.append(value)
        elif len(container) == 1:
            value = container.get_text().strip()
            if "\n" or "\t" in value:
                value = re.sub(r"[\n\t]", "", value)
        else:
            logging.warning("length of container must be greater than zero.")

        return list_result if len(container) > 1 else value
    
    except Exception as e:
        logging.error(f"Error occurs when running get_value method: {e}")