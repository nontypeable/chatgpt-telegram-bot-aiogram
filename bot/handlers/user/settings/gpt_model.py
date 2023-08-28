from aiogram import Router, F, types, Bot

from bot.db.methods.fetch import fetch
from bot.db.methods.update import update
from bot.misc.get_translation import get_translation
from bot.misc.show_gpt_model_settings import show_gpt_model_settings

router = Router()


async def update_and_show_settings(callback: types.CallbackQuery, gpt_model: str, bot: Bot) -> None:
    """method that updates the gpt model in the database and shows the settings of the gpt model"""

    # query to get user language from database
    fetch_language_query = """SELECT language FROM users WHERE chat_id = ?"""
    language = fetch(fetch_language_query, (callback.message.chat.id,))[0][0]

    _ = get_translation(language)  # alias for the function

    update(callback.message, gpt_model=gpt_model)
    await show_gpt_model_settings(bot=bot, data=callback)

    await callback.answer(_("ready"))


@router.callback_query(F.data == "gpt_model")
async def show_gpt_models(callback: types.CallbackQuery, bot: Bot) -> None:
    """method that sends the gpt model settings to the user on clicking on an inline button"""

    await show_gpt_model_settings(bot=bot, data=callback)

    await callback.answer()


@router.callback_query(F.data == "gpt-4")
async def set_gpt_4(callback: types.CallbackQuery, bot: Bot) -> None:
    """method that changes model_gpt to gpt 4 in database"""

    await update_and_show_settings(callback=callback, gpt_model="gpt-4", bot=bot)


@router.callback_query(F.data == "gpt-3.5-turbo")
async def set_gpt_35_turbo(callback: types.CallbackQuery, bot: Bot) -> None:
    """method that changes model_gpt to gpt 3.5 turbo in database"""

    await update_and_show_settings(callback=callback, gpt_model="gpt-3.5-turbo", bot=bot)


@router.callback_query(F.data == "gpt-3.5-turbo-16k")
async def set_gpt_35_turbo_16k(callback: types.CallbackQuery, bot: Bot) -> None:
    """method that changes model_gpt to gpt 3.5 turbo 16k in database"""

    await update_and_show_settings(callback=callback, gpt_model="gpt-3.5-turbo-16k", bot=bot)
