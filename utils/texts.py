# utils/texts.py
# Содержит все текстовые сообщения бота
# - WELCOME_TEXT
# - HELP_TEXT
# - ERROR_MESSAGES
# - SUCCESS_MESSAGES

import config as cfg
from utils.prem_emojies import *

def welcome_text():
    return f"""{bag} <b>Добро пожаловать в {cfg.project_name}</b>

<blockquote>{light} <i>Ваш надежный P2p-гарант</i>
{s1} Автоматические сделки с NFT и подарками
{s2} Полная защита обеих сторон
{s3} Реферальная программа — 30% от комиссии
{s4} Передача товаров через менеджера: @{cfg.menejer_user}</blockquote>

{lampa} <b>Выберите действие ниже</b> {down}"""


def referal_text(earned: float, url: str, referrrals_count: int):
    return f"""{urll} <i>Реферальная система</i>

<blockquote><b>{urll} Ссылка: <code>{url}</code>
{ton} Заработано: <code>{earned} TON</code>
{ref_em} Кол-во рефералов: <code>{referrrals_count}</code>
</b></blockquote>

{diamond} <i>Бонус: 30% от комиссии с каждой сделки реферала!</i>"""

# * DETAILS
def not_details():
    return f"""{detailss} <i>Реквизиты не добавлены.</i>

<blockquote>{carta} Пожалуйста, добавьте реквизиты в разделе <u>Мои реквизиты</u></blockquote>"""

def details_text(ton_wallet: str, carta_wallet: int, stars_user: str, usdt_wallet: str):
    return f"""{detailss} <i>Мои реквизиты</i>

<blockquote><b>{ton} TON-Кошелёк: <code>{ton_wallet}</code>
{carta} Карта: <code>{carta_wallet}</code>
{stars} Stars: <code>{stars_user}</code>
{usdt} USDT (TRC20): <code>{usdt_wallet}</code></b></blockquote>"""

def details_new_wallet(wl: str):
    return f"""{detailss} <b>Введите свой {wl}:</b>

<blockquote>{chat} <i>Отправьте его в чат.</i></blockquote>"""

def details_stars_user():
    return f"""{stars} <b>Введите ваш Telegram Username:</b>

<blockquote>{chat} <i>Отправьте ваш @username в чат для получения Stars.</i></blockquote>"""





# * PAYMENTS & BALANCE
def anough_balance():
    return f"""{xxxx} <b>Недостаточно средств на балансе!</b>

<blockquote>{undov} Пожалуйста, пополните баланс что бы оплатить сделку.</blockquote>"""

def pay_succes(deal_id: str, respondent_user: str, amount: float, descp: int):
    return f"""{success} <b>Сделка #{deal_id} успешно оплачена!</b>

<blockquote>{ref_em} <b>Покупатель:</b> @{respondent_user}
{usdt} <b>Сумма:</b> <code>{amount}</code>
{descpp} <b>Товар:</b> <i>{descp}</i></blockquote>

{typing} <i>продавец передаёт товар менеджеру @{cfg.menejer_user}.
После этого вы сможете подтвердить получение.</i>"""

def pay_succes_respondent_text(deal_id: str, amount: float, descp: int):
    return f"""{success} <b>Сделка #{deal_id} успешно оплачена!</b>

<blockquote>{usdt} <b>Сумма:</b> <code>{amount}</code>
{descpp} <b>Товар:</b> <i>{descp}</i></blockquote>

{typing} <i>Выполните условия, согласованные в сделке.</i>
{undov} <b> После передачи товара менеджеру @{cfg.menejer_user} нажмите кнопку ниже:</b>"""

def succes_transfer(deal_id: str):
    return f"""{tochkaa} <i>Передача товара по сделке #{deal_id} зафиксирована!</i>

<b>{undov} Подтвердите передачу товара:</b>"""

def buyer_instruction(deal_id: str, amount: float, currency: str, descp: str):
    return f"""{buyyer} <b>Вы подключились к сделке #{deal_id} как покупатель.</b>

<blockquote>{descpp} <b>Товар</b>: <i>{descp}</i>
{usdt} <b>Сумма</b>: <code>{amount} {currency}</code>
{carta} <b>Реквизиты менеджера (куда переводить): <code>@{cfg.menejer_user}</code></b></blockquote>

{shit} <b>Переводите средства ТОЛЬКО менеджеру @{cfg.menejer_user}!</b>
{typing} <i>После оплаты нажмите кнопку ниже.</i>"""

