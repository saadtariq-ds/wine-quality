from pathlib import Path
from src.wine_quality_prediction.config.configuration import ConfigurationManager
from src.wine_quality_prediction.components.data_transformation import DataTransformation
from src.wine_quality_prediction import logger


STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        with open(file=Path(data_validation_config.status_file), mode='r') as status_file:
            status_content = status_file.read()

        if "False" in status_content:
            raise Exception("Data Transformation cannot proceed due to Error in Data Validation")
        logger.info("Data Validation successful. Starting Data Transformation.")

        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.data_splitting()


if __name__ == "__main__":
    try:
        logger.info(f"{'>>'*20} {STAGE_NAME} Started {'<<'*20}")
        data_transformation_pipeline = DataTransformationPipeline()
        data_transformation_pipeline.initiate_data_transformation()
        logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")
    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
        raise e
