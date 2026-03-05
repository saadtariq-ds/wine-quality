import os
import json
import yaml
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
from src.wine_quality_prediction import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        ConfigBox: A ConfigBox object containing the contents of the YAML file.
    """
    try:
        with open(file=path_to_yaml, mode='r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file '{path_to_yaml}' read successfully.")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error converting YAML content to ConfigBox: {e}")
        raise ValueError(f"Error converting YAML content to ConfigBox: {e}")
    except Exception as e:
        logger.error(f"Error reading YAML file '{path_to_yaml}': {e}")
        raise ValueError(f"Error reading YAML file '{path_to_yaml}': {e}")
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): A list of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            logger.info(f"Directory '{path}' created successfully or already exists.")
        except Exception as e:
            logger.error(f"Error creating directory '{path}': {e}")
            raise ValueError(f"Error creating directory '{path}': {e}")
        

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        path (Path): The path to the JSON file.
        data (dict): The dictionary to save.
    """
    try:
        with open(file=path, mode='w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"Data saved to JSON file '{path}' successfully.")
    except Exception as e:
        logger.error(f"Error saving data to JSON file '{path}': {e}")
        raise ValueError(f"Error saving data to JSON file '{path}': {e}")
    

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its contents as a ConfigBox object.

    Args:
        path (Path): The path to the JSON file.
    Returns:
        ConfigBox: A ConfigBox object containing the contents of the JSON file.
    """
    try:
        with open(file=path, mode='r') as json_file:
            data = json.load(json_file)
            logger.info(f"Data loaded from JSON file '{path}' successfully.")
            return ConfigBox(data)
    except Exception as e:
        logger.error(f"Error loading data from JSON file '{path}': {e}")
        raise ValueError(f"Error loading data from JSON file '{path}': {e}")
    
@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Saves data to a binary file using joblib.

    Args:
        data (Any): The data to save.
        path (Path): The path to the binary file.
    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"Data saved to binary file '{path}' successfully.")
    except Exception as e:
        logger.error(f"Error saving data to binary file '{path}': {e}")
        raise ValueError(f"Error saving data to binary file '{path}': {e}")
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.

    Args:
        path (Path): The path to the binary file.
    Returns:
        Any: The data loaded from the binary file.
    """
    try:
        data = joblib.load(filename=path)
        logger.info(f"Data loaded from binary file '{path}' successfully.")
        return data
    except Exception as e:
        logger.error(f"Error loading data from binary file '{path}': {e}")
        raise ValueError(f"Error loading data from binary file '{path}': {e}")