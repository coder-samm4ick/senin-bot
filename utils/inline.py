# utils/keyboards.py
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CopyTextButton

import config as cfg


def main_menu(user_id: int):
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Мои реквизиты", callback_data="main:my_details", icon_custom_emoji_id="5769126056262898415")
    keyboard.button(text="Создать сделку", callback_data="main:create_deal", icon_custom_emoji_id="5357080225463149588")
    keyboard.button(text="Баланс", callback_data="main:my_balance", icon_custom_emoji_id="5375296873982604963")
    keyboard.button(text="Мои сделки", callback_data="main:my_deals", icon_custom_emoji_id="5411520005386806155")
    keyboard.button(text="Рефералы", callback_data="main:referral", icon_custom_emoji_id="6033125983572201397")
    keyboard.button(text="Техподдержка", url=f"t.me/{cfg.menejer_user}", icon_custom_emoji_id="6033125983572201397")
    """if user_id in cfg.owners:
        keyboard.button(text="Админ панель", callback_data="admin_panel", icon_custom_emoji_id="5971831809506282660")
        keyboard.adjust(2, 2, 2, 1)
    else:
        keyboard.adjust(2, 2, 1, 1)"""
    keyboard.adjust(2, 2, 1, 1)
    return keyboard.as_markup()

def details_menu():
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="TON-Кошелёк", callback_data="details:ton_wallet", icon_custom_emoji_id="6039802097916974085")
    keyboard.button(text="Карта", callback_data="details:carta", icon_custom_emoji_id="5902056028513505203")
    keyboard.button(text="Stars", callback_data="details:stars", icon_custom_emoji_id="5893494861612455015")
    keyboard.button(text="USDT (TRC20)", callback_data="details:usdt_wallet", icon_custom_emoji_id="5893473283696759404")
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    
    keyboard.adjust(2, 2)
    
    return keyboard.as_markup()

def back_details_menu():
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Назад к реквизитам", callback_data="main:my_details", icon_custom_emoji_id="6039539366177541657")
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    
    keyboard.adjust(1)
    
    return keyboard.as_markup()

def pay_deal(amount: int, currency: str, deal_id: str):
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text=f"Оплатить с баланса ({amount} {currency})", callback_data=f"pay_deal:{amount}:{currency}:{deal_id}", icon_custom_emoji_id="5224257782013769471")
    keyboard.button(text="Техподдержка", url=f"t.me/{cfg.menejer_user}", icon_custom_emoji_id="6033125983572201397")
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    keyboard.adjust(1)
    return keyboard.as_markup()

def respondent_pay_deal(deal_id: str):
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Передать товар менеджеру", url=f"t.me/{cfg.menejer_user}", icon_custom_emoji_id="5895652322469482989")
    keyboard.button(text="Готово - передано", callback_data=f"res_pay_deal:{deal_id}", icon_custom_emoji_id="5895514131896733546")
    keyboard.button(text="Техподдержка", url=f"t.me/{cfg.menejer_user}", icon_custom_emoji_id="6033125983572201397")
    keyboard.adjust(1)
    return keyboard.as_markup()

def confirm_send(deal_id: str):
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Подтвердить", callback_data=f"confirm_deal:{deal_id}", icon_custom_emoji_id="5895514131896733546")
    keyboard.adjust(1)
    return keyboard.as_markup()

def choose_role():
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Продавец", callback_data="new_deal:role_seller", icon_custom_emoji_id="5431492767249342908")
    keyboard.button(text="Покупатель", callback_data="new_deal:role_buyer", icon_custom_emoji_id="5217822164362739968")
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    keyboard.adjust(2, 1)
    return keyboard.as_markup()

def choise_payment():
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Карта", callback_data="new_deal:payment:carta", icon_custom_emoji_id="5902056028513505203")
    keyboard.button(text="Stars", callback_data="new_deal:payment:stars", icon_custom_emoji_id="5893494861612455015")
    keyboard.button(text="Крипта", callback_data="new_deal:payment:crypto", icon_custom_emoji_id="6039802097916974085")
    keyboard.button(text="Назад", callback_data="new_deal:back:choise_role", icon_custom_emoji_id="6039539366177541657")
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    keyboard.adjust(2, 1)
    return keyboard.as_markup()

