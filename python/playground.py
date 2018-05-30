from __future__ import print_function
import os
import sys
import cv2
# api
from api.cherrypy_html import *
from api.flask_basic import *
from api.flask_html import *
from api.flask_json import *

# data structures
from data_structures.abstract_class import *
from data_structures.binary_heaps import *
from data_structures.binary_search_tree import *
from data_structures.binary_tree import *
from data_structures.data_types import *
from data_structures.deque import *
from data_structures.exceptions import *
from data_structures.generator import *
from data_structures.graph_search import *
from data_structures.graph import *
from data_structures.hash_table import *
from data_structures.linked_list import *
from data_structures.list_manipulation import *
from data_structures.list_search import *
from data_structures.list_sort import *
from data_structures.queue import *
from data_structures.stack import *

# database
from database.sql_server.connector import *
from database.sql_server.create_table import *
from database.sql_server.insert_values import *
from database.sql_server.select_values import *

# image_base
from image_base.conversion import *
from image_base.opencv_transformation import *
from image_base.pil_transformation import *

# io_base
from io_base.argument_io import *
from io_base.azure_blob_io import *
from io_base.dask_io import *
from io_base.fastparquet_io import *
from io_base.json_io import *
from io_base.numpy_io import *
from io_base.opencv_io import *
from io_base.pandas_io import *
from io_base.pickle_io import *
from io_base.pil_io import *
from io_base.scikit_image_io import *

# log_base
from log_base.formatting import *
from log_base.logger import *
from log_base.timer import *

# machine_learning
from machine_learning.activations import *
from machine_learning.dataset_split import *
from machine_learning.feature_engineering import *
from machine_learning.k_nearest_neighbor import *
from machine_learning.metrics import *

# numpy_base
from numpy_base.array_evaluation import *
from numpy_base.array_manipulation import *
from numpy_base.conversion import *

# optimization
from optimization.differential_evolution import *
from optimization.downhill_simplex import *
from optimization.functions import *

# pandas_base
from pandas_base.apply_functions import *
from pandas_base.clean import *
from pandas_base.conversion import *
from pandas_base.stats import *
from pandas_base.value_selection import *

# plot_base
from plot_base.matplot_base import *
from plot_base.opencv_plot import *
from plot_base.pil_plot import *
from plot_base.plot_confusion_matrix import *
from plot_base.scikit_image_plot import *

# system
from system.memory_size import *
from system.notebook_memory_management import *
from system.paths import *
from system.system_info import *

# test
from test.unittest_setup_teardown import *

# url_base
from url_base.download_file import *
from url_base.selenium_base import *

# utilities
from utilities.git_stats import *
from utilities.google_trend_stats import *

if __name__ == "__main__" and __package__ is None:
    log = setup_logger(debug_level='INFO')
    log.info("Python playground")
    log.info("Python version: %s" % get_python_version())
    log.info("Pandas version: %s" % get_library_version('pandas'))
    log.info("Numpy version: %s" % get_library_version('numpy'))
    log.info("OpenCV version: %s" % get_library_version('cv2'))

    with Timer() as t:
        log.info("Starting process")
        # Add here the code -----

        # End of code -----
    log.info("Process finished in %.5f seconds" % t.interval)
