import pyodbc


def select_all_entries_from_column(table_name, cursor, column_name):
    """Select all entries from a column.
    Args:
        table_name (str): Table name.
        cursor (object): pyobdc cursor.
        column_name (str): Column name.
    Returns:
        data (list): List with the selected entries.
    Example (non executable):
        $ conn = pyodbc.connect(connection_string)
        $ cur = conn.cursor()
        4 data = select_all_entries_from_column(tab_name, cur, col_name)

    """
    query = "SELECT " + column_name + " FROM " + table_name
    cursor.execute(query)
    data = cursor.fetchall()
    data = [d[0] for d in data]
    return data


def select_entry_where_column_equals_value(table_name, cursor, column_name, value):
    """Select one entry where the a column has a specific value.
    Args:
        table_name (str): Table name.
        cursor (object): pyobdc cursor.
        column_name (str): Column name.
        value (str or integer): Value to query.
    Returns:
        data (list): List of entries for the queried conditions.
    Examples (non executable):
        $ conn = pyodbc.connect(connection_string)
        $ cur = conn.cursor()
        $ data = select_entry_where_column_equals_value(tab_name, cur, col_name, 1)

    """
    query = "SELECT * FROM " + table_name + " WHERE " + column_name + " = ?"
    cursor.execute(query, value)
    data = cursor.fetchone()
    return data

