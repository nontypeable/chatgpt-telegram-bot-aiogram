from typing import Union

from aiogram import Bot, types

from bot.db.methods.fetch import fetch
from bot.keyboards.inline.settings.language import language_keyboard
from bot.misc.get_translation import get_translation


async def show_language_settings(bot: Bot, data: Union[types.CallbackQuery, types.Message]):
    """method that shows language settings"""

    try:
        if isinstance(data, types.CallbackQuery):
            chat_id = data.from_user.id
            message_id = data.message.message_id
        if isinstance(data, types.Message):
            chat_id = data.from_user.id

        # query to get user language from database
        fetch_language_query = "SELECT language FROM users WHERE chat_id = ?"
        language = fetch(fetch_language_query, (chat_id,))[0][0]

        _ = get_translation(language)  # alias for the function

        if isinstance(data, types.CallbackQuery):
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=_("language settings text"), reply_markup=language_keyboard(chat_id))
        elif isinstance(data, types.Message):
            await data.answer(text=_("language settings text"), reply_markup=language_keyboard(chat_id))

    except Exception as e:
        print(f"An error has occurred: {e}")
