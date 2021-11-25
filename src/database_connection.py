import os
import sqlite3


connection = sqlite3.connect(os.getenv('DATABASE'))
connection.row_factory = sqlite3.Row


def get_connection():
    return connection
