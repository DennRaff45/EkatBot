import logging
from aiogram import Bot, Dispatcher, executor, types
import Parsing_site
import json
import string


API_TOKEN = '5891307674:AAGPQ7xonAQjiafm_ADUGNIjKSJs-a55Pxg'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi! I'm EkatBot\nDon't know where to go tonight?.")

"""Create a parser, which returns a list with events"""
@dp.message_handler(commands=['show'])
async def send_result(message: types.Message):
    await message.answer(f'Here the results:\n {Parsing_site.string_out}')


"""Create a checker for bad words"""
@dp.message_handler()
async def bad_words_cheker(message: types.Message):
    if {i.lower().translate(str.maketrans('','', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)