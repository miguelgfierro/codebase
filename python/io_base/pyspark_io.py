import pandas as pd


def save_csv_folder(dataframe, folder, **kwargs):
    """Save a dataframe as several csv spark partitions in a folder.
    Args:
        dataframe (spark.DataFrame): A dataframe.
        folder (str): Folder path.
    Examples:
        >>> shutil.rmtree("test_spark", ignore_errors=True)
        >>> columns = ['id', 'dogs', 'cats']
        >>> vals = [(1, 2, 0), (2, 0, 1)]
        >>> df = spark.createDataFrame(vals, columns)
        >>> save_csv_folder(df, "test_spark", header=True, mode="overwrite")
        >>> os.path.isdir("test_spark")
        True
        >>> len(glob.glob1("test_spark","*.csv"))
        2

    """
    dataframe.write.csv(folder, **kwargs)


def save_csv_folder_1file(dataframe, folder, **kwargs):
    """Save a dataframe as one csv spark partitions in a folder.
    Args:
        dataframe (spark.DataFrame): A dataframe.
        folder (str): Folder path.
    Examples:
        >>> shutil.rmtree("test_spark_one", ignore_errors=True)
        >>> columns = ['id', 'dogs', 'cats']
        >>> vals = [(1, 2, 0), (2, 0, 1)]
        >>> df = spark.createDataFrame(vals, columns)
        >>> save_csv_folder_1file(df, "test_spark_one", header=True, mode="overwrite")
        >>> os.path.isdir("test_spark_one")
        True
        >>> len(glob.glob1("test_spark_one","*.csv"))
        1

    """
    dataframe.coalesce(1).write.csv(folder, **kwargs)


def save_csv_file(dataframe, filename, **kwargs):
    """Save a dataframe as one csv using pandas.
    Args:
        dataframe (spark.DataFrame): A dataframe.
        filename (str): Name of the file.
    Examples:
        >>> shutil.rmtree("test_spark_one", ignore_errors=True)
        >>> columns = ['id', 'dogs', 'cats']
        >>> vals = [(1, 2, 0), (2, 0, 1)]
        >>> df = spark.createDataFrame(vals, columns)
        >>> save_csv_folder(df, "test_spark_one", header=True, mode="overwrite")
        >>> os.path.isdir("test_spark_one")
        True
        >>> len(glob.glob1("test_spark_one","*.csv"))
        1

    """
    dataframe.toPandas().to_csv(filename, **kwargs)


def read_csv_file(filename, **kwargs):
    pass


def read_csv_folder(folder, **kwargs):
    pass
