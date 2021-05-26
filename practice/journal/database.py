import sqlite3

connection = sqlite3.connect("data.db")


def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )


def add_entry(content, date):
    with connection:
        connection.execute(
            f"INSERT INTO entries(content, date) VALUES(?,?)", (content, date)
        )


def get_entries():
    return entries
