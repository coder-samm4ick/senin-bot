# config.py
from aiogram.types import FSInputFile

BOT_TOKEN = "8891656964:AAFVJpGEuGpc_D03GNvzMSvtlDCGqM8Wv90"


db_list = ["sqlite", "postgresql"] # выбор бд, sqlite - проще в настройке, postgresql - лучше для продакшена
db = db_list[0] # выбор бд, 0 - sqlite, 1 - postgresql
db_url_sqlite = "sqlite+aiosqlite:///db/otc.db"
db_url_postgres = "postgresql+asyncpg://postgres:qwerty@localhost/new"
bot_user = "MrktGuarante_Bot" # юзернейм бота без @, нужен для генерации реферальных ссылок и ссылок на сделки
project_name = "Mrkt official" # название проекта
logs_id = -1003487591048 # ID чата для куда будут отправляться новые оплаты по сделкам (можно создать приватный канал и указать его ID)
menejer_user = "mrkt_official_sup"

video = FSInputFile("utils/gift.mp4") # путь к видео ОБЯЗАТЕЛЬНО