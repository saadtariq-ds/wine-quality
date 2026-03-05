from src.wine_quality_prediction.config.configuration import ConfigurationManager
from src.wine_quality_prediction.components.data_validation import DataValidation
from src.wine_quality_prediction import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        data_validation = DataValidation(config=data_validation_config)

        data_validation.validate_data_columns()
        data_validation.validate_data_types()


if __name__ == "__main__":
    try:
        logger.info(f"{'>>'*20} {STAGE_NAME} Started {'<<'*20}")
        data_validation_pipeline = DataValidationPipeline()
        data_validation_pipeline.initiate_data_validation()
        logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")
    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
        raise e
