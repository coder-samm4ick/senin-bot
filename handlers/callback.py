import html, asyncio

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile

from db import db
import config as cfg
from loader import bot
import states.user as stu
import utils.texts as txt
import utils.inline as inb

call_router = Router()

@call_router.callback_query()
async def call_handler(call: CallbackQuery, state: FSMContext):
    data = call.data
    user_id = call.from_user.id
    print(data)
    if data.startswith("main:"):
        user_id = call.from_user.id
        type = data.split(":")[1]
        if type == "my_details":
            await state.clear()
            user = await db.get_user(user_id)
            await call.message.edit_caption(call.inline_message_id,
            txt.details_text(user.ton_wallet, user.card_details,
                            user.stars_username, user.usdt_wallet), 
                            reply_markup=inb.details_menu())
        elif type == "create_deal":
            await call.message.edit_caption(call.inline_message_id,
            txt.new_deal_role(), reply_markup=inb.choose_role())
        elif type == "my_balance":
            user = await db.get_user(user_id)
            await call.message.edit_caption(call.inline_message_id,
            txt.balance_text(user.balance_rub, user.balance_ton,
            user.balance_usdt, user.balance_stars, user.deals_count), reply_markup=inb.back_menu())
        elif type == "my_deals":
            deals = await db.get_user_deals(user_id)
            total = len(deals)
            completed = sum(1 for d in deals if d.status == "completed")
            await call.message.edit_caption(call.inline_message_id,
                txt.my_deals_text(total, completed),
                reply_markup=inb.my_deals_menu(deals, page=0))
        elif type == "referral":
            user = await db.get_user(user_id)
            url = f"t.me/{cfg.bot_user}?start=ref_{user_id}"
            await call.message.edit_caption(call.inline_message_id,
            txt.referal_text(user.earned_from_referrals, url, user.referrals_count),
            reply_markup=inb.referral_menu(url))
    elif data.startswith("new_deal:"):
        user_id = call.from_user.id
        parts = data.split(":")
        role = parts[1]
        user = await db.get_user(user_id)
        if role == "role_seller":
            await state.set_state(stu.UserStates.deal_role)
            await state.update_data(role="seller")
            await call.message.edit_caption(call.inline_message_id,
            txt.new_deal_payment_method("seller"), reply_markup=inb.choise_payment())
        elif role == "role_buyer":
            await state.set_state(stu.UserStates.deal_role)
            await state.update_data(role="buyer")
            await call.message.edit_caption(call.inline_message_id,
            txt.new_deal_payment_method("buyer"), reply_markup=inb.choise_payment())
        elif role == "payment":
            payment = parts[2]

            payments = {
                "carta": {
                    "check": user.card_details,
                    "currency": "RUB",
                    "caption": "carta"
                },
                "stars": {
                    "check": user.stars_username,
                    "currency": "Stars",
                    "caption": "stars"
                },
                "ton": {
                    "check": user.ton_wallet,
                    "currency": "TON",
                    "caption": "crypto"
                },
                "usdt": {
                    "check": user.usdt_wallet,
                    "currency": "USDT",
                    "caption": "usdt"
                }
            }

            if payment == "crypto":
                return await call.message.edit_caption(call.inline_message_id,
                    caption=txt.deal_choise_crypto(),
                    reply_markup=inb.choise_crypto()
                )

            pay = payments.get(payment)

            if not pay:
                return

            if pay["check"] == "—":
                await state.clear()

                return await call.message.edit_caption(call.inline_message_id,
                    caption=txt.not_details(),
                    reply_markup=inb.back_menu()
                )

            msg = await call.message.answer_video(
                cfg.video,
                caption=txt.new_deal_amount(pay["caption"]),
                reply_markup=inb.deal_amount()
            )

            await state.update_data(
                currency=pay["currency"],
                msg_id=msg.message_id
            )

            await state.set_state(stu.UserStates.deal_amount)

            try:
                await call.message.delete()
            except:
                pass
    
    elif data.startswith("pay_deal:"):
        _, amountt, currency, deal_id = data.split(":")
        amount = float(amountt)
        user = await db.get_user(user_id)

        currency_lower = currency.lower()
        if currency_lower == "stars":
            wallet_detail = user.stars_username
            user_balance = user.balance_stars
        elif currency_lower == "rub":
            wallet_detail = user.card_details
            user_balance = user.balance_rub
        elif currency_lower == "ton":
            wallet_detail = user.ton_wallet
            user_balance = user.balance_ton
        elif currency_lower == "usdt":
            wallet_detail = user.usdt_wallet
            user_balance = user.balance_usdt
        else:
            return await call.answer("Неизвестная валюта.")

        if wallet_detail == "—":
            await state.clear()
            return await call.message.edit_caption(call.inline_message_id,
                caption=txt.not_details(),
                reply_markup=inb.back_menu())

        if amount > user_balance:
            return await call.message.answer(txt.anough_balance(), reply_markup=inb.back_menu())
        deal = await db.get_deal(deal_id)
        if deal.status != "active":
            return await call.answer("Это сделка уже оплачена либо не существует.")
        creator = await db.get_user(deal.creator_id)
        respondent = await bot.get_chat(deal.respondent_id)
        respondent_user = respondent.username if respondent.username else f"Без юзера / ID {deal.respondent_id}"
        creator_user = creator.username if creator.username else f"Без юзера / ID {deal.creator_id}"
        deal.status = "paid"
        await db.save()
        await call.message.answer(txt.pay_succes(deal_id, respondent_user, amount, deal.description))
        if deal.creator_role == "buyer":
            await call.bot.send_message(
            deal.respondent_id,
            txt.pay_succes_respondent_text(deal_id, amount, deal.description,),
            reply_markup=inb.respondent_pay_deal(deal_id)
        )
        else:
            await call.bot.send_message(
                deal.creator_id,
                txt.pay_succes_respondent_text(deal_id, amount, deal.description,),
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
    elif data.startswith("res_pay_deal:"):
        _, deal_id = data.split(":")
        
        deal = await db.get_deal(deal_id)
        if deal.status != "paid":
            return await call.answer("Это сделка не оплачена либо уже завершена.")
        deal.status = "sended"
        await db.save()
        await call.message.answer(f"✅ Вы подтвердили передачу товара по сделке #{deal_id}.\nОжидаем подверждение передачи товара.")
        if deal.creator_role == "buyer":
            await call.bot.send_message(deal.creator_id, txt.succes_transfer(deal_id), reply_markup=inb.confirm_send(deal_id))
        else:
            await call.bot.send_message(deal.respondent_id, txt.succes_transfer(deal_id), reply_markup=inb.confirm_send(deal_id))
    
    elif data.startswith("confirm_deal:"):
        _, deal_id = data.split(":")
        deal = await db.get_deal(deal_id)
        if deal.status != "sended":
            return await call.answer(f"Товар не передан")
        deal.status = "completed"
        await db.save()
        await call.message.edit_text(f"✅ Оплата по сделке #{deal_id} подтверждена.")
        await call.message.answer(f"🎉 Сделка #{deal_id} успешно завершена! Спасибо за доверие ♥️")
        if deal.creator_role == "buyer":
            await call.bot.send_message(deal.respondent_id, f"✅ Передача товара по сделке #{deal_id} зафиксирована.")
        else:
            
            await call.bot.send_message(deal.creator_id, f"✅ Передача товара по сделке #{deal_id} зафиксирована.")
            
        
    elif data.startswith("my_deals_page:"):
        page = int(data.split(":")[1])
        deals = await db.get_user_deals(user_id)
        total = len(deals)
        completed = sum(1 for d in deals if d.status == "completed")
        await call.message.edit_caption(call.inline_message_id,
            txt.my_deals_text(total, completed),
            reply_markup=inb.my_deals_menu(deals, page=page))

    elif data == "my_deals_noop":
        await call.answer()

    elif data.startswith("my_deal_info:"):
        parts = data.split(":")
        deal_id_req = parts[1]
        page = int(parts[2]) if len(parts) > 2 else 0
        deal = await db.get_deal_by_id_search(deal_id_req, user_id)
        if not deal:
            await call.answer("Сделка не найдена", show_alert=True)
            return
        await call.message.edit_caption(call.inline_message_id,
            txt.my_deal_info_text(deal),
            reply_markup=inb.my_deal_info_menu(deal_id_req, page))

    elif data == "my_deals_search":
        await state.set_state(stu.UserStates.search_deal)
        await call.message.edit_caption(call.inline_message_id,
            txt.search_deal_prompt(),
            reply_markup=inb.back_menu())

    elif data.startswith("details:"):
        parts = data.split(":")
        wallet = parts[1]
        await call.message.delete()
        if wallet == "ton_wallet":
            await state.set_state(stu.UserStates.ton_wallet)
            msg = await call.message.answer_video(cfg.video, caption=txt.details_new_wallet("TON-адрес"), reply_markup=inb.back_menu())
            await state.update_data(msg_id=msg.message_id)
        elif wallet == "stars":
            await state.set_state(stu.UserStates.stars_username)
            msg = await call.message.answer_video(cfg.video, caption=txt.details_stars_user(), reply_markup=inb.back_menu())
            await state.update_data(msg_id=msg.message_id)
        elif wallet == "carta":
            await state.set_state(stu.UserStates.carta_wallet)
            msg = await call.message.answer_video(cfg.video, caption=txt.details_new_wallet("номер карты"), reply_markup=inb.back_menu())
            await state.update_data(msg_id=msg.message_id)
        elif wallet == "usdt_wallet":
            await state.set_state(stu.UserStates.usdt_wallet)
            msg = await call.message.answer_video(cfg.video, caption=txt.details_new_wallet("USDT-адрес"), reply_markup=inb.back_menu())
            await state.update_data(msg_id=msg.message_id)
    elif data == "main_menu":
        user_id = call.from_user.id
        if call.message.caption:
            await call.message.edit_caption(call.inline_message_id,
            txt.welcome_text(), reply_markup=inb.main_menu(user_id))
        else:
            try:
                await call.message.delete()
            except:
                pass
            await call.message.answer_video(cfg.video, caption=txt.welcome_text(), reply_markup=inb.main_menu(user_id))