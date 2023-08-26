import os
import sqlite3
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram import types

from bot.db.methods.fetch import fetch


class UsernameCheckMiddleware(BaseMiddleware):
    """middleware to check the correctness of the username in the database"""

    async def __call__(self, handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]], event: types.Message,
                       data: Dict[str, Any]) -> Any:
        # defining the absolute path to the database
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "database.db")

        try:
            # creating a database connection
            with sqlite3.connect(db_path) as connection:
                cursor = connection.cursor()

                # query to get the username of the user from the database
                fetch_username_query = """SELECT username FROM users WHERE chat_id = ?"""
                username_in_db = fetch(fetch_username_query, (event.chat.id,))[0][0]

                if username_in_db is not event.from_user.username:
                    # query to update the username of the user in the database
                    update_username_query = """UPDATE users SET username = ? WHERE chat_id = ?;"""
                    cursor.execute(update_username_query, (event.from_user.username, event.chat.id,))

        except sqlite3.Error as e:
            print(f"An SQLite3 error has occurred: {e}")
        except Exception as e:
            print(f"An error has occurred: {e}")

        return await handler(event, data)
