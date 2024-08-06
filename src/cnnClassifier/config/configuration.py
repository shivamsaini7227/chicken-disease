import sys
import os
sys.path.append(os.path.abspath('src'))

from cnnClassifier.constants import CONFIG_FILE_PATH , PARAM_FILE_PATH 
from cnnClassifier.utils.common import read_yaml , create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig  #class under the config_entity 
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig 
from pathlib import Path


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAM_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        print(self.config)
        print(self.params)

        

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_file = config.local_file,
            unzip_dir = config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_model_prepare_config(self) -> PrepareBaseModelConfig:
        config = self.config.base_model

        create_directories([config.root_dir])

        model_prepare_config = PrepareBaseModelConfig(
            root_dir= Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path = Path(config.updated_base_model_path),
            params_image_size= self.params.IMAGE_SIZE,
            params_learning_rate =self.params.LEARNING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes = self.params.CLASSES
        )

        return model_prepare_config      
    





      