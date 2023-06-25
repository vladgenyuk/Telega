from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMRegister(StatesGroup):
    username = State()
    email = State()