"""Logger class."""

import os
from logging import FileHandler, Formatter, Logger, getLogger
from typing import Optional


class LogHandler:
    """Class to handle all logs."""

    def __init__(self) -> None:
        """Initialize class."""
        self.save_file: Optional[str] = None
        self.logger: Optional[Logger] = None

        os.makedirs("logs", exist_ok=True)

    def init_logger(self, log_name: str) -> None:
        """Initialize logger.

        Args:
            log_name (str): Name of logger.
        """
        self.logger = getLogger(log_name)
        self.save_file = f"logs/{log_name}.log"

        self.file_handler = FileHandler(self.save_file)
        formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        self.logger.addHandler(self.file_handler)

    @staticmethod
    def display_log(save_file: str) -> None:
        """Print log in terminal.

        Args:
            save_file (str): Name of log.
        """
        with open(f"logs/{save_file}.log", "r") as file:
            log_content = file.read()
            print(log_content)
