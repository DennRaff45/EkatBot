import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import Parsing_site
import Parser_movies
import CHB_parsing
import Chel_cinema
import json
import string

API_TOKEN = '5891307674:AAGPQ7xonAQjiafm_ADUGNIjKSJs-a55Pxg'

logging.basicConfig(level=logging.INFO)

"""Create Bot"""

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

"""Create keyboard buttons"""

b1 = KeyboardButton('/Случайное_событие')
b2 = KeyboardButton('/Все_события')
b3 = KeyboardButton('/Кино')
b4 = KeyboardButton('/Случайный_фильм')
b5 = KeyboardButton('/События_в_Челябинске')
b6 = KeyboardButton('/Кино_в_Челябинске')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1, b2).row(b3, b4).row(b5, b6)


"""Create a start handler"""
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi! I'm EkatBot\nDon't know where to go tonight?.", reply_markup=kb_client)


"""Create a handler, which returns a list with all events"""
@dp.message_handler(commands=['Все_события'])
async def send_all_events(message: types.Message):
    await message.answer(f'Here the results:\n {Parsing_site.string_out}') #reply_markup=ReplyKeyboardRemove())

"""Create handler, which returns the one random event"""
@dp.message_handler(commands=['Случайное_событие'])
async def send_random_event(message: types.Message):
    await message.answer(f'Here the results:\n {random.choice(Parsing_site.out)}')


"""Create handler, which returns all cinemas"""
@dp.message_handler(commands=['Кино'])
async def send_all_events(message: types.Message):
    await message.answer(f'Here the results:\n {Parser_movies.string_out}') #reply_markup=ReplyKeyboardRemove())

"""Create handler, which returns the all events in Chelyabinsk"""
@dp.message_handler(commands=['События_в_Челябинске'])
async def send_all_chb_events(message: types.Message):
    await message.answer(f'Here the results:\n {CHB_parsing.string_out}')

"""Create handler, which returns the all film in Chelyabinsk"""
@dp.message_handler(commands=['Кино_в_Челябинске'])
async def send_all_events(message: types.Message):
    await message.answer(f'Here the results:\n {Chel_cinema.string_out}')

"""Create handler, which returns the one random film"""
@dp.message_handler(commands=['Случайный_фильм'])
async def send_random_event(message: types.Message):
    await message.answer(f'Here the results:\n {random.choice(Parser_movies.out_cinema)}')


"""Create a checker for bad words"""
@dp.message_handler()
async def bad_words_cheker(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
