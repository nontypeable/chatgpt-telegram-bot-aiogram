from aiogram import Bot, Router, types
from aiogram.filters import Command

from bot.misc.show_menu import show_menu

router = Router()


@router.message(Command("menu"))
async def menu(message: types.Message, bot: Bot) -> None:
    """method that sends the bot menu to the user on command"""

    await show_menu(bot=bot, data=message)
