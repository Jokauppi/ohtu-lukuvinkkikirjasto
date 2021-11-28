import os
import sqlite3
import config

def get_connection(db_file=os.getenv('DATABASE')):

    print(db_file)
    connection = sqlite3.connect(db_file)
    connection.row_factory = sqlite3.Row

    return connection
