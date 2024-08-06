#now we can directly call data_ingestion (components) and configuration files (config)
from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath('src'))
from cnnClassifier.components.model_prep import PrepareBaseModel
from cnnClassifier.config.configuration import  ConfigurationManager
from cnnClassifier import logger

stageName= "base_model_preparation"

class modelPreparationPipeline:
    def __init__(self):
        pass

    def main(self):
           config = ConfigurationManager()
           prepare_base_model_config = config.get_model_prepare_config()
           base_model = PrepareBaseModel(config=prepare_base_model_config)
           base_model.get_base_model()
           base_model.update_base_model()

if __name__== "__main__":
    try:
       logger.info(f'The pipeline 02 {stageName} has started')
       obj1=modelPreparationPipeline()
       obj1.main()
       logger.info(f'The pipeline 02 {stageName} completed')
    except Exception as e:
       logger.exception(e)
       raise e


