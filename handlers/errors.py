from aiogram.types import ErrorEvent
from loader import dp
from utils import logger
import traceback

@dp.errors()
async def errors(event: ErrorEvent):
    exception = event.exception

    tb = traceback.extract_tb(exception.__traceback__)[-1]

    logger.error(
        f"{type(exception).__name__} | "
        f"{tb.name}() | "
        f"line {tb.lineno} | "
        f"{exception}"
    )

    return True