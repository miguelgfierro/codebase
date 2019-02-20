import sqlite3
from contextlib import contextmanager
import csv


def insert_row(connector, table_name, table_instruction, values):
    """Insert a row of items in a table.
    
    Args:
        connector (object): sqlite connector.
        table_name (str): Table name.
        table_instruction (str): Instruction to insert the values.
        values (list): List with values to insert
    
    Example:
        >>> import datetime
        >>> conn = sqlite3.connect('temp.db')
        >>> instruction = '(num ,float_num, letter, input_date) VALUES (?,?,?,?)'
        >>> values = [5, 1.5, 'b', datetime.date(2000, 1, 1)]
        >>> insert_row(conn, 'table_name', instruction, values)
        >>> cur = conn.cursor()
        >>> result = cur.execute('SELECT * FROM table_name')
        >>> cur.fetchone()
        (5, 1.5, 'b', '2000-01-01')
    """
    query = "INSERT INTO " + table_name + " " + table_instruction
    with _commit_transaction(connector) as cur:
        cur.execute(query, values)


def insert_csv(connector, table_name, table_instruction, filename, header=False):
    """Insert the content of a csv file in a table.
    NOTE: the only way is to load the csv into memory and then
    insert it in the database.
    Source: https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python
    +info: http://adamantine.me/2017/05/22/how-to-write-data-to-a-sqlite-database-in-python/
    Args:
        cursor (object): sqlite cursor.
        connector (object): sqlite connector.
        table_name (str): Table name.
        filename (str): Path to csv file.
    
    Example:
        >>> conn = sqlite3.connect('temp.db')
        >>> instruction = '(t ,q0, q1) VALUES (?,?,?)'
        >>> insert_csv(conn, 'table_csv', instruction, os.path.abspath('share/traj.csv'))
        >>> cur = conn.cursor()
        >>> result = cur.execute('SELECT * FROM table_csv')
        >>> cur.fetchall()
        [(0.0416667, 443, 205), (0.0833333, 444, 206)]
    """
    f = open(filename, "r")  # open the csv data file
    if header:
        next(f, None)  # skip the header row
    reader = csv.reader(f)

    query = "INSERT INTO " + table_name + " " + table_instruction
    with _commit_transaction(connector) as cur:
        for row in reader:
            cur.execute(query, row)


@contextmanager
def _commit_transaction(connector):
    cur = connector.cursor()
    try:
        yield cur
        connector.commit()
    except:
        connector.rollback()
        raise
    finally:
        cur.close()
