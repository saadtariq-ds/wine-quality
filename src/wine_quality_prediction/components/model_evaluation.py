import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import joblib
from pathlib import Path
from src.wine_quality_prediction.constants import *
from src.wine_quality_prediction.utils.common import save_json
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse
from src.wine_quality_prediction.entity.config_entity import ModelEvaluationConfig
from src.wine_quality_prediction import logger


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluation_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(y_true=actual, y_pred=pred))
        mae = mean_absolute_error(y_true=actual, y_pred=pred)
        r2 = r2_score(y_true=actual, y_pred=pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)
            logger.info("Evaluating on Test Data")
            (rmse, mae, r2) = self.evaluation_metrics(actual=test_y, pred=predicted_qualities)

            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_parameters)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)
            logger.info("Parameters and Metrics are Logged into MLFlow")

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="wine_quality_model")
            else:
                mlflow.sklearn.log_model(model, "model")