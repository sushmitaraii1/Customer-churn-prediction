import logging
import os

import requests
from tqdm import tqdm

url = "http://bit.ly/texam-2021"
def download_dataset(url):
   
    try:
        response = requests.get(url, stream=True)
        print("Dataset Successfully Downloaded !!")
        with open("churn.csv", "wb") as handle:
            for data in tqdm(response.iter_content()):
                handle.write(data)

    except requests.exceptions.RequestException as e:
       print("Dataset Download Failed, Exception:{}".format(e))

    return True

if __name__ == "__main__":
    print(download_dataset(url=url))
