import pyodbc


def connect_to_database(
    database,
    user,
    password,
    driver="ODBC Driver 13 for SQL Server",
    server="localhost",
    port=1433,
):
    """    Connect to a SQL server database.
    
    Args:
        database (str): Database name.
        user (str): User name.
        password (str): Password.
        driver (str): SQL driver. For windows: 'ODBC Driver 13 for SQL Server',
        for linux: 'FreeTDS'.
        server(str): Server name.
        port (int): Port of the SQL server.
    
    Returns:
        object: Connector object.

    """
    db_driver = "DRIVER={" + driver + "}"
    port_num = "PORT=" + str(port)
    server_name = "SERVER=" + server
    db_name = "DATABASE=" + database
    uid = "UID=" + user
    pwd = "PWD=" + password
    connection_string = ";".join([db_driver, server_name, port_num, db_name, uid, pwd])
    return pyodbc.connect(connection_string)

