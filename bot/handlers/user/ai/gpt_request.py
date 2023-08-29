from aiogram import Router, F, Bot, types

from bot.db.methods.fetch import fetch
from bot.misc.get_translation import get_translation
from bot.misc.gpt_request import gpt_request

router = Router()


@router.message(F.text)
async def request(message: types.Message, bot: Bot) -> None:
    """method that handle user messages by sending them to GPT"""

    chat_id = message.chat.id

    # query to get user language from database
    fetch_language_query = "SELECT language FROM users WHERE chat_id = ?"
    language = fetch(fetch_language_query, (chat_id,))[0][0]

    _ = get_translation(language)  # alias for the function

    msg = await message.answer(text=_("request has been sent"))
    text = await gpt_request(message=message)

    await message.answer(text=text)

    await bot.delete_message(chat_id=chat_id, message_id=msg.message_id)
