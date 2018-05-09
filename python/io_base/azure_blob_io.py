import os
import pandas as pd
from io import StringIO
import pyspark
from pyspark import SparkConf
from azure.storage.blob import BlockBlobService


class BlobIO(object):
    """Azure Blob Storage IO manager.
    More info: http://azure-storage.readthedocs.io/ref/azure.storage.blob.blockblobservice.html
    Attributes:
        service (object): Blob service object
        account_name (str): Account name
        account_key (str): Account key
    """
    def __init__(self, account_name, account_key):
        """Initializer
        Args:
            account_name (str): Account name
            account_key (str): Account key
        """
        self.service = BlockBlobService(account_name=account_name,
                                        account_key=account_key)
        self.account_name = account_name
        self.account_key = account_key

    def upload_file(self, container, blob_path, local_path):
        """Uploads a file to a blob inside a container
        Args:
            container (str): Container name
            blob_path (str): Blob path
            local_path (str): Local path to the file
        Examples:
            >>> from json_io import read_file
            >>> cred = read_file('../../share/blob_config.json')
            >>> blob = BlobIO(cred['account_name'], cred['account_key'])
            >>> blob.upload_file('codebase', 'upload/traj.csv', '../../share/traj.csv')

        """
        # FIXME: add a condition to make sure I am modifying the blob
        if not self.service.exists(container_name=container):
            self.service.create_container(container)
        self.service.create_blob_from_path(container,
                                           blob_path,
                                           local_path)

    def upload_folder(self, container, blob_path, local_path):
        pass

    def download_file(self, container, blob_path, local_path):
        """Download a file from a blob inside a container
        Args:
            container (str): Container name
            blob_path (str): Blob path
            local_path (str): Local path to the file
        Returns:
            etag (str): Value to check if the blob has been modified
        Examples:
            >>> from json_io import read_file
            >>> cred = read_file('../../share/blob_config.json')
            >>> blob = BlobIO(cred['account_name'], cred['account_key'])
            >>> blob.download_file('codebase', 'upload/traj.csv', '../../share/traj_blob.csv')
            True

        """
        self.service.get_blob_to_path(container,
                                      blob_path,
                                      local_path)
        if os.path.isfile(local_path):
            return True
        else:
            return False

    def download_folder(self, container, blob_path, local_path):
        pass

    def list_blobs(self, container, blob_path=None):
        """List files (blobs) in container
        Args:
            container (str): Container name
            blob_path (str): Blob path
        Returns:
            blobs (list): List of blobs
        Examples:
            >>> from json_io import read_file
            >>> cred = read_file('../../share/blob_config.json')
            >>> blob = BlobIO(cred['account_name'], cred['account_key'])
            >>> files = blob.list_blobs('codebase', 'upload')
            >>> files
            ['upload/traj.csv', 'upload/traj.txt']

        """
        blobs = [b.name for b in self.service.list_blobs(
            container, prefix=blob_path)]
        return blobs

    def list_containers(self):
        """List the containers
        Args:
            container (str): Container name
        Returns:
            blobs (list): List of blobs
        Examples:
            >>> from json_io import read_file
            >>> cred = read_file('../../share/blob_config.json')
            >>> blob = BlobIO(cred['account_name'], cred['account_key'])
            >>> files = blob.list_containers()
            >>> files
            ['codebase', 'datasets', 'deep-learning', 'installer', 'projects', 'vhds']

        """
        containers = [c.name for c in self.service.list_containers()]
        return containers

    def read_pandas_dataframe(self, container, blob_path, **kargs):
        """Read a pandas dataframe from blob
        Args:
            container (str): Container name
            blob_path (str): Blob path
            sep (str): Separator
        Returns:
            df (pd.DataFrame): Dataframe
        Examples:
            >>> from json_io import read_file
            >>> cred = read_file('../../share/blob_config.json')
            >>> blob = BlobIO(cred['account_name'], cred['account_key'])
            >>> df = blob.read_pandas_dataframe('codebase', 'upload/traj.csv',
            ...                                 sep=',', header=None, names=['time','q1','q2'])
            >>> df
                   time   q1   q2
            0  0.041667  443  205
            1  0.083333  444  206
            >>> df = blob.read_pandas_dataframe('codebase', 'upload/traj.txt',
            ...                                 sep=' ', header=None)
            >>> df
                      0   1   2
            0  0.041667 443 205
            1  0.083333 444 206
            2  0.125000 445 205
            3  0.166667 444 204

        """
        blob = self.service.get_blob_to_text(container, blob_path)
        df = pd.read_csv(StringIO(blob.content), **kargs)
        return df

    def read_spark_dataframe(self, container, blob_path, spark=None, **kargs):
        """Read a spark dataframe from blob
        Args:
            container (str): Container name
            blob_path (str): Blob path
            spark (object): Spark context
        Returns:
            df (): Dataframe
        Examples:
            >>> from json_io import read_file
            >>> cred = read_file('../../share/blob_config.json')
            >>> blob = BlobIO(cred['account_name'], cred['account_key'])
            >>> df = blob.read_spark_dataframe('codebase', 'upload/traj_header.csv', 
                                               header=True, inferSchema=True)
            >>> df.head(2)
            [Row(t=0.0416667, q0=443, q1=205), Row(t=0.0833333, q0=444, q1=206)]

        """
        spark = self._manage_spark_config(spark)
        wasb_template = "wasb://{container}@{store_name}.blob.core.windows.net/{blob_name}"
        wasb = wasb_template.format(container=container,
                                    store_name=self.account_name,
                                    blob_name=blob_path)
        df = spark.read.csv(wasb, **kargs)
        return df

    def _manage_spark_config(self, spark):
        if spark is None:
            spark = pyspark.sql.SparkSession.builder.config(conf=SparkConf()).getOrCreate()
        sc = spark.sparkContext
        spark_config_template = "fs.azure.account.key.{store_name}.blob.core.windows.net"
        spark_config = spark_config_template.format(store_name=self.account_name)
        sc._jsc.hadoopConfiguration().set(spark_config, self.account_key)
        sc._jsc.hadoopConfiguration().set("fs.wasb.impl", "org.apache.hadoop.fs.azure.NativeAzureFileSystem")
        spark.conf.set(spark_config, self.account_key)
        return spark
