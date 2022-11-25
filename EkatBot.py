import logging
from aiogram import Bot, Dispatcher, executor, types
import Parsing_site

API_TOKEN = '5891307674:AAGPQ7xonAQjiafm_ADUGNIjKSJs-a55Pxg'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi! I'm EkatBot\nDon't know where to go tonight?.")

@dp.message_handler(commands=['show'])
async def send_result(message: types.Message):
    await message.answer(f'Here the results:\n {Parsing_site.string_out}')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)