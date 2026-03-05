import os
import sys
import logging

logging_message_format = "[%(asctime)s] %(levelname)s: %(module)s: %(message)s]"

log_directory = "logs"
log_file_path = os.path.join(log_directory, "wine_quality_prediction.log")

os.makedirs(log_directory, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_message_format,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("wine_quality_prediction_logger")