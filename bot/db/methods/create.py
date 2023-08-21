import sqlite3
import os


def create_table() -> None:
    """method that creates a table in the database"""

    # defining the absolute path to the database
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database.db")

    try:
        # creating a database connection
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()

            # query to create table in database
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER,
                username TEXT,
                gpt_model TEXT,
                language TEXT
            )
            """

            cursor.execute(create_table_query)

    except sqlite3.Error as e:
        print(f"An SQLite3 error has occurred: {e}")
    except Exception as e:
        print(f"An error has occurred: {e}")