def choise_crypto():
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="TON", callback_data="new_deal:payment:ton", icon_custom_emoji_id="6039802097916974085")
    keyboard.button(text="USDT (TRC20)", callback_data="new_deal:payment:usdt", icon_custom_emoji_id="5893473283696759404")
    keyboard.button(text="Назад", callback_data="new_deal:back:choise_payment", icon_custom_emoji_id="6039539366177541657")
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    keyboard.adjust(2, 1)
    return keyboard.as_markup()
    

def deal_amount():
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Назад", callback_data="new_deal:back:shoise_payment", icon_custom_emoji_id="6039539366177541657")
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    keyboard.adjust(1)
    return keyboard.as_markup()

def deal_back_amount():
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Назад", callback_data="new_deal:back:amount", icon_custom_emoji_id="6039539366177541657")
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    keyboard.adjust(1)
    return keyboard.as_markup()

def referral_menu(url):
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Скопировать Реф. ссылку", copy_text=CopyTextButton(text=url))
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    keyboard.adjust(1)
    return keyboard.as_markup()


def deal_role():
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Я покупатель", callback_data="deal:buyyer", icon_custom_emoji_id="5217822164362739968")
    keyboard.button(text="Я продавец", callback_data="deal:seller", icon_custom_emoji_id="5217822164362739968")
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    keyboard.adjust(2, 1)
    return keyboard.as_markup()

def deallll():
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Техподдержка", url=f"t.me/{cfg.menejer_user}", icon_custom_emoji_id="6033125983572201397")
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    keyboard.adjust(1)
    return keyboard.as_markup()

def back_menu(user_id: int = None):
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    keyboard.adjust(1)
    return keyboard.as_markup()

DEALS_PER_PAGE = 4  # 4 сделки с каждой стороны = 8 кнопок (2 колонки по 4)

def _deal_status_emoji(status: str) -> str:
    return {
        "pending":   "⏳",
        "active":    "💳",
        "paid":      "📦",
        "sended":    "📦",
        "completed": "✅",
        "cancelled": "❌",
        "dispute":   "❌",
    }.get(status, "❓")

def my_deals_menu(deals: list, page: int = 0):
    """
    Клавиатура «Мои сделки»:
    - До 4 сделок слева (чётные) и 4 справа (нечётные) → 2 колонки по 4 строки
    - 5-я строка: ◀ страница N/M ▶
    - Поиск по ID
    - Назад в меню
    """
    keyboard = InlineKeyboardBuilder()

    per_page = DEALS_PER_PAGE * 2  # 8 сделок на странице
    total = len(deals)
    total_pages = max(1, (total + per_page - 1) // per_page)
    page = max(0, min(page, total_pages - 1))

    start = page * per_page
    page_deals = deals[start:start + per_page]

    # Добавляем кнопки сделок парами (2 в ряд)
    for deal in page_deals:
        emoji = _deal_status_emoji(deal.status)
        label = f"{emoji} #{deal.deal_id} · {deal.amount} {deal.currency}"
        keyboard.button(text=label, callback_data=f"my_deal_info:{deal.deal_id}:{page}")

    # Выравниваем по 2 в ряд
    rows = [2] * (len(page_deals) // 2)
    if len(page_deals) % 2 == 1:
        rows.append(1)

    # Пагинация
    if total_pages > 1:
        if page > 0:
            keyboard.button(text=" ", callback_data=f"my_deals_page:{page - 1}", icon_custom_emoji_id="5321301893757018871")
        keyboard.button(text=f"{page + 1} / {total_pages}", callback_data="my_deals_noop")
        if page < total_pages - 1:
            keyboard.button(text=" ", callback_data=f"my_deals_page:{page + 1}", icon_custom_emoji_id="5321356066179525416")
        nav_count = (1 if page > 0 else 0) + 1 + (1 if page < total_pages - 1 else 0)
        rows.append(nav_count)

    # Поиск + назад
    keyboard.button(text="Поиск по ID", callback_data="my_deals_search", icon_custom_emoji_id="5893382531037794941")
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    rows += [1, 1]

    keyboard.adjust(*rows)
    return keyboard.as_markup()

def my_deal_info_menu(deal_id: str, page: int = 0):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="◀ К списку сделок", callback_data=f"my_deals_page:{page}")
    keyboard.button(text="Назад в меню", callback_data="main_menu", icon_custom_emoji_id="5960671702059848143")
    keyboard.adjust(1)
    return keyboard.as_markup()
