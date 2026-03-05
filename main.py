from src.wine_quality_prediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.wine_quality_prediction.pipeline.data_validation_pipeline import DataValidationPipeline
from src.wine_quality_prediction.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.wine_quality_prediction.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.wine_quality_prediction import logger

logger.info("Starting the wine quality prediction application...")


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"{'>>'*20} {STAGE_NAME} Started {'<<'*20}")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")
except Exception as e:
    logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
    raise e

print("*****" * 30)

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"{'>>'*20} {STAGE_NAME} Started {'<<'*20}")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.initiate_data_validation()
    logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")
except Exception as e:
    logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
    raise e

print("*****" * 30)

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"{'>>'*20} {STAGE_NAME} Started {'<<'*20}")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")
except Exception as e:
    logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
    raise e

print("*****" * 30)

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"{'>>'*20} {STAGE_NAME} Started {'<<'*20}")
    model_trainer_pipeline = ModelTrainingPipeline()
    model_trainer_pipeline.initiate_model_training()
    logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")
except Exception as e:
    logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
    raise e