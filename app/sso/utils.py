from typing import Dict, Any

import logging
import datetime
import json


def _logger(msg: str, ldata: Dict[str, Any] = None) -> None:
    dt = datetime.datetime.now()
    logger = logging.getLogger("django")

    logger.info(f"[{dt}] {msg}")
    if ldata is not None:
        logger.info(f"[{dt}] [DATA] {json.dumps(ldata)}")


def log(msg: str, ldata: dict = None) -> None:
    _logger(f"[INFO] {msg}", ldata)


def error(msg: str, ldata: dict = None) -> None:
    _logger(f"[ERROR] {msg}", ldata)
