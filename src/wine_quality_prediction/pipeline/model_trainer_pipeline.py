from src.wine_quality_prediction.config.configuration import ConfigurationManager
from src.wine_quality_prediction.components.model_trainer import ModelTrainer
from src.wine_quality_prediction import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()

        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    try:
        logger.info(f"{'>>'*20} {STAGE_NAME} Started {'<<'*20}")
        model_trainer_pipeline = ModelTrainingPipeline()
        model_trainer_pipeline.initiate_model_training()
        logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")
    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
        raise e
