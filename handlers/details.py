# handlers/details.py
import uuid

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from db import db
import config as cfg
from loader import bot
import states.user as stu
import utils.texts as txt
import utils.inline as inb
import utils.prem_emojies as em

details_router = Router()

@details_router.message(stu.UserStates.ton_wallet)
async def new_ton_wallet(message: Message, state: FSMContext):
    user_id = message.from_user.id
    ton_wallet = message.text
    
    user = await db.get_user(user_id)
    
    data = await state.get_data()
    await bot.delete_message(message.chat.id, data["msg_id"])
    await message.delete()
    user.ton_wallet = ton_wallet
    await db.save()
    await message.answer_video(cfg.video, caption=txt.details_text(
                            ton_wallet, user.card_details,
                            user.stars_username, user.usdt_wallet), 
                            reply_markup=inb.details_menu())
    await state.clear()
    
    
@details_router.message(stu.UserStates.usdt_wallet)
async def new_usdt_wallet(message: Message, state: FSMContext):
    user_id = message.from_user.id
    usdt_wallet = message.text
    
    user = await db.get_user(user_id)
    
    data = await state.get_data()
    await bot.delete_message(message.chat.id, data["msg_id"])
    await message.delete()
    user.usdt_wallet = usdt_wallet
    await db.save()
    await message.answer_video(cfg.video, caption=txt.details_text(
                            user.ton_wallet, user.card_details,
                            user.stars_username, usdt_wallet), 
                            reply_markup=inb.details_menu())
    await state.clear()


@details_router.message(stu.UserStates.carta_wallet)
async def new_carta_wallet(message: Message, state: FSMContext):
    user_id = message.from_user.id
    card_details = message.text
    
    user = await db.get_user(user_id)
    
    data = await state.get_data()
    await bot.delete_message(message.chat.id, data["msg_id"])
    await message.delete()
    user.card_details = card_details
    await db.save()
    await message.answer_video(cfg.video, caption=txt.details_text(
                            user.ton_wallet, card_details,
                            user.stars_username, user.usdt_wallet), 
                            reply_markup=inb.details_menu())
    await state.clear()
    
    
@details_router.message(stu.UserStates.stars_username)
async def new_stars_username(message: Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.text
    
    user = await db.get_user(user_id)
    if not username.startswith("@"):
        username = "@" + username
    data = await state.get_data()
    await bot.delete_message(message.chat.id, data["msg_id"])
    await message.delete()
    user.stars_username = username
    await db.save()
    await message.answer_video(cfg.video, caption=txt.details_text(
                            user.ton_wallet, user.card_details,
                            username, user.usdt_wallet), 
                            reply_markup=inb.details_menu())
    await state.clear()