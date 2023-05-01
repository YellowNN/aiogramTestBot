from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в онлайн')


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.reply('Здаров')


@dp.message_handler(commands=['команда'])
async def echo(message: types.Message):
    await message.reply(message.text)


@dp.message_handler(lambda message: 'такси' in message.text.lower())
async def taxi(message: types.Message):
    await message.reply('таксист в пути')


@dp.message_handler(lambda message: 'нло' in message.text.lower())
async def taxi(message: types.Message):
    await message.reply('нло над вашим домом')


@dp.message_handler()
async def empty(message: types.Message):
    await message.reply('Нет такой команды')
    await message.delete()


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
