import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%d_%M_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "Log", LOG_FILE)
os.makedirs(log_path, exist_ok=False)

Log_file_path = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=Log_file_path,
    format="[ %(asctime)s ] %(lineno)s %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,
)


# if __name__ == "__main__":
#    logging.info("divide by zero error")
