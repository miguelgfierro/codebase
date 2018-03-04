from timeit import default_timer


class Timer(object):
    """Timer class.
    Examples:
        >>> import numpy as np
        >>> big_num = 10000000
        >>> t = Timer()
        >>> t.start()
        >>> r = 0
        >>> a = [r+i for i in range(big_num)]
        >>> t.stop()
        >>> np.round(t.interval)
        2.0
        >>> r = 0
        >>> with Timer() as t:
        ...   a = [r+i for i in range(big_num)]
        >>> np.round(t.interval)
        2.0

    """
    def __init__(self):
        self._timer = default_timer

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

    def start(self):
        """Start the timer."""
        self.init = self._timer()

    def stop(self):
        """Stop the timer. Calculate the interval in seconds."""
        self.end = self._timer()
        self.interval = self.end - self.init

