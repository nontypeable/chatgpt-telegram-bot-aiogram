import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import setup_application, SimpleRequestHandler
from aiohttp import web
from dotenv import load_dotenv
from pyngrok import ngrok

from bot.handlers.register_all_handlers import register_all_handlers
from bot.middlewares.check_username_in_database import UsernameCheckMiddleware
from bot.middlewares.update_date_and_time_in_database import UpdateLastUsageTimeMiddleware

# defining the absolute path to the environment file
env_path = os.path.join(os.path.dirname(__file__), "env.env")

load_dotenv(env_path)  # loading environment file


async def on_startup(bot: Bot) -> None:
    ngrok.conf.get_default().config_path = ".config/ngrok.yml"
    ngrok.set_auth_token(os.getenv("NGROK_AUTHTOKEN"))

    tunnel = ngrok.connect(8081, "http").public_url

    print(f"Webhook set to: {tunnel}")

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(url=tunnel)


async def on_shutdown(bot: Bot) -> None:
    ngrok.kill()

    await bot.delete_webhook()
    await bot.session.close()


def start() -> None:
    dp = Dispatcher()
    bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"), parse_mode=ParseMode.HTML)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.message.middleware(UpdateLastUsageTimeMiddleware())
    dp.message.middleware(UsernameCheckMiddleware())

    register_all_handlers(dp)

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(dp, bot)

    webhook_requests_handler.register(app, path="")

    setup_application(app, dp, bot=bot)
    web.run_app(app=app, port=8081)
