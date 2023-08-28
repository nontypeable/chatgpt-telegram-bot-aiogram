from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton

from bot.db.methods.fetch import fetch
from bot.misc.get_translation import get_translation

# GPT model names
GPT_MODELS = [
    "gpt-4",
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k"
]


def gpt_model_keyboard(chat_id: int) -> InlineKeyboardMarkup:
    """method that returns the keyboard layout for setting the bot's GPT model"""

    keyboard = InlineKeyboardBuilder()

    # query to get user language from database
    fetch_language_query = """SELECT language FROM users WHERE chat_id = ?"""
    language = fetch(fetch_language_query, (chat_id,))[0][0]

    # query to get user gpt model from database
    fetch_gpt_model_query = """SELECT gpt_model FROM users WHERE chat_id = ?"""
    gpt_model = fetch(fetch_gpt_model_query, (chat_id,))[0][0]

    _ = get_translation(language)  # alias for the function

    for model in GPT_MODELS:
        text = f"{model} ✅" if model == gpt_model else model
        keyboard.row(
            InlineKeyboardButton(
                text=text,
                callback_data=model
            )
        )

    keyboard.row(
        InlineKeyboardButton(
            text=_("back to settings"),
            callback_data="settings"
        )
    )

    return keyboard.as_markup()
