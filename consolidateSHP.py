import geopandas as gp
import pandas as pd
import logging
import glob
import time

def consolidateSHP(dataPath, targetPath):
    logging.info(f"Consolidating shapefiles from {dataPath} to {targetPath}...")
    ts = time.time()
    files = glob.glob(dataPath)
    logging.info(f"Found {len(files)} shapefiles to consolidate.")
    data = []
    for file in files:
        try:
            data.append(gp.read_file(file))
            logging.info(f"Consolidating {file}: done.")
        except:
            logging.info(f"Consolidating {file}: failed.")
            raise
    
    try:
        logging.info(f"Consolidating in memory...")
        result = gp.GeoDataFrame(pd.concat(data, ignore_index=True))

        logging.info(f"Saving to file...")
        result.to_file(targetPath)

        
    except:
        raise
    logging.info(f"Consolidating shapefiles from {dataPath} to {targetPath}: done in {time.time() - ts} seconds.")


if __name__ == "__main__":
    logging.basicConfig(
        level = logging.INFO,
        format = '[%(asctime)s] %(levelname)s: %(message)s',
        datefmt = '%Y-%m-%d %I:%M:%S'
    )

    dataPath = "/media/RAID/DATA/GADM/4.1/SHP/data/*/*0.shp"
    targetPath = "/media/RAID/DATA/GADM/4.1/SHP/consolidated/consolidated.shp"

    consolidateSHP(dataPath, targetPath)