import asyncio
import databases
from DB_FICH import db_conn
from Bot2 import dp, bot
from write_func import write_to_file
from aiogram.types import Message, InputMediaVideo, InputMediaPhoto, ChatActions
from models import *
from keyboard import *
DB_INFO = 'postgresql://postgres:qseawdzxc1@localhost:5432/Psyc_lesson_1'

database = databases.Database(DB_INFO)


PHOTO = 'https://vk.com/club47724318'
KITTENS = [
    'https://www.championat.com/cybersport/news-4575511-tesla-otlozhila-sozdanie-mashiny-buduschego-cybertruck-azh-do-2023-goda.html',
    'https://www.autonews.ru/news/621e39399a794715dc9153dc',
]


@dp.message_handler(commands=['help'])
async def help_message(message: Message):
    msg = 'Я могу ответить на следующие команды: \n /audio /photo, /group, ' \
          '/note, /file,\n /video, /text, /test_kb,\n /test_kb1, /test_inkb'
    await message.reply('Хелп !!!' + msg)


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


'''@dp.message_handler(commands=['note'])
async def process_note_command(message: Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO_NOTE)
    await asyncio.sleep(1)  # конвертируем видео и отправляем его пользователю
    await bot.send_video_note(message.from_user.id, VIDEO_NOTE)'''


@dp.message_handler(commands=['file'])
async def process_file_command(message: Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
    await asyncio.sleep(1)  # скачиваем файл и отправляем его пользователю
    with open('Data/angel_respawn_meloboom.mp3', 'rb') as TEXT_FILE:
        await bot.send_document(user_id, TEXT_FILE,
                                caption='Этот файл специально для тебя!')


# @dp.message_handler(commands=['files'])
# async def get_all_files(message: Message):
#     user_id = message.from_user.id
#     files = await


@dp.message_handler(commands=['text'])
async def get_text(message: Message):
    file = await db_conn(3)
    user_id = message.from_user.id
    with open(file, 'rb') as f:
        await bot.send_document(user_id, f)


@dp.message_handler(commands=['test_kb'])
async def process_start_command(message: Message):
    await message.reply("Привет!", reply_markup=greet_kb)


@dp.message_handler(commands=['test_kb1'])
async def process_start_command(message: Message):
    await message.reply("Привет!", reply_markup=greet_kb1)


@dp.message_handler(commands=['test_inkb'])
async def process_start_command(message: Message):
    await message.reply("Привет!", reply_markup=inline_kb1)




@dp.message_handler()
async def echo(message: Message):
    text = f'Привет, ты написал {message.text}'
    await bot.send_message(message.from_user.id, text=text)
    await message.answer(text=text)
    write_to_file(message.text)





