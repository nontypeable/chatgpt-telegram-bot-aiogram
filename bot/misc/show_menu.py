from typing import Union

from aiogram import Bot, types

from bot.db.methods.fetch import fetch
from bot.keyboards.inline.menu.menu import menu_keyboard
from bot.misc.get_translation import get_translation


async def show_menu(bot: Bot, data: Union[types.CallbackQuery, types.Message]) -> None:
    """method that shows the menu"""

    try:
        if isinstance(data, types.CallbackQuery):
            chat_id = data.from_user.id
            first_name = data.from_user.first_name
            message_id = data.message.message_id
        elif isinstance(data, types.Message):
            chat_id = data.from_user.id
            first_name = data.from_user.first_name

        # query to get user language from database
        fetch_language_query = "SELECT language FROM users WHERE chat_id = ?"
        language = fetch(fetch_language_query, (chat_id,))[0][0]

        _ = get_translation(language)  # alias for the function

        if isinstance(data, types.CallbackQuery):
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=_("hello, {first_name}").format(first_name=first_name),
                                        reply_markup=menu_keyboard(chat_id))
        elif isinstance(data, types.Message):
            await data.answer(text=_("hello, {first_name}").format(first_name=first_name),
                              reply_markup=menu_keyboard(chat_id))

    except Exception as e:
        print(f"An error has occurred: {e}")
