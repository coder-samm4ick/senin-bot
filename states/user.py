from aiogram.fsm.state import StatesGroup, State

class UserStates(StatesGroup):
    # Details states
    ton_wallet = State()
    usdt_wallet = State()
    carta_wallet = State()
    stars_username = State()

    # Deal creation states
    deal_role = State()
    deal_amount = State()
    deal_currency = State()
    deal_description = State()

    # My deals search
    search_deal = State()
    