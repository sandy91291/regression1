import logging  # Import logging module for logging errors and messages
import sys  # Import sys module to access system-specific parameters and functions  
import os  # Import os module to interact with the operating system
from datetime import datetime  # Import datetime module to work with dates and times

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"  # Define the log file name with current timestamp
logs_path = os.path.join(os.getcwd(), "logs")  # Define the logs directory path
os.makedirs(logs_path, exist_ok=True)  # Create the logs directory if it doesn't exist
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  # Full path for the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file path
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',  # Define the log message format
    level=logging.INFO,  # Set the logging level to INFO
)