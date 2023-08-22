import sqlite3
import os

from aiogram import types


def update(message: types.Message, gpt_model: str | None = None, language: str | None = None) -> None:
    """a method that updates the bot settings information for the user in the database"""

    # defining the absolute path to the database
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database.db")

    try:
        # creating a database connection
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()

            if gpt_model:
                # query to update gpt_model in database
                update_gpt_model_query = """UPDATE users SET gpt_model = ? WHERE chat_id = ?"""

                cursor.execute(update_gpt_model_query, (gpt_model, message.chat.id,))

            if language:
                # query to update language in database
                update_language_query = """UPDATE users SET language = ? WHERE chat_id = ?"""

                cursor.execute(update_language_query, (language, message.chat.id,))

    except sqlite3.Error as e:
        print(f"An SQLite3 error has occurred: {e}")
    except Exception as e:
        print(f"An error has occurred: {e}")
