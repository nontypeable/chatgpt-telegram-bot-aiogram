import os
import sqlite3
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, types


class CheckUserIsAdministratorMiddleware(BaseMiddleware):
    """middleware to check if a user is an administrator"""

    async def __call__(self, handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]], event: types.Message,
                       data: Dict[str, Any]) -> Any:
        # defining the absolute path to the database
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "database.db")

        try:
            # creating a database connection
            with sqlite3.connect(db_path) as connection:
                cursor = connection.cursor()

                # query to update the date and time of the last time the bot was used
                fetch_user_admin_status_query = """SELECT is_admin FROM users WHERE chat_id = ?"""
                cursor.execute(fetch_user_admin_status_query, (event.chat.id,))

                if cursor.fetchone()[0] == 1:
                    return await handler(event, data)

        except sqlite3.Error as e:
            print(f"An SQLite3 error has occurred: {e}")
        except Exception as e:
            print(f"An error has occurred: {e}")
