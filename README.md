# GADM: all countries consolidated shapefile

GADM data in version 4.1 can be downloaded from https://geodata.ucdavis.edu/gadm/gadm4.1/. More information about GADM project: https://gadm.org/.

Data for individual countries is available in shapefiles. Separate shapefiles are provided for different levels of administrative boundaries (Level 0 is country boundaries).

Unfortunately there is no longer consolidated shapefile with borders for all countries. I find having such file useful, so I created simple script to fetch all countries and consolidate Level-0 shapefiles into one file. 

## `getAllCountries.py`

This script will:
1. fetch list of available countries 
2. download zip file for each country
3. unpack downloaded zip files

Please make sure to update `url` (if needed) and `localPath` before running.

## `consolidateSHP.py`

This script will:
1. scan local files for Level-0 shapefiles
2. load all Level-0 shapefiles into memory
3. consolidate downloaded data into one variable
4. save one consolidated shapefile to disk

Please make sure to update `dataPath` and `targetPath` before running. 