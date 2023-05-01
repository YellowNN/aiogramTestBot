from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
ans = dict()

async def on_startup(_):
    # sqlite_db.sql_start()
    print('Бот вышел в онлайн')


# Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton1 = InlineKeyboardButton(text='Ссылка1', url='https://www.youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://www.google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='https://www.google.com'),
     InlineKeyboardButton(text='Ссылка4', url='https://www.google.com'),
     InlineKeyboardButton(text='Ссылка5', url='https://www.google.com')]
urlkb.add(urlButton1, urlButton2).row(*x)


@dp.message_handler(commands='ссылки')
async def ulr_command(message: types.Message):
    await message.answer('ссылочки:', reply_markup=urlkb)


inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
                                             InlineKeyboardButton(text='Not Like', callback_data='like_-1'))


@dp.message_handler(commands='test')
async def test_command(message: types.Message):
    await message.answer('Голосование:', reply_markup=inkb)


@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback: types.CallbackQuery):
#    await callback.answer('Нажата инлайн кнопка')  # Выводит гаснущее окно
###    await callback.message.answer('Нажата инлайн кнопка')  # Выводит сообщение
###    await callback.answer('Нажата инлайн кнопка')  # ЗАВЕРШАЕТ ОЖИДАНИЕ КОЛЛБЭКА + Выводит гаснущее окно
### await callback.answer('Нажата инлайн кнопка', show_alert=True)  # ЗАВЕРШАЕТ ОЖИДАНИЕ КОЛЛБЭКА + *Должен выводить НЕгаснущее окно
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in ans:
        ans[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
