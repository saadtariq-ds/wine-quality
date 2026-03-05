from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_directory: Path
    source_URL: str
    local_data_file: Path
    unzip_directory: Path

@dataclass
class DataValidationConfig:
    root_directory: Path
    unzip_data_directory: Path
    status_file: Path
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_directory: Path
    data_directory: Path

@dataclass
class ModelTrainerConfig:
    root_directory: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str