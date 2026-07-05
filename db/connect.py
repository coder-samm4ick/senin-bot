from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import NullPool

import config as cfg

Base = declarative_base()

engine = create_async_engine(
    cfg.db_url_postgres if cfg.db == "postgresql" else cfg.db_url_sqlite,
    echo=False
)

async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# НЕ ИСПОЛЬЗУЙ ГЛОБАЛЬНУЮ СЕССИЮ!
# session: AsyncSession = async_session_factory()  # <-- УБРАТЬ!