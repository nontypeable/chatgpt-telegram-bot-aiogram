from aiogram import Dispatcher

from bot.handlers.user.ai.gpt_request import router as gpt_request_router
from bot.handlers.user.menu.information import router as information_router
from bot.handlers.user.menu.menu import router as menu_router
from bot.handlers.user.menu.settings import router as settings_router
from bot.handlers.user.settings.gpt_model import router as gpt_model_router
from bot.handlers.user.settings.language import router as language_settings_router
from bot.handlers.user.start import router as start_router


def register_all_user_handlers(dp: Dispatcher) -> None:
    """method that registers all user handlers"""

    dp.include_router(start_router)
    dp.include_router(language_settings_router)
    dp.include_router(menu_router)
    dp.include_router(information_router)
    dp.include_router(settings_router)
    dp.include_router(gpt_model_router)
    dp.include_router(gpt_request_router)
