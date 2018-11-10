import pandas as pd


def save_csv_folder(dataframe, folder, **kwargs):
    """Save a csv as spark partitions in a folder.
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

    """
    dataframe.write.csv(folder, **kwargs)


def save_csv_folder_1file(dataframe, folder, **kwargs):
    pass


def save_csv_file(dataframe, filename):
    pass


def read_csv_file(filename, **kwargs):
    pass


def read_csv_folder(folder, **kwargs):
    pass
