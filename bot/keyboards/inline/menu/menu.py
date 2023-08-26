from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton
from bot.db.methods.fetch import fetch
from bot.misc.get_translation import get_translation


def menu_keyboard(chat_id: int) -> InlineKeyboardMarkup:
    """method that returns the keyboard layout for the bot's menu"""

    keyboard = InlineKeyboardBuilder()

    # query to get user language from database
    fetch_language_query = """SELECT language FROM users WHERE chat_id = ?"""
    language = fetch(fetch_language_query, (chat_id,))[0][0]

    _ = get_translation(language)  # alias for the function

    keyboard.row(
        InlineKeyboardButton(
            text=_("information"),
            callback_data="information"
        )
    )

    keyboard.row(
        InlineKeyboardButton(
            text=_("settings"),
            callback_data="settings"
        )
    )

    return keyboard.as_markup()
