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
    r = a * np.exp(b)  # 91.5 µs ± 266 ns per loop (10000 loops each)
    r = ne.evaluate("a*exp(b)") # 161 µs ± 5.88 µs per loop (10000 loops each)
    r = expcpu(a, b)  # 107 µs ± 418 ns per loop (10000 loops each)
    r = expcuda(a, b) # 780 µs ± 63.5 µs per loop (1 loop each)

    S1 = 1000
    S2 = 1000
    r = a * np.exp(b)  # 9.36 ms ± 23.4 µs per loop (100 loops each)
    r = ne.evaluate("a*exp(b)") # 414 µs ± 10.7 µs per loop (1000 loops each)
    r = expcpu(a, b)  # 10.6 ms ± 17.5 µs per loop (100 loops each)
    r = expcuda(a, b) # 3.5 ms ± 1.01 ms per loop (1 loop each)
    
    S1 = 10000
    S2 = 10000
    r = a * np.exp(b)  # 1.07 s ± 1.33 ms per loop (1 loop each)
    r = ne.evaluate("a*exp(b)") # 43.8 ms ± 237 µs per loop (10 loops each)
    r = expcpu(a, b)  # 1.16 s ± 1.97 ms per loop (1 loop each)
    r = expcuda(a, b) # 283 ms ± 31 ms per loop (1 loop each)

    S1 = 100000
    S2 = 10000
    r = a * np.exp(b)  # 10.6 s ± 7.08 ms per loop (1 loop each)
    r = ne.evaluate("a*exp(b)") # 361 ms ± 5.96 ms per loop (1 loop each)
    r = expcpu(a, b)  # 11.5 s ± 23.3 ms per loop (1 loop each)
    r = expcuda(a, b) # CUDA OOM on NVIDIA P100
    
    S1 = 100000
    S2 = 100000
    r = a * np.exp(b)  # 1min 46s ± 59 ms per loop (1 loop each)
    r = ne.evaluate("a*exp(b)") # 3.49 s ± 72.6 ms per loop (1 loop each)
    r = expcpu(a, b)  # 1min 55s ± 154 ms per loop (1 loop each)
    r = expcuda(a, b) # CUDA OOM on NVIDIA P100
    
    
@vectorize(["float32(float32, float32)"], target="cpu")
def sincpu(a, b):
    return a*math.sin(b)
    # return a*np.sin(b)


@vectorize(["float32(float32, float32)"], target="cuda")
def sincuda(a, b):
    return a*math.sin(b)
    
    
def benchmark_sin():
    "Benchmark done using %timeit (mean ± std. dev. of 7 runs) using np.float32"
    S1 = 100
    S2 = 100
    a = np.random.randn(S1, S2).astype(np.float32)
    b = np.random.randn(S1, S2).astype(np.float32)
    r = a * np.sin(b)  # 91.1 µs ± 385 ns per loop (10000 loops each)
    r = ne.evaluate("a*sin(b)") # 148 µs ± 9.26 µs per loop (10000 loops each)
    r = sincpu(a, b)  # 106 µs ± 260 ns per loop (10000 loops each)
    r = sincuda(a, b)  # 782 µs ± 81.2 µs per loop (1 loop each)
   
    S1 = 1000
    S2 = 1000
    r = a * np.sin(b)  # 9.39 ms ± 39.4 µs per loop (100 loops each)
    r = ne.evaluate("a*sin(b)") # 444 µs ± 9.12 µs per loop (1000 loops each)
    r = sincpu(a, b)  # 10.6 ms ± 30.4 µs per loop (100 loops each)
    r = sincuda(a, b)  # 3.54 ms ± 1.01 ms per loop (1 loop each)
    
    S1 = 10000
    S2 = 10000
    r = a * np.sin(b)  # 1.07 s ± 2.39 ms per loop (1 loop each)
    r = ne.evaluate("a*sin(b)") # 44.2 ms ± 258 µs per loop (10 loops each)
    r = sincpu(a, b)  # 1.08 s ± 6.04 ms per loop (1 loop each)
    r = sincuda(a, b)  # 268 ms ± 30.8 ms per loop (1 loop each)
    
    S1 = 100000
    S2 = 10000
    r = a * np.sin(b)  # 10.7 s ± 15.5 ms per loop (1 loop each)
    r = ne.evaluate("a*sin(b)") # 426 ms ± 3.83 ms per loop (1 loop each)
    r = sincpu(a, b)  # 10.9 s ± 18.3 ms per loop (1 loop each)
    r = sincuda(a, b)  # 2.67 s ± 19 ms per loop (1 loop each)
    
    S1 = 100000
    S2 = 100000
    r = a * np.sin(b)  # 1min 47s ± 230 ms per loop (1 loop each)
    r = ne.evaluate("a*sin(b)") # 4.34 s ± 21.2 ms per loop (1 loop each)
    r = sincpu(a, b)  # 1min 47s ± 239 ms per loop (1 loop each)
    r = sincuda(a, b)  # CUDA OOM on NVIDIA P100
    
 
