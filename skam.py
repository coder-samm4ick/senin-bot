#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import logging
from handlers import handler_router
from db import db
from loader import bot, dp

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Главная функция запуска бота"""
    try:
        # Подключаемся к базе данных
        await db.create_tables()
        logger.info("✅ База данных готова")
        
        # Подключаем роутеры
        dp.include_router(handler_router)
        logger.info("✅ Роутеры подключены")
        
        # Запускаем бота
        logger.info("🚀 Бот запускается...")
        print("🤖 Бот запущен!")
        
        await dp.start_polling(bot)
        
    except asyncio.CancelledError:
        logger.info("⏹️ Бот остановлен")
    except Exception as e:
        logger.error(f"❌ Ошибка: {e}")
        raise
    finally:
        # Закрываем соединения
        await bot.session.close()
        logger.info("🔌 Соединения закрыты")

async def on_startup():
    """Действия при запуске"""
    logger.info("🔄 Выполняется инициализация...")
    await db.create_tables()
    logger.info("✅ Инициализация завершена")

async def on_shutdown():
    """Действия при остановке"""
    logger.info("🔄 Выполняется завершение...")
    await bot.session.close()
    logger.info("✅ Завершение выполнено")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⏹️ Бот выключен пользователем")
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        logger.error(f"Критическая ошибка: {e}")
    finally:
        print("👋 Бот остановлен")