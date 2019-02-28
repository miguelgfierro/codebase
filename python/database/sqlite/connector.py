import sqlite3
from sqlite3 import Error


def connect_to_database(database=None):
    """Connect to a sqlite database. Don't forget to close the connection at the
    end of the routine with `conn.close()`.
    
    Args:
        database (str): Database filename.
    
    Returns:
        object: Connector object.

    """
    if database is None:
        database = ":memory:"
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)
        raise
    return conn
