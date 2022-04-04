from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
import db_reader

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

#@dp.message_handler()
#async def echo_message(msg: types.Message):
 #   await bot.send_message(msg.from_user.id, msg.text)

@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id, db_reader.read_blob_data(2))

if __name__ == '__main__':
    executor.start_polling(dp)