def menejer_get_pay_succes_text(deal_id: str, buyer: str, seller: str, amount: float, descp: str):
    return f"""{carta} <b>Новая оплата по сделке #{deal_id}!</b>

<blockquote>{ref_em} <b>Покупатель:</b> @{buyer}
{ref_em} <b>Продавец:</b> {seller}
{usdt} <b>Сумма:</b> <code>{amount}</code>
{descpp} <b>Товар:</b> <i>{descp}</i></blockquote>

<i>{success} <b>Сделка #{deal_id} успешно оплачена!</b></i>"""

def deal_payment_method(buyyer: bool):
    return f"""{s1} Способ оплаты

<blockquote>{chat} <i>{buyyer if buyyer else "Каким способом вы хотите оплатить?"}</i></blockquote>
"""

def balance_text(balance_rub: float, balance_ton: float, 
                balance_usdt: float, balance_stars: float, 
                deal_count: int):
    return f"""{detailss} <b>Ваш баланс:</b>

<blockquote>{rubb} <b>Рублей: <code>{balance_rub}</code>
{ton} TON: <code>{balance_ton}</code>
{usdt} USDT: <code>{balance_usdt}</code>
{stars} Stars: <code>{balance_stars}</code></b></blockquote>

<blockquote><b>Количество сделок: <code>{deal_count}</code></b></blockquote>"""

# * DEALS
def deal_respondet_sign(deal_id: str, creator_role: str, username: str, deal_count: int):

    if creator_role.lower() == "buyer":
        respondent_role = "продавец"
        hint = f"{typing} <i>Продавец передаст товар менеджеру после вашей оплаты.</i>"
    else:
        respondent_role = "покупатель"
        hint = f"{typing} <i>Покупатель оплатит сделку через менеджера @{cfg.menejer_user}.</i>"
    return f"""{light} <b>К сделке #{deal_id} присоеденился {respondent_role} @{username}!</b>

<blockquote>{qol} <b>Завершённых сделок у него: {deal_count}</b></blockquote>

{shit} Вся оплата проходит ТОЛЬКО через менеджера @{cfg.menejer_user}.
{hint}"""

def deal_respondet_sign1(deal_id: str, username: str, deal_count: int):
    # Вызывается когда creator=seller, значит respondent=покупатель
    return f"""{light} <b>К сделке #{deal_id} присоеденился покупатель @{username}!</b>

<blockquote>{qol} <b>Завершённых сделок у него: {deal_count}</b></blockquote>

{typing} <i>Покупатель оплатит сделку через менеджера @{cfg.menejer_user}.</i>"""

def deal_sign_text(deal_id: str, text: bool, respondent: str, 
            respondent_id: int, respondent_deal_counts: int, 
            descp: str, currency: str, price: float):
    my_role0 = "продавец" if text else "покупатель"
    creator_role1 = "Покупатель" if text else "Продавец"
    creator_role2 = "покупателя" if text else "продавца"
    if text:
        # respondent = продавец, creator = покупатель
        action_hint = f"{typing} <i>Ожидайте оплату от покупателя через менеджера @{cfg.menejer_user}. После подтверждения — передайте товар менеджеру.</i>"
    else:
        # respondent = покупатель, creator = продавец
        action_hint = f"{typing} <i>Оплатите сделку через менеджера @{cfg.menejer_user}. После передачи товара продавцом — подтвердите получение.</i>"
    return f"""{success} <b>Вы подключились к сделке #{deal_id} как {my_role0}.</b>

<blockquote>{ref_em} <b>{creator_role1}</b>: @{respondent}
{idd} <b>ID {creator_role2}</b>: <code>{respondent_id}</code>
{qol} <b>Сделок у {creator_role2}</b>: <code>{respondent_deal_counts}</code>
{descpp} <b>Описание</b>: {descp}
{detailss} <b>Валюта</b>: <code>{currency}</code>
{usdt} <b>Сумма</b>: <code>{price}</code>
{carta} <b>Реквизиты менеджера: <code>@{cfg.menejer_user}</code></b></blockquote>

{shit} <b>Вся оплата и передача товара проходит ТОЛЬКО через менеджера @{cfg.menejer_user}</b>
{action_hint}"""

