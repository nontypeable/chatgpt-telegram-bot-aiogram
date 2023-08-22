import sqlite3
import os

from typing import Any, LiteralString, Iterable


def fetch(sql: LiteralString, params: Iterable[Any] | None = None) -> list[dict]:
    """method that fetch information from the database"""

    # defining the absolute path to the database
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database.db")

    try:
        # creating a database connection
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()

            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)

            result = cursor.fetchall()

            return result

    except sqlite3.Error as e:
        print(f"An SQLite3 error has occurred: {e}")
        return []
    except Exception as e:
        print(f"An error has occurred: {e}")
        return []

