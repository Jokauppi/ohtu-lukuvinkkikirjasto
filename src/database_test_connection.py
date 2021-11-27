import os
import sqlite3
from database_connection import get_connection as connect

def get_connection(db_file):

    if os.path.exists(db_file):
        os.remove(db_file)
    
    connection = connect(db_file)
    
    return connection
