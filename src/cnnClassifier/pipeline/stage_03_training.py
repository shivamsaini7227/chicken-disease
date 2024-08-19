import sys
import os
sys.path.append(os.path.abspath('src'))

from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml,create_directories
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.training import Training
from cnnClassifier.components.prepare_callback import PrepareCallback
from cnnClassifier import logger
 


stageName= 'Training'

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
    
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )
if __name__== "__main__":
    try:
       logger.info(f'The pipeline 02 {stageName} has started')
       obj1=ModelTrainingPipeline()
       obj1.main()
       logger.info(f'The pipeline 02 {stageName} completed')
    except Exception as e:
       logger.exception(e)
       raise e

