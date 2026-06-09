import logging
from datetime import datetime

class LoggerService:

    def __init__(self):
        logging.basicConfig(
            filename="logs/app.log",
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s"
        )

    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)