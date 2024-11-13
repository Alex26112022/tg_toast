from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

themes = {
    'Короткие': 1,
    'Смешные': 2,
    'На ДР': 3,
    'На юбилей': 4,
    'Свадебные': 5,
    'За родителей': 6,
    'За женщин': 7,
    'Про любовь': 8,
    'Кавказские': 9,
    'Притчи': 10,
}


async def reply_themes():
    keyboard = ReplyKeyboardBuilder()
    for theme in themes:
        keyboard.add(KeyboardButton(text=theme))
    return keyboard.adjust(3).as_markup()
