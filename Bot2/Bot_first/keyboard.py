from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Привет!')
button_bye = KeyboardButton('Пока!')
button_1 = KeyboardButton('Xx_1_xX')
button_2 = KeyboardButton('Xx_2_xX')

greet_kb = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
greet_kb1 = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
greet_kb.add(button_hi)
greet_kb.add(button_bye)
greet_kb1.add(button_1)
greet_kb1.add(button_2)


inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

