import sys
import os
sys.path.append(os.path.abspath('src'))
from cnnClassifier.pipeline.stage_01_dataIngestion import dataIngestionPipeline
from cnnClassifier import logger
stageName="DataIngestionStage"

try:
    logger.info(f'The pipeline {stageName} has started')
    obj1=dataIngestionPipeline()
    obj1.main()
    logger.info(f'The pipeline {stageName} completed')
except Exception as e:
    logger.exception(e)
    raise e


