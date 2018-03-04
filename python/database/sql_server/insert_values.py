import pyodbc
import datetime


def insert_row(table_name, cursor, connector, value1, value2):
    """Insert a row of items in a table.
    Args:
        table_name (str): Table name.
        cursor (object): pyobdc cursor.
        connector (object): pyodbc connector.
        value1 (str or int): Value to insert.
        value2 (datetime.py): Value to insert.
    Example:
        >>> conn = pyodbc.connect(connection_string)
        >>> cur = conn.cursor()
        >>> insert_row(tab_name, cur, conn, "item1", datetime.datetime.now())

    """
    query = "INSERT INTO " + table_name + "( name, date ) VALUES (?,?)"
    cursor.execute(query, value1, value2)
    connector.commit()



