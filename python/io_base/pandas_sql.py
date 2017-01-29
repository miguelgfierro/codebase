# From datacamp pandas cheat sheet:
# https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PandasPythonForDataScience+(1).pdf

import pandas as pd
from sqlalchemy import create_engine


def save_file(data, connection_string):
    engine = create_engine(connection_string)
    pd.to_sql(data, engine)


def read_file(connection_string='sqlite:///:memory:'):
    engine = create_engine(connection_string)
    pd.read_sql("SELECT * FROM my_table;", engine)
    pd.read_sql_table('my_table', engine)
    pd.read_sql_query("SELECT * FROM my_table;", engine)

