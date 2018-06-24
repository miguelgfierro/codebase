import sqlite3


def create_table(cursor, table_name, table_instruction):
    """Create a table and drop it if it exists.
    Args:
        cursor (object): sqlite cursor.
        table_name (str): Table name.
        table_instruction (str): Table variable definition.
    Example:
        >>> conn = sqlite3.connect('temp.db')
        >>> cur = conn.cursor()
        >>> instruction = '''num INT(11) NULL, float_num FLOAT(8,6) NOT NULL DEFAULT "0",letter CHAR(1),input_date DATE'''
        >>> create_table(cur, "table_name", instruction)
        >>> c = cur.execute('PRAGMA table_info([table_name]);')
        >>> cur.fetchall()
        [(0, 'num', 'INT(11)', 0, None, 0), (1, 'float_num', 'FLOAT(8,6)', 1, '"0"', 0), (2, 'letter', 'CHAR(1)', 0, None, 0), (3, 'input_date', 'DATE', 0, None, 0)]
        >>> instruction = '''t FLOAT(8, 6), q0 INT(5), q1 INT(5)'''
        >>> create_table(cur, "table_csv", instruction)
        >>> c = cur.execute('PRAGMA table_info([table_csv]);')
        >>> cur.fetchall()
        [(0, 't', 'FLOAT(8, 6)', 0, None, 0), (1, 'q0', 'INT(5)', 0, None, 0), (2, 'q1', 'INT(5)', 0, None, 0)]


    """
    query = "DROP TABLE IF EXISTS " + table_name + ";"
    cursor.execute(query)
    query = " CREATE TABLE " + table_name
    query += " (" + table_instruction + " );"
    cursor.execute(query)
