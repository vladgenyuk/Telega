import asyncio
import requests

from aiogram.types import Message, InputMediaVideo, InputMediaPhoto
from aiogram.dispatcher import FSMContext

from keyboard import kb1
from bot import dp, bot
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from crud import UserCRUD
from states import FSMRegister


DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


PHOTO = 'https://vk.com/club47724318'

KITTENS = [
    'https://www.championat.com/cybersport/news-4575511-tesla-otlozhila-sozdanie-mashiny-buduschego-cybertruck-azh-do-2023-goda.html',
    'https://www.autonews.ru/news/621e39399a794715dc9153dc',
]


@dp.message_handler(commands=['help'])
async def help_message(message: Message):
    msg = 'Я могу ответить на следующие команды: \n /audio /photo, /group, ' \
          '/file,\n /video, /test_kb, /cat, /register, '
    await message.reply('Привет !\n' + msg)


@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['photo'])
async def photo_send(message: Message):
    await bot.send_photo(message.from_user.id, PHOTO, caption='BANDIT')


@dp.message_handler(commands=['video'])
async def video_send(message: Message):
    await bot.send_video(message.from_user.id, 'BAACAgIAAxkDAAIBbWLRdz4W-U1vKtZJT2ViAV2yF7kxAAJ5HAACifWQSrOQebLf4Ab_KQQ')


@dp.message_handler(commands=['group'])
async def process_group_command(message: Message):
    media = [InputMediaVideo('BAACAgIAAxkDAAIBbWLRdz4W-U1vKtZJT2ViAV2yF7kxAAJ5HAACifWQSrOQebLf4Ab_KQQ', 'ёжик и котятки')]
    for photo_id in KITTENS:
        media.append(InputMediaPhoto(photo_id))
    await bot.send_media_group(message.from_user.id, media)


@dp.message_handler(commands=['audio'])
async def audio_send(message: Message):
    await bot.send_audio(message.from_user.id, 'BAACAgIAAxkDAAIBfWLReB-qNcQjXlzraLUDmsgZGjZEAAKAHAACifWQSlPQUIZKMnARKQQ')


@dp.message_handler(commands=['file'])
async def process_file_command(message: Message):
    user_id = message.from_user.id
    with open('Data/angel_respawn_meloboom.mp3', 'rb') as TEXT_FILE:
        await bot.send_document(user_id, TEXT_FILE,
                                caption='Этот файл специально для тебя!')


@dp.message_handler(commands=['test_kb'])
async def process_start_command(message: Message):
    await message.reply("Привет!", reply_markup=kb1)


@dp.message_handler(text='Посмотреть котика')
async def show_kitty(message: Message):
    user_id = message.from_user.id

    URL = 'https://cataas.com/cat/says/hello%20world!'
    r = requests.get(URL)

    await bot.send_photo(user_id, r.content,
                         caption='Этот котик специально для вас!')


@dp.message_handler(commands=['register'], state=None)
async def register_user(message: Message):
    await FSMRegister.username.set()
    await message.reply("Введите имя пользователя")


@dp.message_handler(state=FSMRegister.username)
async def load_username(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await FSMRegister.next()
    await message.reply('Введите email пользователя')


@dp.message_handler(state=FSMRegister.email)
async def load_email(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    user_data = dict(data)
    if await UserCRUD.user_exists(user_data.get('email')):
        await message.reply('Пользователь уже зарегистрирован')
        await state.finish()
    else:
        await UserCRUD.add_user(username=user_data.get('username'),
                                email=user_data.get('email'))
        await message.reply('Спасибо за регистрацию!!')
        await state.finish()



