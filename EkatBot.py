import logging
import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import Parsing_site
import json
import string

API_TOKEN = '5891307674:AAGPQ7xonAQjiafm_ADUGNIjKSJs-a55Pxg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

"""Create keyboard buttons"""

b1 = KeyboardButton('/Случайное_событие')
b2 = KeyboardButton('/Все_события')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi! I'm EkatBot\nDon't know where to go tonight?.", reply_markup=kb_client)


"""Create a handler, which returns a list with all events"""

@dp.message_handler(commands=['Все_события'])
async def send_all_events(message: types.Message):
    await message.answer(f'Here the results:\n {Parsing_site.string_out}', reply_markup=ReplyKeyboardRemove())

"""Create handler, which returns the one random event"""
@dp.message_handler(commands=['Случайное_событие'])
async def send_random_event(message: types.Message):
    await message.answer(f'Here the results:\n {random.choice(Parsing_site.out)}')


"""Create a checker for bad words"""

@dp.message_handler()
async def bad_words_cheker(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
