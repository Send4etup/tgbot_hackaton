from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')],
    [KeyboardButton(text='Поддержка')],
],      resize_keyboard=True,
        input_field_placeholder='Выберите что-то одно, пж',
        one_time_keyboard=True)

settings = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Ну это ютубчик твой любимый, да, зависимый?', url='https://youtube.com')]
    ])

cars = ['Koenigsegg', 'Pagain', 'Mclaren', 'Ferrari', 'Lamborghini']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://youtube.com'))
    return keyboard.adjust(1).as_markup()