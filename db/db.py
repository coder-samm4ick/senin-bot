from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User, Deal, Workers
from .connect import session, Base, engine

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncSession:
    """Получить свежую сессию для запроса"""
    from .connect import async_session_factory
    return async_session_factory()

# ! USER
async def add_user(user_id: int, username: str, referrer_id: int = None):
    async with await get_session() as sess:
        # Проверяем существование пользователя
        stmt = select(User).where(User.user_id == user_id)
        result = await sess.execute(stmt)
        user = result.scalar_one_or_none()
        
        if not user:
            # Обработка реферала
            if referrer_id:
                ref_stmt = select(User).where(User.user_id == referrer_id)
                ref_result = await sess.execute(ref_stmt)
                referrer = ref_result.scalar_one_or_none()
                if referrer:
                    referrer.referrals_count += 1
                    await sess.commit()
            
            # Создаём пользователя
            user = User(user_id=user_id, username=username, referrer_id=referrer_id)
            sess.add(user)
            await sess.commit()
        
        return user

async def get_user(user_id: int):
    async with await get_session() as sess:
        stmt = select(User).where(User.user_id == user_id)
        result = await sess.execute(stmt)
        return result.scalar_one_or_none()

# * DEALS
async def add_deal(deal_id: str, creator_id: int, respondent_id: int, amount: float, description: str, payment_method: str, creator_role: str):
    async with await get_session() as sess:
        new_deal = Deal(
            deal_id=deal_id,
            creator_id=creator_id,
            respondent_id=respondent_id,
            amount=amount,
            description=description,
            currency=payment_method,
            creator_role=creator_role
        )
        sess.add(new_deal)
        await sess.commit()
        return new_deal

async def get_deal(deal_id: str):
    async with await get_session() as sess:
        stmt = select(Deal).where(Deal.deal_id == deal_id)
        result = await sess.execute(stmt)
        return result.scalar_one_or_none()

async def get_user_deals(user_id: int):
    async with await get_session() as sess:
        stmt = select(Deal).where(
            or_(Deal.creator_id == user_id, Deal.respondent_id == user_id)
        ).order_by(Deal.created_at.desc())
        result = await sess.execute(stmt)
        return result.scalars().all()

async def get_deal_by_id_search(deal_id: str, user_id: int):
    async with await get_session() as sess:
        stmt = select(Deal).where(
            Deal.deal_id == deal_id,
            or_(Deal.creator_id == user_id, Deal.respondent_id == user_id)
        )
        result = await sess.execute(stmt)
        return result.scalar_one_or_none()

# ! WORKERS
async def add_worker(user_id: int):
    async with await get_session() as sess:
        stmt = select(Workers).where(Workers.user_id == user_id)
        result = await sess.execute(stmt)
        worker = result.scalar_one_or_none()
        
        if not worker:
            worker = Workers(user_id=user_id)
            sess.add(worker)
            await sess.commit()
        
        return worker

async def get_worker(user_id: int):
    async with await get_session() as sess:
        stmt = select(Workers).where(Workers.user_id == user_id)
        result = await sess.execute(stmt)
        return result.scalar_one_or_none()