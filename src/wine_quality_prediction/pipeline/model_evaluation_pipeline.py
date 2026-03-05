from src.wine_quality_prediction.config.configuration import ConfigurationManager
from src.wine_quality_prediction.components.model_evaluation import ModelEvaluation
from src.wine_quality_prediction import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()

        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"{'>>'*20} {STAGE_NAME} Started {'<<'*20}")
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.initiate_model_evaluation()
        logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")
    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
        raise e