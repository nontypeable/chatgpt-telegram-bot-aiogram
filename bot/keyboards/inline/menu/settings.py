from typing import Union

from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton

from bot.db.methods.fetch import fetch
from bot.misc.get_translation import get_translation


def settings_keyboard(chat_id: int, data: Union[types.CallbackQuery, types.Message]) -> InlineKeyboardMarkup:
    """method that returns the keyboard layout for the bot settings"""

    keyboard = InlineKeyboardBuilder()

    # query to get user language from database
    fetch_language_query = """SELECT language FROM users WHERE chat_id = ?"""
    language = fetch(fetch_language_query, (chat_id,))[0][0]

    _ = get_translation(language)  # alias for the function

    keyboard.row(
        InlineKeyboardButton(
            text=_("language"),
            callback_data="language"
        )
    )

    keyboard.row(
        InlineKeyboardButton(
            text=_("gpt model"),
            callback_data="gpt_model"
        )
    )

    if isinstance(data, types.CallbackQuery):
        keyboard.row(
            InlineKeyboardButton(
                text=_("back to menu"),
                callback_data="menu"
            )
        )

    return keyboard.as_markup()
