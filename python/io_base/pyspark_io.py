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
        >>> len(glob.glob1("test_spark","*.csv")) > 1
        True

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
        >>> if os.path.isfile("df_spark.csv"):
        ...     os.remove("df_spark.csv")
        >>> columns = ['id', 'dogs', 'cats']
        >>> vals = [(1, 2, 0), (2, 0, 1)]
        >>> df = spark.createDataFrame(vals, columns)
        >>> save_csv_file(df, "df_spark.csv", header=True, index=False) # doctest: +SKIP
        >>> os.path.isfile("df_spark.csv") # doctest: +SKIP
        True

    """
    dataframe.toPandas().to_csv(filename, **kwargs)


def read_csv_file(spark, filename, **kwargs):
    """Read a csv file.
    Args:
        filename (str): Name of the file.
    Returns:
        dataframe (spark.DataFrame): An dataframe.
    Examples:
        >>> filename = os.path.join("share", "traj_header.csv")
        >>> df = read_csv_file(spark, filename, header=True, inferSchema=True)
        >>> df.head(2)
        [Row(t=0.0416667, q0=443, q1=205), Row(t=0.0833333, q0=444, q1=206)]
        >>> df.schema
        StructType(List(StructField(t,DoubleType,true),StructField(q0,IntegerType,true),StructField(q1,IntegerType,true)))
        >>> schema = sptypes.StructType([sptypes.StructField("t", sptypes.FloatType()), sptypes.StructField("q0", sptypes.IntegerType()), sptypes.StructField("q1", sptypes.StringType())])
        >>> df2 = read_csv_file(spark, filename, header=True, schema=schema)
        >>> df2.head(2)
        [Row(t=0.041666701436042786, q0=443, q1='205'), Row(t=0.08333329856395721, q0=444, q1='206')]
        >>> df2.schema  
        StructType(List(StructField(t,FloatType,true),StructField(q0,IntegerType,true),StructField(q1,StringType,true)))


    """
    return spark.read.csv(filename, **kwargs)


def read_csv_folder(spark, folder, **kwargs):
    """Read a csv folder of Spark format.
    Args:
        folder (str): Folder path.
    Returns:
        dataframe (spark.DataFrame): An dataframe.
    Examples:
        >>> path = os.path.join("share", "traj_spark")
        >>> df = read_csv_folder(spark, path, header=True, inferSchema=True)
        >>> df.head(2)
        [Row(t=0.0833333, q0=444, q1=205), Row(t=0.0416667, q0=443, q1=205)]
        >>> df.schema
        StructType(List(StructField(t,DoubleType,true),StructField(q0,IntegerType,true),StructField(q1,IntegerType,true)))

    """
    return spark.read.csv(folder, **kwargs)

