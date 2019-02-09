import os
import sys
import pytest
import numpy
import pandas
import subprocess
import glob
import json
import shutil
from collections import Counter
from pyspark.sql import SparkSession
import pyspark.sql.types as sptypes


@pytest.fixture(autouse=True)
def add_libraries(doctest_namespace):
    """Definition of doctest namespace
    More info: https://docs.pytest.org/en/latest/doctest.html#the-doctest-namespace-fixture
    """    
    doctest_namespace["os"] = os
    doctest_namespace["sys"] = sys
    doctest_namespace["np"] = numpy
    doctest_namespace["pd"] = pandas
    doctest_namespace["subprocess"] = subprocess
    doctest_namespace["glob"] = glob
    doctest_namespace["json"] = json
    doctest_namespace["shutil"] = shutil
    doctest_namespace["Counter"] = Counter
    spark = (
        SparkSession.builder.appName("test codebase")
        .master("local[*]")
        .config("spark.driver.memory", "4g")
        .getOrCreate()
    )
    doctest_namespace["spark"] = spark
    doctest_namespace["sptypes"] = sptypes