def new_deal_role():
    return f"""{bag} <b>Новая сделка

<blockquote><i>{chat} Кем вы выступаете в этой сделке?</i></blockquote>

{seller} Продавец — вы продаёте товар/услугу и получаете оплату.
{buyyer} Покупатель — вы платите и получаете товар/услугу.</b>"""


def new_deal_payment_method(role: str):
    txtt = None
    if role == "buyer":
        txtt = "Каким способом хотите оплатить сделку?"
    elif role == "seller":
        txtt = "Как покупатель переведёт средства?"
    return f"""{s1} <b>Способ оплаты:</b>

<blockquote>{chat} <i>{txtt}</i></blockquote>"""

def deal_choise_crypto():
    return f"""{ton} <b>Выберите криптовалюту:</b>

<blockquote>{chat} <i>Какую монету вы будете использовать для оплаты?</i></blockquote>"""


def new_deal_amount(method: str):
    ttm = None
    if method == "stars":
        ttm = "Stars"
    elif method == "carta":
        ttm = "RUB"
    elif method == "crypto":
        ttm = "TON"
    elif method == "usdt":
        ttm = "USDT"
    return f"""{s2} <b>Укажите количество {ttm}</b>"""

def new_deal_descp():
    return f"""{s3} <b>Введите описание товара:</b>

<blockquote><i>Например: https://t.me/nft/ToyBear-32961
или просто отправьте текстовое описание товара:</i></blockquote>"""

def new_deal_created(deal_id: str, role: str, amount: int, currency: str, descp: str):
    role_display = "Покупатель" if role == "buyer" else "Продавец"
    return f"""{success} <b>Сделка #{deal_id} успешно создана!</b>

<blockquote>{s1} <b>Роль</b>: <i>{role_display}</i>
{s2} <b>Валюта</b>: <code>{currency}</code>
{s3} <b>Сумма</b>: <code>{amount}</code>
{s4} <b>Описание</b>: <i>{descp}</i></blockquote>

{urll} Ссылка сделки: <code>t.me/{cfg.bot_user}?start=deal_{deal_id}</code>"""

# * MY DEALS
def my_deals_text(total: int, completed: int):
    return f"""{qol} <b>Мои сделки</b>

<blockquote>{success} <b>Завершено сделок:</b> <code>{completed}</code>
{urll} <b>Всего сделок:</b> <code>{total}</code></blockquote>

{lampa} <i>Выберите сделку для просмотра подробностей</i>"""

def my_deal_info_text(deal):
    status_map = {
        "pending":   ("⏳", "Ожидание участника"),
        "active":    ("💳", "Ожидает оплаты"),
        "paid":      ("📦", "Товар передаётся"),
        "sended":    ("📦", "Товар у менеджера"),
        "completed": ("✅", "Завершена"),
        "cancelled": ("❌", "Отменена"),
        "dispute":   ("❌", "Спор"),
    }
    emoji, status_text = status_map.get(deal.status, ("❓", deal.status))
    role_text = "Покупатель" if deal.creator_role == "buyer" else "Продавец"
    return f"""{qol} <b>Сделка #{deal.deal_id}</b>

<blockquote>{idd} <b>ID:</b> <code>{deal.deal_id}</code>
{detailss} <b>Валюта:</b> <code>{deal.currency}</code>
{usdt} <b>Сумма:</b> <code>{deal.amount}</code>
{descpp} <b>Описание:</b> <i>{deal.description or '—'}</i>
{ref_em} <b>Ваша роль:</b> {role_text}
{light} <b>Статус:</b> {emoji} {status_text}</blockquote>"""

def deal_not_found_text():
    return f"""{xxxx} <b>Сделка не найдена.</b>

<blockquote>{chat} <i>Убедитесь, что ID правильный и вы являетесь участником этой сделки.</i></blockquote>"""

def search_deal_prompt():
    return f"""{idd} <b>Поиск сделки по ID</b>

<blockquote>{chat} <i>Введите ID сделки в чат:</i></blockquote>"""
