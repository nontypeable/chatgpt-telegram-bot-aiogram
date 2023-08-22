import os

from aiogram.enums import ParseMode
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from bot.handlers.register_all_handlers import register_all_handlers

# defining the absolute path to the environment file
env_path = os.path.join(os.path.dirname(__file__), "env.env")

load_dotenv(env_path)  # loading environment file


async def start() -> None:
    """method that starts the bot"""
    bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"), parse_mode=ParseMode.MARKDOWN)
    dp = Dispatcher()

    register_all_handlers(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)