import numpy as np
import numexpr as ne
from numba import vectorize
import math

"""
On this benchmark we compare several operations using numpy, numexpr and numba (CPU&GPU)
"""


@vectorize(["int16(int16, int16)"], target="cpu")
def multicpu(a, b):
    return a * b


@vectorize(["int16(int16, int16)"], target="cuda")
def multicuda(a, b):
    return a * b


def benchmark_multiplication_int():
    """Benchmark done using %timeit (mean ± std. dev. of 7 runs) using np.int16
    NOTE: For numba solutions, having a solution empty vector speeds up around 10%
    r0 = np.empty((S1, S2), dtype=np.int16)
    r0 = multicpu(a, b)
    source: https://devblogs.nvidia.com/numba-python-cuda-acceleration/
    """
    S1 = 100
    S2 = 100
    a = np.random.randint(1, 5, (S1, S2), dtype=np.int16)
    b = np.random.randint(1, 10, (S1, S2), dtyp=np.int16)
    r = a * b  # 1.79 µs ± 7.29 ns per loop (100000 loops each)
    r = ne.evaluate("a*b")  # 761 µs ± 82.6 µs per loop (1000 loops each)
    r = multicpu(a, b)  # 1.85 µs ± 123 ns per loop (100000 loops each)
    r = multicuda(a, b)  # 1.35 ms ± 74.2 µs per loop (1 loop each)

    # Testing with a different size
    S1 = 1000
    S2 = 1000
    r = a * b  # 194 µs ± 7.61 µs per loop (1000 loops each)
    r = ne.evaluate("a*b")  # 679 µs ± 15.8 µs per loop (1000 loops each)
    r = multicpu(a, b)  # 194 µs ± 13.8 µs per loop (1000 loops each)
    r = multicuda(a, b)  # 3.39 ms ± 802 µs per loop (1 loop each)

    S1 = 10000
    S2 = 10000
    r = a * b  # 116 ms ± 5.58 ms per loop (10 loops each)
    r = ne.evaluate("a*b")  # 57.7 ms ± 1.58 ms per loop (10 loops each)
    r = multicpu(a, b)  # 120 ms ± 5.58 ms per loop (10 loops each)
    r = multicuda(a, b)  # 301 ms ± 75.7 ms per loop (1 loop each)

    S1 = 100000
    S2 = 10000
    r = a * b  # 1.52 s ± 261 ms per loop (1 loop each)
    r = ne.evaluate("a*b")  # 430 ms ± 27 ms per loop (1 loop each)
    r = multicpu(a, b)  # 1.37 s ± 134 ms per loop (1 loop each)
    r = multicuda(a, b)  # 2.2 s ± 169 ms per loop (1 loop each)

    S1 = 100000
    S2 = 100000
    r = a * b  # 9.36 s ± 273 ms per loop (1 loop each)
    r = ne.evaluate("a*b")  # 2.67 s ± 17.4 ms per loop (1 loop each)
    r = multicpu(a, b)  # 8.65 s ± 40.9 ms per loop (1 loop each)
    r = multicuda(a, b) # CUDA OOM on NVIDIA P100
    

@vectorize(["float32(float32, float32)"], target="cpu")
def multfcpu(a, b):
    return a * b


@vectorize(["float32(float32, float32)"], target="cuda")
def multfcuda(a, b):
    return a * b
    
    
