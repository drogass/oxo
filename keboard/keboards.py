from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Отправить фото пиццы')
    button_2 = KeyboardButton('Перейти на следующую клавиатуру')
    button_5 = KeyboardButton('Отправить фото суши')
    keyboard.add(button_1, button_2, button_5)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_3 = KeyboardButton('Отправить фото бургера')
    button_4 = KeyboardButton('Перейти назад')
    keyboard_2.add(button_3, button_4)
    return keyboard_2
