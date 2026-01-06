import logging
import os
import sys

def setup_logging(log_file="output/simulation.log"):
    """
    Sets up logging to both console and a file.
    """
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
    logging.info(f"Logging setup complete. Log file: {log_file}")
