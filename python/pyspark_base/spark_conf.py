from pyspark.sql import SparkSession


def spark(app_name="App", url="local[*]", memory="10G", cores="16"):
    """Start Spark if not started
    
    Args:
        app_name (str): Set name of the application
        url (str): URL for spark master.
        memory (str): Size of memory for spark driver and executor.  
        cores (str): Number of executor cores
    
    Returns:
        obj: Spark context.
    
    Examples: 
        >>> spark = spark() # doctest: +SKIP
        >>> spark is not None
        True
    """
    return (
        SparkSession.builder.appName(app_name)
        .master(url)
        .config("spark.driver.memory", memory)
        .config("spark.executor.cores", cores)
        .config("spark.executor.memory", memory)
        .config("spark.memory.fraction", "0.9")
        .config("spark.memory.stageFraction", "0.3")
        .config("spark.executor.instances", 1)
        .config("spark.executor.heartbeatInterval", "36000s")
        .config("spark.network.timeout", "10000000s")
        .config("spark.driver.maxResultSize", "50g")
        .getOrCreate()
    )
