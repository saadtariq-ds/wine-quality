import pandas as pd
from src.wine_quality_prediction.entity.config_entity import DataValidationConfig
from src.wine_quality_prediction import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_directory)
            all_columns = list(data.columns)

            all_schema_columns = self.config.all_schema.keys()

            for column in all_columns:
                if column not in all_schema_columns:
                    logger.info(f"Column: {column} is not present in the dataset.")
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

                else:
                    logger.info(f"Column: {column} is present in the dataset.")
                    validation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        except Exception as e:
            logger.exception(f"Error occurred while validating the data: {e}")
            raise e
        
    def validate_data_types(self) -> bool:
        """
        Validate column datatypes according to schema.
        """
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_directory)

            for column, dtype in self.config.all_schema.items():
                actual_dtype = str(data[column].dtype)

                if actual_dtype != dtype:
                    validation_status = False
                    logger.error(
                        f"Datatype mismatch for column '{column}'. "
                        f"Expected: {dtype}, Found: {actual_dtype}"
                    )

                else:
                    validation_status = True
                    logger.info(
                        f"Datatype matched for column '{column}' -> {dtype}"
                    )

            with open(self.config.status_file, 'a') as f:
                f.write(f"\nDatatype Validation Status: {validation_status}")

            return validation_status

        except Exception as e:
            logger.exception(f"Error occurred while validating datatypes: {e}")
            raise e