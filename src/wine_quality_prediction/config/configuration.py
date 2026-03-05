from src.wine_quality_prediction.constants import *
from src.wine_quality_prediction.utils.common import read_yaml, create_directories
from src.wine_quality_prediction.entity.config_entity import (
    DataIngestionConfig, DataValidationConfig,
    DataTransformationConfig, ModelTrainerConfig)


class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH):
        self.config_file_path = read_yaml(path_to_yaml=config_file_path)
        self.params_file_path = read_yaml(path_to_yaml=params_file_path)
        self.schema_file_path = read_yaml(path_to_yaml=schema_file_path)

        create_directories([self.config_file_path.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config_file_path.data_ingestion

        create_directories([config.root_directory])

        data_ingestion_config = DataIngestionConfig(
            root_directory=config.root_directory,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_directory=config.unzip_directory
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config_file_path.data_validation
        schema = self.schema_file_path.columns

        create_directories([config.root_directory])

        data_validation_config = DataValidationConfig(
            root_directory=config.root_directory,
            unzip_data_directory=config.unzip_data_directory,
            status_file=config.status_file,
            all_schema=schema
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config_file_path.data_transformation

        create_directories([config.root_directory])

        data_transformation_config = DataTransformationConfig(
            root_directory=config.root_directory,
            data_directory=config.data_directory,
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config_file_path.model_trainer
        params = self.params_file_path.elastic_net
        schema = self.schema_file_path.target_column

        create_directories([config.root_directory])

        model_trainer_config = ModelTrainerConfig(
            root_directory=config.root_directory,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name,
        )

        return model_trainer_config