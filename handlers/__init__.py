# handlers/__init__.py
from .start import st_router
from .deal import deal_router
from .callback import call_router
from .details import details_router
from .workers import workers_router
from . import errors

from aiogram import Router

handler_router = Router()
handler_router.include_routers(st_router, call_router, deal_router, details_router, workers_router)