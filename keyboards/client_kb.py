from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #,ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('/Оставить номер для отправки купонов', request_contact=True)
b5 = KeyboardButton('/Оставить геоданные для розыгрыша', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)  #, one_time_keyboard=True/False) ## Разицы нет

# kb_client.add(b1).insert(b2).add(b3)
kb_client.row(b1, b2).add(b3).row(b4, b5)
# kb_client.row(b1, b2, b3)
