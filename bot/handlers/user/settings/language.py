from aiogram import Router, F, types

from bot.db.methods.fetch import fetch
from bot.db.methods.update import update
from bot.misc.get_translation import get_translation

router = Router()


@router.callback_query(F.data == "russian")
async def set_russian_language(callback: types.CallbackQuery) -> None:
    """method that sets the Russian language for a user in the database"""

    update(message=callback.message, language="ru")

    # query to get user language from database
    fetch_language_query = """SELECT language FROM users WHERE chat_id = ?"""
    language = fetch(fetch_language_query, (callback.message.chat.id,))[0][0]

    _ = get_translation(language)  # alias for the function

    await callback.answer(_("ready"))


@router.callback_query(F.data == "english")
async def set_english_language(callback: types.CallbackQuery) -> None:
    """method that sets the English language for a user in the database"""

    update(message=callback.message, language="en")

    # query to get user language from database
    fetch_language_query = """SELECT language FROM users WHERE chat_id = ?"""
    language = fetch(fetch_language_query, (callback.message.chat.id,))[0][0]

    _ = get_translation(language)  # alias for the function

    await callback.answer(_("ready"))
