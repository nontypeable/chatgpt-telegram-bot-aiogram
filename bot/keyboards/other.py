from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton

from bot.db.methods.fetch import fetch
from bot.misc.get_translation import get_translation


def start_language_setup_keyboard() -> InlineKeyboardMarkup:
    """method that returns the keyboard markup for selecting the language of the bot at startup time"""

    keyboard = InlineKeyboardBuilder()

    keyboard.row(
        InlineKeyboardButton(
            text="🇷🇺 Русский",
            callback_data="ru"
        )
    )

    keyboard.row(
        InlineKeyboardButton(
            text="🇺🇸 English",
            callback_data="en"
        )
    )

    return keyboard.as_markup()


def back_to_menu_keyboard(chat_id: int) -> InlineKeyboardMarkup:
    """a method that returns the keyboard layout that allows you to return back to the menu"""

    keyboard = InlineKeyboardBuilder()

    # query to get user language from database
    fetch_language_query = """SELECT language FROM users WHERE chat_id = ?"""
    language = fetch(fetch_language_query, (chat_id,))[0][0]

    _ = get_translation(language)  # alias for the function

    keyboard.row(
        InlineKeyboardButton(
            text=_("back to menu"),
            callback_data="menu"
        )
    )

    return keyboard.as_markup()
