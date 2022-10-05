import requests
import re
import zipfile
import logging
import time

def downloadFile(url, localFilename):
    logging.info(f"Downloading {url} to {localFilename}...")
    ts = time.time()
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(localFilename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
    except:
        logging.info(f"Downloading {url} to {localFilename}: failed")
        raise
    logging.info(f"Downloading {url} to {localFilename}: done in {time.time() - ts} seconds.")
    return True

def getCountryList(url):
    logging.info(f"Getting country list from {url}...")
    ts = time.time()
    html = requests.get(url).text
    filesToDownload = list(set(re.findall("gadm[0-9]{2}_[A-Z]{3}_shp.zip", html)))
    logging.info(f"Getting country list from {url}: done in {time.time() - ts} seconds.")

    return filesToDownload

def unzip(file, target):
    logging.info(f"Unzipping {file} to {target}...")
    ts = time.time()
    with zipfile.ZipFile(file,"r") as zip_ref:
        zip_ref.extractall(target)
    logging.info(f"Unzipping {file} to {target}: done in {time.time() - ts} seconds.")

def processFiles(filesToDownload, localPath):
    for file in filesToDownload:
        try:
            downloadFile(f"{url}/{file}", f"{localPath}/{file}")
            countryCode = re.findall("[A-Z]{3}", file)[0]
            unzip(f"{localPath}/{file}", f"{localPath}/{countryCode}")
        except:
            raise

if __name__ == "__main__":
    logging.basicConfig(
        level = logging.INFO,
        format = '[%(asctime)s] %(levelname)s: %(message)s',
        datefmt = '%Y-%m-%d %I:%M:%S'
    )

    url = "https://geodata.ucdavis.edu/gadm/gadm4.1/shp/"
    localPath = "/media/RAID/DATA/GADM/4.1/SHP/data/"

    filesToDownload = getCountryList(url)
    processFiles(filesToDownload, localPath)