def benchmark_multiplication_float():
    "Benchmark done using %timeit (mean ± std. dev. of 7 runs) using np.float32"
    S1 = 100
    S2 = 100
    a = np.random.randn(S1, S2).astype(np.float32)
    b = np.random.randn(S1, S2).astype(np.float32)
    r = a * b  # 2.7 µs ± 35.1 ns per loop (100000 loops each)
    r = ne.evaluate("a*b")  # 147 µs ± 10.4 µs per loop (10000 loops each)
    r = multfcpu(a, b)  # 3.18 µs ± 7.9 ns per loop (100000 loops each)
    r = multfcuda(a, b) # 778 µs ± 91.4 µs per loop (1 loop each)

    S1 = 1000
    S2 = 1000
    r = a * b  # 400 µs ± 1.25 µs per loop (1000 loops each)
    r = ne.evaluate("a*b")  # 247 µs ± 8.39 µs per loop (1000 loops each)
    r = multfcpu(a, b)  # 420 µs ± 3.43 µs per loop (1000 loops each)
    r = multfcuda(a, b) # 3.68 ms ± 1.02 ms per loop (1 loop each)
    
    S1 = 10000
    S2 = 10000
    r = a * b  # 176 ms ± 543 µs per loop (10 loops each)
    r = ne.evaluate("a*b")  # 34 ms ± 308 µs per loop (10 loops each)
    r = multfcpu(a, b)  # 174 ms ± 1.01 ms per loop (10 loops each)
    r = multfcuda(a, b) # 282 ms ± 35.9 ms per loop (1 loop each)

    S1 = 100000
    S2 = 10000       
    r = a * b  # 1.73 s ± 11.7 ms per loop (1 loop each)
    r = ne.evaluate("a*b")  # 318 ms ± 10.3 ms per loop (1 loop each)
    r = multfcpu(a, b)  # 1.73 s ± 5.16 ms per loop (1 loop each)
    r = multfcuda(a, b) # 2.84 s ± 7.87 ms per loop (1 loop each)
    
    S1 = 100000
    S2 = 100000
    r = a * b  # 17.9 s ± 564 ms per loop (1 loop each)
    r = ne.evaluate("a*b")  # 3.02 s ± 49.4 ms per loop (1 loop each)
    r = multfcpu(a, b)  # 17.1 s ± 28.3 ms per loop (1 loop each)
    r = multfcuda(a, b) # CUDA OOM on NVIDIA P100
    

@vectorize(["float32(float32, float32)"], target="cpu")
def expcpu(a, b):
    return a*math.exp(b)
    #return a*np.exp(b)


@vectorize(["float32(float32, float32)"], target="cuda")
def expcuda(a, b):
    return a*math.exp(b)
    #return a*np.exp(b) # raises UntypedAttributeError

    
def benchmark_exponential():
    "Benchmark done using %timeit (mean ± std. dev. of 7 runs) using np.float32"
    S1 = 100
    S2 = 100
    a = np.random.randn(S1, S2).astype(np.float32)
    b = np.random.randn(S1, S2).astype(np.float32)
    r = a * np.exp(b)  # 
    r = ne.evaluate("a*exp(b)") # 
    r = expcpu(a, b)  # 
    r = expcuda(a, b) #

    
@vectorize(["float32(float32, float32)"], target="cpu")
def sincpu(a, b):
    #return a*math.exp(b)
    return a*np.sin(b)


@vectorize(["float32(float32, float32)"], target="cuda")
def sincuda(a, b):
    #return a*math.exp(b)
    return a*np.sin(b)
    
def benchmark_sin():
    "Benchmark done using %timeit (mean ± std. dev. of 7 runs) using np.float32"
    S1 = 100
    S2 = 100
    a = np.random.randn(S1, S2).astype(np.float32)
    b = np.random.randn(S1, S2).astype(np.float32)
    c = a * np.sin(b)  # 
    c = ne.evaluate("a*sin(b)") 

    
def benchmark():
    """Benchmark done using %timeit (mean ± std. dev. of 7 runs)"""
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
    c = a * np.exp(b)  # 2min 27s ± 5.13 s per loop (1 loop each)
    c = ne.evaluate("a*exp(b)")  # 1min 6s ± 6.1 s per loop (1 loop each)

    # Benchmark sine
    a = np.random.randn(100, 100)
    b = np.random.randn(100, 100)
    c = a * np.sin(b)  # 138 µs ± 7.53 µs per loop (10000 loops each)
    c = ne.evaluate("a*sin(b)")  # 158 µs ± 1.51 µs per loop (10000 loops each)

    a = np.random.randn(1000, 1000)
    b = np.random.randn(1000, 1000)
    c = a * np.sin(b)  # 14.4 ms ± 422 µs per loop (100 loops each)
    c = ne.evaluate("a*sin(b)")  # 2.59 ms ± 31.8 µs per loop (100 loops each)

    a = np.random.randn(10000, 10000)
    b = np.random.randn(10000, 10000)
    c = a * np.sin(b)  # 1.9 s ± 17.5 ms per loop (1 loop each)
    c = ne.evaluate("a*sin(b)")  # 379 ms ± 10.9 ms per loop (1 loop each)

    a = np.random.randn(100000, 10000)  # note the size is (1e5, 1e4)
    b = np.random.randn(100000, 10000)
    c = a * np.sin(b)  # 2min 34s ± 16.5 s per loop (1 loop each)
    c = ne.evaluate("a*sin(b)")  # 1min 1s ± 1.48 s per loop (1 loop each)

