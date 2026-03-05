import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.wine_quality_prediction.entity.config_entity import DataTransformationConfig
from src.wine_quality_prediction import logger

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def data_splitting(self):
        data = pd.read_csv(self.config.data_directory)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_directory, "train.csv"), index=False, header=True)
        test.to_csv(os.path.join(self.config.root_directory, "test.csv"), index=False, header=True)

        logger.info("Splitted Data into Train and Test Set")
        logger.info(f"Train Shape: {train.shape} and Test Shape: {test.shape}")