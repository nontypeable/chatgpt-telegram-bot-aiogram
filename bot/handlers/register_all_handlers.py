from aiogram import Dispatcher

from bot.handlers.user.register_all_user_handlers import register_all_user_handlers
from bot.handlers.admin.register_all_admin_handlers import register_all_admin_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    """method that registers admin and user handlers"""

    handlers = (
        register_all_user_handlers,
        register_all_admin_handlers
    )

    for handler in handlers:
        handler(dp)
