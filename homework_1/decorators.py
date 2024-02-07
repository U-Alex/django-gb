import logging
from typing import Callable


logger = logging.getLogger(__name__)


def custom_log(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"view: {func.__name__} | {args}")
        # print(*result.__dict__['_container'])
        return result
    return wrapper


