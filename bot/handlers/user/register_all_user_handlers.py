from aiogram import Dispatcher

from bot.handlers.user.start import router as start_router
from bot.handlers.user.settings.language import router as language_settings_router


def register_all_user_handlers(dp: Dispatcher) -> None:
    """method that registers all user handlers"""

    dp.include_router(start_router)
    dp.include_router(language_settings_router)
