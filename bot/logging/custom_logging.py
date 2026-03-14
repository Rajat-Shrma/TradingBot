import os
import logging
from datetime import datetime

# Ensure log directory exists so logs can be written.
logs_folder_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_folder_path, exist_ok=True)

# Create a log file named with a timestamp for each run.
LOG_FILE_NAME = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_folder_path, LOG_FILE_NAME)

# Configure global logger to write INFO (and above) messages to file with standard format.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | Line: %(lineno)d | Message: %(message)s",
)
