# handlers/start.py
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db import db
import config as cfg
from loader import bot
import utils.texts as txt
import utils.inline as inb
import utils.prem_emojies as em

st_router = Router()

@st_router.message(Command("start"))
async def start_cmd(message: Message):
    user_id = message.from_user.id
    parts = message.text.split(maxsplit=1)

    if len(parts) > 1:
        arg = parts[1]
    else:
        arg = None
    
    if arg:
        try:
            key, value = arg.split("_", 1)
            if key == "ref":
                ref_id = int(value)
                await db.add_user(user_id, message.from_user.username, ref_id)
            elif key == "deal":
                deal_id = value
                deal = await db.get_deal(deal_id)
                if deal:
                    if deal.respondent_id == deal.creator_id:
                        return await message.answer(
                            f"<b>{em.undov} Вы не можете присоедениться к своей сделке!</b>",
                            reply_markup=inb.back_menu()
                        )
                    if deal.respondent_id is not None:
                        return await message.answer(
                            f"<b>{em.xxxx} Эта сделка уже занята!</b>",
                            reply_markup=inb.back_menu()
                        )
                    
                    creator = await db.get_user(deal.creator_id)
                    if not await db.get_user(user_id):
                        await db.add_user(user_id, message.from_user.username)
                    
                    user = await db.get_user(user_id)
                    user_chat = await bot.get_chat(creator.user_id)
                    creator_username = user_chat.username if user_chat.username else f"Без юзера / ID {deal.creator_id}"
                    user_username = message.from_user.username if message.from_user.username else f"Без юзера / ID {user_id}"

                    deal.respondent_id = user_id
                    deal.status = "active"
                    
                    # Сохраняем через сессию
                    from db.connect import async_session_factory
                    async with async_session_factory() as sess:
                        sess.add(deal)
                        await sess.commit()

                    if deal.creator_role.lower() == "buyer":
                        await message.answer_video(
                            cfg.video,
                            caption=txt.deal_sign_text(
                                deal_id, True, creator_username, deal.creator_id,
                                creator.deals_count, deal.description, deal.currency, deal.amount
                            )
                        )
                        notify_text = txt.deal_respondet_sign(deal_id, "buyer", user_username, user.deals_count)
                        await bot.send_message(deal.creator_id, notify_text, reply_markup=inb.pay_deal(deal.amount, deal.currency, deal_id))
                    else:
                        notify_text = txt.deal_respondet_sign1(deal_id, user_username, user.deals_count)
                        await bot.send_message(deal.creator_id, notify_text)
                        await message.answer_video(
                            cfg.video,
                            caption=txt.buyer_instruction(deal_id, deal.amount, deal.currency, deal.description),
                            reply_markup=inb.pay_deal(deal.amount, deal.currency, deal_id)
                        )
                    return
        except ValueError:
            pass

    await db.add_user(user_id, message.from_user.username)
    await message.answer_video(cfg.video, caption=txt.welcome_text(), reply_markup=inb.main_menu(user_id))