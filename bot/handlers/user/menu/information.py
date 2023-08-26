from aiogram import Router, types, Bot, F
from aiogram.filters import Command

from bot.misc.show_information import show_information

router = Router()


@router.message(Command("info"))
async def information(message: types.Message, bot: Bot) -> None:
    """a method that sends information to the user on command"""

    await show_information(bot=bot, data=message)


@router.callback_query(F.data == "information")
async def information(callback: types.CallbackQuery, bot: Bot) -> None:
    """method that sends information to the user on clicking on an inline button"""

    await show_information(bot=bot, data=callback)
