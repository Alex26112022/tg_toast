from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
import app.keyboards as kb
from app.database.select_db import SelectDb

new_select = SelectDb()

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.reply(text='Выберите тему!',
                        reply_markup=await kb.reply_themes())


@router.message(F.text)
async def get_toast(message: Message):
    if message.text in kb.themes:
        toast = await new_select.select_random_toast(
            kb.themes.get(message.text))
        print(
            f'{message.from_user.id} | {message.from_user.first_name} | {message.text} -> {toast.content}')
        await message.reply(toast.content)
    else:
        await message.reply("Такой темы нет в меню!")
