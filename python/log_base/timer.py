import time


class Timer(object):
    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

    def start(self):
        self.start = time.clock()

    def stop(self):
        self.end = time.clock()
        self.interval = self.end - self.start

if __name__ == "__main__":

    big_num = 100000

    # Example with start and stop
    print("Example: start and stop")
    t = Timer()
    t.start()
    for i in range(big_num):
        r = 1
    t.stop()
    print("Request took %.03f sec.\n" % t.interval)

    # Example in with statement
    print("Example: with statement")
    with Timer() as t:
        for i in range(big_num):
            r = 1
    print("Request took %.03f sec.\n" % t.interval)

    # Example in try
    print("Example: try")
    try:
        with Timer() as t:
            for i in range(big_num):
                r = 1
            raise(Exception("Get out!"))
    finally:
        print("Request took %.03f sec.\n" % t.interval)

