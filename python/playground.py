from __future__ import print_function
import os, sys
import cv2
from data_structures.list import *
from io_base.numpy_io import *
from io_base.pandas_io import *
from io_base.pandas_sql import *
from io_base.pickle_io import *
from log_base.logger import *
from log_base.memory_size import *
from log_base.timer import *
from minsc.system_info import *
from pandas_base.conversion_categorical import *
from pandas_base.stats import *
from pandas_base.value_selection import *
from plot_base.matplot_base import *


if __name__ == "__main__"  and __package__ is None:
    log = setup_logger(debug_level='INFO')
    log.info("Python playground")
    log.info("Python version: %s" % get_python_version())
    log.info("Pandas version: %s" % get_library_version('pandas'))
    log.info("Numpy version: %s" % get_library_version('numpy'))

    with Timer() as t:
        log.info("Starting process")
        # Add here the code -----


        # End of code -----
    log.info("Process finished in %.5f seconds" % t.interval)