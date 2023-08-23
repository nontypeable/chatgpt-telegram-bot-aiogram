from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton


def start_language_setup_keyboard() -> InlineKeyboardMarkup:
    """method that returns the keyboard markup for selecting the language of the bot at startup time"""

    keyboard = InlineKeyboardBuilder()

    keyboard.row(
        InlineKeyboardButton(
            text="🇷🇺 Русский",
            callback_data="russian"
        )
    )

    keyboard.row(
        InlineKeyboardButton(
            text="🇺🇸 English",
            callback_data="english"
        )
    )

    return keyboard.as_markup()
