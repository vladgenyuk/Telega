from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData


cb_inline = CallbackData('post', 'action', 'data')

cat_btn = InlineKeyboardButton(text='Посмотреть котика',
                           callback_data=cb_inline.new(action='showcat', data='text'))

kb = InlineKeyboardMarkup().add(cat_btn)

btn = KeyboardButton(text='Посмотреть котика',
                           callback_data=cb_inline.new(action='showcat', data='text'))

kb1 = ReplyKeyboardMarkup().add(btn)