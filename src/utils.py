# src/utils.py

import logging
from typing import Optional


def setup_logging(log_level: str = "INFO", log_file: Optional[str] = None):
    """Configure logging system"""
    handlers = [logging.StreamHandler()]
    if log_file:
        handlers.append(logging.FileHandler(log_file))

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=log_level,
        handlers=handlers
    )
    logging.captureWarnings(True)


def format_duration(seconds: float) -> str:
    """Convert seconds to human-readable duration"""
    # Can be used for performance metrics
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes)}m {seconds:.2f}s"
