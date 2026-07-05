# handlers/deal.py
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

deal_router = Router()

@deal_router.message(stu.UserStates.deal_amount)
async def new_deal_amount(message: Message, state: FSMContext):
    amount = message.text
    user_id = message.from_user.id
    data = await state.get_data()
    if not amount.isdigit():
        return await message.answer(f"<b>Отправьте корректную сумму сделки, например: 100.</b>")
    try:
        price = int(amount)
    except:
        return await message.answer(f"<b>Отправьте корректную сумму сделки, например: 100.</b>")
    if price <= 0:
        return await message.answer(f"<b>Сумма сделки не может быть ниже нуля!</b>")
    await state.update_data(amount=price)
    await bot.delete_message(message.chat.id, data["msg_id"])
    await message.delete()
    msg = await message.answer_video(cfg.video, caption=txt.new_deal_descp(), reply_markup=inb.deal_back_amount())
    await state.update_data(msg_id=msg.message_id)
    await state.set_state(stu.UserStates.deal_description)
    
@deal_router.message(stu.UserStates.deal_description)
async def new_deal_descp(message: Message, state: FSMContext):
    user_id = message.from_user.id
    descp = message.text
    data = await state.get_data()
    
    await bot.delete_message(message.chat.id, data["msg_id"])
    await message.delete()
    deal_id = uuid.uuid4().hex[:10]
    await db.add_deal(deal_id, user_id, None, data["amount"],
                    descp, data["currency"], data["role"])
    await message.answer(txt.new_deal_created(deal_id, data["role"], data["amount"], data["currency"], descp))
    await state.clear()
        


@deal_router.message(stu.UserStates.search_deal)
async def search_deal_handler(message: Message, state: FSMContext):
    deal_id = message.text.strip()
    user_id = message.from_user.id
    await state.clear()
    deal = await db.get_deal_by_id_search(deal_id, user_id)
    if not deal:
        return await message.answer(txt.deal_not_found_text(), reply_markup=inb.my_deal_info_menu(deal_id, 0))
    await message.answer(txt.my_deal_info_text(deal), reply_markup=inb.my_deal_info_menu(deal.deal_id, 0))

