#now we can directly call data_ingestion (components) and configuration files (config)
from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath('src'))
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.config.configuration import  ConfigurationManager
from cnnClassifier import logger

stageName= "data_ingestion_stage"

class dataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
          config= ConfigurationManager()
          data_ingestion_config = config.get_data_ingestion_config()
          data_ingestion= DataIngestion(config=data_ingestion_config)
          data_ingestion.download_file()
          data_ingestion.extract_zip_file() 


if __name__== "__main__":
    try:
       logger.info(f'The pipeline {stageName} has started')
       obj1=dataIngestionPipeline()
       obj1.main()
       logger.info(f'The pipeline {stageName} completed')
    except Exception as e:
       logger.exception(e)
       raise e


