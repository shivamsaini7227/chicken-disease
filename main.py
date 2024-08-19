import sys
import os
sys.path.append(os.path.abspath('src'))
from cnnClassifier.pipeline.stage_01_dataIngestion import dataIngestionPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline
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

STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e

