from aiogram import Router, F, types, Bot

from bot.db.methods.fetch import fetch
from bot.db.methods.update import update
from bot.misc.get_translation import get_translation
from bot.misc.show_language_settings import show_language_settings
from bot.misc.show_menu import show_menu

router = Router()


@router.callback_query(F.data == "language")
async def language_settings(callback: types.CallbackQuery, bot: Bot):
    """method that shows the language settings of the bot by clicking on the inline button"""

    await show_language_settings(bot=bot, data=callback)


@router.callback_query(F.data == "ru")
async def set_russian_language(callback: types.CallbackQuery, bot: Bot) -> None:
    """method that sets the Russian language for a user in the database"""

    update(message=callback.message, language="ru")

    # query to get user language from database
    fetch_language_query = """SELECT language FROM users WHERE chat_id = ?"""
    language = fetch(fetch_language_query, (callback.message.chat.id,))[0][0]

    _ = get_translation(language)  # alias for the function

    await show_menu(bot=bot, data=callback)

    await callback.answer(_("ready"))


@router.callback_query(F.data == "en")
async def set_english_language(callback: types.CallbackQuery, bot: Bot) -> None:
    """method that sets the English language for a user in the database"""

    update(message=callback.message, language="en")

    # query to get user language from database
    fetch_language_query = """SELECT language FROM users WHERE chat_id = ?"""
    language = fetch(fetch_language_query, (callback.message.chat.id,))[0][0]

    _ = get_translation(language)  # alias for the function

    await show_menu(bot=bot, data=callback)

    await callback.answer(_("ready"))
