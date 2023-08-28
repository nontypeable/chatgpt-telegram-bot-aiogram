from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder

from bot.db.methods.fetch import fetch
from bot.misc.get_translation import get_translation

# bot languages
LANGUAGES = {
    "ru": "Русский 🇷🇺",
    "en": "English 🇺🇸"
}


def language_keyboard(chat_id: int) -> InlineKeyboardMarkup:
    """Method that returns the keyboard layout for setting the bot's language"""

    keyboard = InlineKeyboardBuilder()

    # Query to get user language from database
    fetch_language_query = """SELECT language FROM users WHERE chat_id = ?"""
    language = fetch(fetch_language_query, (chat_id,))[0][0]

    _ = get_translation(language)  # alias for the function

    for lang in LANGUAGES:
        text = f"{LANGUAGES[lang]} ✅" if lang == language else LANGUAGES[lang]
        keyboard.row(
            InlineKeyboardButton(
                text=text,
                callback_data=lang
            )
        )

    keyboard.row(
        InlineKeyboardButton(
            text=_("back to settings"),
            callback_data="settings"
        )
    )

    return keyboard.as_markup()
