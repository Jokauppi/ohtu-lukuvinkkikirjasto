import os
import sqlite3

def get_connection(db_file=os.getenv('DATABASE')):

    connection = sqlite3.connect(db_file)
    connection.row_factory = sqlite3.Row

    return connection
