from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from config import TOKEN

import db_reader as db_r
import keyboard as kb
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!!!\nЭтот бот помогает подготовиться к ЕГЭ\nВведи /help чтобы познакомиться с возможностями")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Введи:\n/informatics и выбери задания по информатике")

@dp.message_handler(commands=['informatics'])
async def process_command_subjects(message: types.Message):
    await message.reply("Выберите задание", reply_markup=kb.inline_kb_tasks)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('tsk'))
async def process_callback_informatics(callback_query: types.CallbackQuery):
    code = callback_query.data[-2]+callback_query.data[-1]
    print(code)
    if code.isdigit():
        code = int(code)
    print(code)
    if code == 1:
        await bot.answer_callback_query(callback_query.id, text='Первое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(1))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(2))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(3))

    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='Второе задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(4))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(5))

    if code == 3:
        await bot.answer_callback_query(callback_query.id, text='Третье задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(6))

    if code == 4:
        await bot.answer_callback_query(callback_query.id, text='Четвертое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(7))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(8))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(9))

    if code == 5:
        await bot.answer_callback_query(callback_query.id, text='Пятое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(10))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(11))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(12))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(13))

    if code == 6:
        await bot.answer_callback_query(callback_query.id, text='Шестое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(14))

    if code == 7:
        await bot.answer_callback_query(callback_query.id, text='Седьмое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(15))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(16))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(17))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(18))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(19))

    if code == 8:
        await bot.answer_callback_query(callback_query.id, text='Восьмое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(20))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(21))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(22))

    if code == 9:
            await bot.answer_callback_query(callback_query.id, text='Девятое задание')
            await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(23))

    if code == 10:
        await bot.answer_callback_query(callback_query.id, text='Десятое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(24))

    if code == 11:
        await bot.answer_callback_query(callback_query.id, text='Одинадцатое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(25))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(26))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(27))

    if code == 12:
        await bot.answer_callback_query(callback_query.id, text='Двенадцатое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(28))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(29))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(30))

    if code == 13:
        await bot.answer_callback_query(callback_query.id, text='Тренадцатое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(31))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(32))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(33))

    if code == 14:
        await bot.answer_callback_query(callback_query.id, text='Четырнадцатое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(34))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(35))

    if code == 15:
        await bot.answer_callback_query(callback_query.id, text='Пятнадцатое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(36))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(37))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(38))

    if code == 16:
        await bot.answer_callback_query(callback_query.id, text='Шестнадцатое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(39))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(40))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(41))

    if code == 17:
        await bot.answer_callback_query(callback_query.id, text='Семнадцатое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(42))

    if code == 18:
        await bot.answer_callback_query(callback_query.id, text='Восемнадцатое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(44))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(45))

    if (code == 19) or (code == 20) or (code == 21):
        await bot.answer_callback_query(callback_query.id, text='Девятнадцатое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(46))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(47))

    if code == 22:
        await bot.answer_callback_query(callback_query.id, text='Двадцать второе задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(48))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(49))

    if code == 23:
        await bot.answer_callback_query(callback_query.id, text='Двадцать третье задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(50))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(51))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(52))

    if code == 24:
        await bot.answer_callback_query(callback_query.id, text='Двадцать четвертое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(53))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(54))

    if code == 25:
        await bot.answer_callback_query(callback_query.id, text='Двадцать пятое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(55))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(56))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(57))

    if code == 26:
        await bot.answer_callback_query(callback_query.id, text='Двадцать шестое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(58))

    if code == 27:
        await bot.answer_callback_query(callback_query.id, text='Двадцать седьмое задание')
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(59))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(60))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(61))
        await bot.send_photo(callback_query.from_user.id, db_r.read_blob_data(62))
    await bot.send_message(callback_query.from_user.id, text="Это все что у меня есть")
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)