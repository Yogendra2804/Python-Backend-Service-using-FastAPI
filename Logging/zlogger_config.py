import logging
import os

Logging_dir = os.path.dirname(__file__)

FASTAPI_dir = os.path.dirname(Logging_dir)

# base_dir = os.path.dirname(FASTAPI_dir)

logging_dir = os.path.join(FASTAPI_dir , "Logging" , "logs")

file_logger_dir = os.path.join(logging_dir , "app.log")

logging.basicConfig(
    level=logging.INFO,
    filemode='a',
    filename=file_logger_dir,
    format= "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
