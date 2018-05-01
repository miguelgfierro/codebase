from scipy.optimize import rosen
import numpy as np


def rosenbrock(x):
    """The Rosenbrock funtion is  is a non-convex function used as a performance test problem for optimization
    algorithms. The function is defined by: f(x,y) = (a-x)^2 + b(y-x^2)^2. The global minimum is inside a long, narrow,
    parabolic shaped flat valley. To find the valley is trivial. To converge to the global minimum, is difficult.
    More info: https://en.wikipedia.org/wiki/Rosenbrock_function

    """
    return rosen(x)


def ackley(x):
    """Custom function."""
    arg1 = -0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2))
    arg2 = 0.5 * (np.cos(2. * np.pi * x[0]) + np.cos(2. * np.pi * x[1]))
    return -20. * np.exp(arg1) - np.exp(arg2) + 20. + np.e
