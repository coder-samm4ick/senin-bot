from sqlalchemy import Column, Integer, BigInteger, String, Float   , ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy import DateTime
from .connect import Base



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, unique=True)
    balance_rub = Column(Float, default=0.0)
    balance_ton = Column(Float, default=0.0)
    balance_usdt = Column(Float, default=0.0)
    balance_stars = Column(Float, default=0.0)
    username = Column(String, nullable=True)
    deals_count = Column(Integer, default=0)
    
    # Wallets/Details
    ton_wallet = Column(String, default="—")
    usdt_wallet = Column(String, default="—")
    card_details = Column(String, default="—")
    stars_username = Column(String, default="—")
    
    # Referral system
    referrer_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=True)
    referrals_count = Column(Integer, default=0)
    earned_from_referrals = Column(Float, default=0.0)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Deal(Base):
    __tablename__ = 'deals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    deal_id = Column(String, unique=True)
    creator_id = Column(BigInteger, ForeignKey('users.user_id'))
    respondent_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=True)
    
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=True) # ton, card, stars, usdt
    description = Column(Text, nullable=True)
    
    # Statuses: 'pending', 'active', 'completed', 'dispute', 'cancelled'
    status = Column(String, default='pending')
    
    creator_role = Column(String) # 'buyer' or 'seller'
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
class Workers(Base):
    __tablename__ = 'workers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
