from sqlalchemy import select, or_
from .models import User, Deal, Workers
from sqlalchemy.sql import func
from sqlalchemy import DateTime
from .connect import session, Base, engine




async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def save():
    await session.commit()
    

# ! USER
async def add_user(user_id: int, username: str, referrer_id: int = None):
    user = select(User).where(User.user_id == user_id)
    user = (await session.execute(user)).scalar_one_or_none()
    if not user:
        if referrer_id:
            referrer = await session.execute(select(User).where(User.user_id == referrer_id))
            referrer = referrer.scalar_one_or_none()
            if referrer:
                referrer.referrals_count += 1
                await session.commit()
        user = User(user_id=user_id, username=username, referrer_id=referrer_id)
        session.add(user)
        await session.commit()
    return user

async def get_user(user_id: int):
    user = select(User).where(User.user_id == user_id)
    user = (await session.execute(user)).scalar_one_or_none()
    return user


# * DEALS
async def add_deal(deal_id: str, creator_id: int, respondent_id: int, amount: float, description: str, payment_method: str, creator_role: str):
    new_deal = Deal(deal_id=deal_id, creator_id=creator_id, respondent_id=respondent_id, amount=amount, description=description, currency=payment_method, creator_role=creator_role)
    session.add(new_deal)
    await session.commit()
    return new_deal

async def get_deal(deal_id: str):
    deal = select(Deal).where(Deal.deal_id == deal_id)
    deal = (await session.execute(deal)).scalar_one_or_none()
    return deal

async def get_user_deals(user_id: int):
    """Получить все сделки пользователя (как создатель или участник)"""
    stmt = select(Deal).where(
        or_(Deal.creator_id == user_id, Deal.respondent_id == user_id)
    ).order_by(Deal.created_at.desc())
    result = await session.execute(stmt)
    return result.scalars().all()

async def get_deal_by_id_search(deal_id: str, user_id: int):
    """Поиск сделки по ID, если пользователь участник"""
    stmt = select(Deal).where(
        Deal.deal_id == deal_id,
        or_(Deal.creator_id == user_id, Deal.respondent_id == user_id)
    )
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


# ! WORKERS
async def add_worker(user_id: int):
    worker = select(Workers).where(Workers.user_id == user_id)
    worker = (await session.execute(worker)).scalar_one_or_none()
    if not worker:
        worker = Workers(user_id=user_id)
        session.add(worker)
        await session.commit()
    return worker

async def get_worker(user_id: int):
    worker = select(Workers).where(Workers.user_id == user_id)
    worker = (await session.execute(worker)).scalar_one_or_none()
    return worker