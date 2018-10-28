import os
import sys
import cv2

# api
from python.api.cherrypy_html import *
from python.api.flask_basic import *
from python.api.flask_html import *
from python.api.flask_json import *

# data structures
from python.data_structures.abstract import *
from python.data_structures.binary_heaps import *
from python.data_structures.binary_search_tree import *
from python.data_structures.binary_tree import *
from python.data_structures.data_types import *
from python.data_structures.deque import *
from python.data_structures.exceptions import *
from python.data_structures.generator import *
from python.data_structures.graph_search import *
from python.data_structures.graph import *
from python.data_structures.hash_table import *
from python.data_structures.linked_list import *
from python.data_structures.list_manipulation import *
from python.data_structures.list_search import *
from python.data_structures.list_sort import *
from python.data_structures.queue import *
from python.data_structures.stack import *

# database
from python.database.sql_server.connector import *
from python.database.sql_server.create_table import *
from python.database.sql_server.insert_values import *
from python.database.sql_server.select_values import *

# image_base
from python.image_base.conversion import *
from python.image_base.opencv_transformation import *
from python.image_base.pil_transformation import *

# io_base
from python.io_base.argument_io import *

# from python.io_base.azure_blob_io import *
from python.io_base.dask_io import *
from python.io_base.fastparquet_io import *
from python.io_base.json_io import *
from python.io_base.numpy_io import *
from python.io_base.opencv_io import *
from python.io_base.pandas_io import *
from python.io_base.pickle_io import *
from python.io_base.pil_io import *
from python.io_base.scikit_image_io import *

# log_base
from python.log_base.formatting import *
from python.log_base.logger import *
from python.log_base.timer import *

# machine_learning
from python.machine_learning.activations import *
from python.machine_learning.dataset_split import *
from python.machine_learning.feature_engineering import *
from python.machine_learning.k_nearest_neighbor import *
from python.machine_learning.metrics import *

# numpy_base
from python.numpy_base.array_evaluation import *
from python.numpy_base.array_manipulation import *
from python.numpy_base.conversion import *

# optimization
from python.optimization.differential_evolution import *
from python.optimization.downhill_simplex import *
from python.optimization.functions import *

# pandas_base
from python.pandas_base.apply_functions import *
from python.pandas_base.clean import *
from python.pandas_base.conversion import *
from python.pandas_base.stats import *
from python.pandas_base.value_selection import *

# plot_base
from python.plot_base.matplot_base import *
from python.plot_base.opencv_plot import *
from python.plot_base.pil_plot import *
from python.plot_base.plot_confusion_matrix import *
from python.plot_base.scikit_image_plot import *

# system
# from python.system.notebook_memory_management import *
from python.system.paths import *
from python.system.system_info import *
from python.system.memory import *


# test
from python.test.unittest_fixtures import *

# url_base
from python.url_base.download_file import *
from python.url_base.selenium_base import *

# utilities
from python.utilities.git_stats import *
from python.utilities.google_trend_stats import *

if __name__ == "__main__" and __package__ is None:
    log = setup_logger(debug_level="INFO")
    log.info("Python playground")
    log.info("Python version: %s" % get_python_version())
    log.info("Pandas version: %s" % get_library_version("pandas"))
    log.info("Numpy version: %s" % get_library_version("numpy"))
    log.info("OpenCV version: %s" % get_library_version("cv2"))

    with Timer() as t:
        log.info("Starting process")
        # Add here the code -----

        # End of code -----
    log.info("Process finished in %.5f seconds" % t.interval)
