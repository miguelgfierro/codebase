import pyodbc


def create_table(table_name, cursor):
    """Create a table and drop it if it exists.
    Args:
        table_name (str): Table name.
        cursor (object): pyobdc cursor.
    Example (non executable):
        $ conn = pyodbc.connect(connection_string)
        $ cur = conn.cursor()
        $ create_table(tab_name, cur)

    """
    query = (
        "IF OBJECT_ID('" + table_name + "') IS NOT NULL DROP TABLE " + table_name + " "
    )
    query += "CREATE TABLE " + table_name
    query += " ( user_id VARCHAR(50) not null, num INT not null, array VARBINARY(MAX) not null )"
    cursor.execute(query)
    cursor.commit()

