from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN, ADMIN_ID

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


async def send_to_admin(dp):
    await bot.send_message(chat_id=ADMIN_ID, text='Bot RUNS! \n /help')

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_startup=send_to_admin)


