# More information: https://miguelgfierro.com/blog/2018/a-beginners-guide-to-python-testing/
#

import pytest


def fibonacci(n):
    """Fibonacci series"""
    fib_values = [0, 1]
    for i in range(2, n):
        fib_values.append(fib_values[i-1] + fib_values[i-2])
    return fib_values


@pytest.mark.parametrize('n, fib_list', [
    (4, [0, 1, 1, 2]),
    (6, [0, 1, 1, 2, 3, 5]),
])
def test_implicit_pooling_synthetic(n, fib_list):
    values = fibonacci(n)
    assert values == fib_list
