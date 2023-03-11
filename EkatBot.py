import logging
import openai
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import Parsing_site
import Parser_movies
import CHB_parsing
import Chel_cinema
import json
import string


"""Telegram bot token"""
API_TOKEN = '5891307674:AAGPQ7xonAQjiafm_ADUGNIjKSJs-a55Pxg'

"""OpenAI token"""
OPENAI_TOKEN = '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'
openai.api_key = OPENAI_TOKEN
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

inkb = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text = 'Все события', callback_data='Все события'),\
                                             InlineKeyboardButton(text = 'Кино', callback_data='Кино'),\
                                             InlineKeyboardButton(text = 'Случайный фильм', callback_data='Случайный фильм'),\
                                             InlineKeyboardButton(text = 'События в Челябинске', callback_data='События в Челябинске'),\
                                             InlineKeyboardButton(text = 'Кино в Челябинске', callback_data='Кино в Челябинске'))


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1, b2).row(b3, b4).row(b5, b6)


"""Create a start handler"""
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi! I'm Event'sBot\nDon't know where to go tonight?. I can also answer for your question, please ask me...")
    await message.answer('Выберите действие:', reply_markup=inkb)


"""Create handler for Chat_GPT"""
@dp.message_handler()
async def gpt_answer(message: types.Message):
    prompt = message.text
    model_engine = 'text-davinci-003'
    max_tokens = 1024
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    await message.answer('ChatGPT: Генерирую ответ...')
    await message.answer('ChatGPT: '+completion.choices[0].text)




"""Create a handlers for inline buttons"""
@dp.callback_query_handler(text='Все события')
async def send_inkb_all_events(callback: types.CallbackQuery):
    await callback.message.answer(f'Here the results:\n {Parsing_site.string_out}')
    await callback.message.answer('Выберите действие:', reply_markup=inkb)

@dp.callback_query_handler(text='Кино')
async def send_inkb_all_films(callback: types.CallbackQuery):
    await callback.message.answer(f'Here the results:\n {Parser_movies.string_out}')
    await callback.message.answer('Выберите действие:', reply_markup=inkb)

@dp.callback_query_handler(text='Случайный фильм')
async def send_inkb_all_films(callback: types.CallbackQuery):
    await callback.message.answer(f'Here the results:\n {random.choice(Parser_movies.out_cinema)}')
    await callback.message.answer('Выберите действие:', reply_markup=inkb)

@dp.callback_query_handler(text='Случайное событие')
async def send_inkb_all_films(callback: types.CallbackQuery):
    await callback.message.answer(f'Here the results:\n {random.choice(Parsing_site.out)}')
    await callback.message.answer('Выберите действие:', reply_markup=inkb)

@dp.callback_query_handler(text='События в Челябинске')
async def send_inkb_all_films(callback: types.CallbackQuery):
    await callback.message.answer(f'Here the results:\n {CHB_parsing.string_out}')
    await callback.message.answer('Выберите действие:', reply_markup=inkb)

@dp.callback_query_handler(text='Кино в Челябинске')
async def send_inkb_all_films(callback: types.CallbackQuery):
    await callback.message.answer(f'Here the results:\n {Chel_cinema.string_out}')
    await callback.message.answer('Выберите действие:', reply_markup=inkb)



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


@dp.message_handler()
async def empty(message: types.Message):
    await message.answer('Нет такой команды')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
