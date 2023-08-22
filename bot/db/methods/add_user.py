import sqlite3
import os

from aiogram import types

from bot.db.methods.fetch import fetch


def add_user(*, message: types.Message, gpt_model: str | None = "gpt-3.5-turbo", language: str | None = "ru") -> None:
    """method that adds information about the user to the database"""

    # defining the absolute path to the database
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database.db")

    # query to fetch user information from the database
    fetch_user_information_query = """SELECT * FROM users WHERE chat_id = ?"""

    if not fetch(fetch_user_information_query, (message.chat.id,)):
        try:
            with sqlite3.connect(db_path) as connection:
                cursor = connection.cursor()

                # query to insert user information into the database
                add_user_query = """INSERT INTO users (chat_id, username, gpt_model, language) VALUES (?, ?, ?, ?)"""

                cursor.execute(add_user_query, (message.chat.id, message.from_user.username, gpt_model, language))

        except sqlite3.Error as e:
            print(f"An SQLite3 error has occurred: {e}")
        except Exception as e:
            print(f"An error has occurred: {e}")
