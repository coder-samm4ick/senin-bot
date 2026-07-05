# config.py
from aiogram.types import FSInputFile

BOT_TOKEN = "8891656964:AAFVJpGEuGpc_D03GNvzMSvtlDCGqM8Wv90"

# ВАЖНО: Используй SQLite на Render (проще)
db = "sqlite"  # 0 - sqlite, 1 - postgresql
db_url_sqlite = "sqlite+aiosqlite:///db/otc.db"
db_url_postgres = "postgresql+asyncpg://postgres:qwerty@localhost/new"

bot_user = "MrktGuarante_Bot"
project_name = "Mrkt official"
logs_id = -1003487591048
menejer_user = "mrkt_official_sup"

video = FSInputFile("utils/gift.mp4")