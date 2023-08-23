from aiogram import Router, types
from aiogram.filters import Command

from bot.keyboards.other import start_language_setup_keyboard
from bot.db.methods.add_user import add_user

router = Router()


@router.message(Command("start"))
async def start(message: types.Message) -> None:
    """method that sends a message with keyboard markup to select the language of the bot"""

    add_user(message=message)

    await message.answer("Выберите язык / Choose language:", reply_markup=start_language_setup_keyboard())

