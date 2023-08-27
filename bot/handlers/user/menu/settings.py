from aiogram import Bot, Router, F, types
from aiogram.filters import Command

from bot.misc.show_settings import show_settings

router = Router()


@router.message(Command("settings"))
async def settings(message: types.Message, bot: Bot):
    """a method that sends the bot settings to the user on command"""

    await show_settings(data=message, bot=bot)


@router.callback_query(F.data == "settings")
async def settings(callback: types.CallbackQuery, bot: Bot):
    """method that sends the bot settings to the user on clicking on an inline button"""

    await show_settings(data=callback, bot=bot)
