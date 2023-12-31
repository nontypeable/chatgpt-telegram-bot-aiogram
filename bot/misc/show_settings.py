from typing import Union

from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.db.methods.fetch import fetch
from bot.keyboards.inline.menu.settings import settings_keyboard
from bot.misc.get_translation import get_translation


async def show_settings(bot: Bot, data: Union[types.CallbackQuery, types.Message]):
    """method that shows settings"""

    try:
        if isinstance(data, types.CallbackQuery):
            chat_id = data.from_user.id
            message_id = data.message.message_id
        elif isinstance(data, types.Message):
            chat_id = data.from_user.id

        # query to get user language from database
        fetch_language_query = """SELECT language FROM users WHERE chat_id = ?"""
        language = fetch(fetch_language_query, (chat_id,))[0][0]

        _ = get_translation(language)  # alias for the function

        if isinstance(data, types.CallbackQuery):
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=_("settings text"),
                                        reply_markup=settings_keyboard(chat_id, data))
        elif isinstance(data, types.Message):
            await data.answer(_("settings text"), reply_markup=settings_keyboard(chat_id, data))

    except Exception as e:
        print(f"An error has occurred: {e}")
