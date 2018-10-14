import numpy as np
import numexpr as ne

# Benchmark done using %timeit (mean ± std. dev. of 7 runs)
# Benchmark integers
a = np.random.randint(1, 5, (100, 100))
b = np.random.randint(1, 10, (100, 100))
c = a * b  # 6.35 µs ± 354 ns per loop (10000 loops each)
c = ne.evaluate("a*b")  # 153 µs ± 6.02 µs per loop (10000 loops each)

a = np.random.randint(1, 5, (1000, 1000))
b = np.random.randint(1, 10, (1000, 1000))
c = a * b  # 1.12 ms ± 34.1 µs per loop (1000 loops each)
c = ne.evaluate("a*b")  # 738 µs ± 33.3 µs per loop (1000 loops each)

a = np.random.randint(1, 5, (10000, 10000))
b = np.random.randint(1, 10, (10000, 10000))
c = a * b  # 568 ms ± 24.8 ms per loop (1 loop each)
c = ne.evaluate("a*b")  # 303 ms ± 27.2 ms per loop (1 loop each)

a = np.random.randint(1, 5, (100000, 10000))  # note the size is (1e5, 1e4)
b = np.random.randint(1, 10, (100000, 10000))
c = a * b  # 31.2 s ± 288 ms per loop
c = ne.evaluate("a*b")  # 21.6 s ± 493 ms per loop

# Benchmark float
a = np.random.randn(100, 100)
b = np.random.randn(100, 100)
c = a * b  # 6.16 µs ± 360 ns per loop (10000 loops each)
c = ne.evaluate("a*b")  # 154 µs ± 2.02 µs per loop (10000 loops each)

a = np.random.randn(1000, 1000)
b = np.random.randn(1000, 1000)
c = a * b  # 1.21 ms ± 25.3 µs per loop (1000 loops each)
c = ne.evaluate("a*b")  # 841 µs ± 63 µs per loop (1000 loops each)

a = np.random.randn(10000, 10000)
b = np.random.randn(10000, 10000)
c = a * b  # 600 ms ± 62.3 ms per loop (1 loop each)
c = ne.evaluate("a*b")  # 321 ms ± 19.4 ms per loop (1 loop each)

a = np.random.randn(100000, 10000)  # note the size is (1e5, 1e4)
b = np.random.randn(100000, 10000)
c = a * b  # 1min 35s ± 3.11 s per loop (1 loop each)
c = ne.evaluate("a*b")  # 1min 4s ± 6.01 s per loop (1 loop each)

# Benchmark exponential
a = np.random.randn(100, 100)
b = np.random.randn(100, 100)
c = a * np.exp(b)  # 76.2 µs ± 1.72 µs per loop (10000 loops each)
c = ne.evaluate("a*exp(b)")  # 158 µs ± 2.49 µs per loop (10000 loops each)

a = np.random.randn(1000, 1000)
b = np.random.randn(1000, 1000)
c = a * np.exp(b)  # 7.43 ms ± 242 µs per loop (1000 loops each)
c = ne.evaluate("a*exp(b)")  # 2.07 ms ± 63.2 µs per loop (1000 loops each)

a = np.random.randn(10000, 10000)
b = np.random.randn(10000, 10000)
c = a * np.exp(b)  # 1.25 s ± 22.1 ms per loop (1 loop each)
c = ne.evaluate("a*exp(b)")  # 324 ms ± 20.6 ms per loop (1 loop each)

a = np.random.randn(100000, 10000)  # note the size is (1e5, 1e4)
b = np.random.randn(100000, 10000)
c = a * np.exp(b) # 2min 27s ± 5.13 s per loop (1 loop each)
c = ne.evaluate("a*exp(b)")
