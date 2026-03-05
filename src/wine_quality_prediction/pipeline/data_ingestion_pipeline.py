from src.wine_quality_prediction.config.configuration import ConfigurationManager
from src.wine_quality_prediction.components.data_ingestion import DataIngestion
from src.wine_quality_prediction import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(config=data_ingestion_config)

        data_ingestion.download_data()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"{'>>'*20} {STAGE_NAME} Started {'<<'*20}")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")
    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
        raise e