# Differential evolution optimizer
# https://en.wikipedia.org/wiki/Differential_evolution
# Working version of scipy 0.19
# Function definition:
# https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.optimize.differential_evolution.html


from scipy.optimize import rosen, differential_evolution
import numpy as np


def rosenbrock(x):
    """The Rosenbrock funtion is  is a non-convex function used as a performance test problem for optimization
    algorithms. The function is defined by: f(x,y) = (a-x)^2 + b(y-x^2)^2. The global minimum is inside a long, narrow,
    parabolic shaped flat valley. To find the valley is trivial. To converge to the global minimum, is difficult.
    More info: https://en.wikipedia.org/wiki/Rosenbrock_function
    Examples:
        >>> bounds = [(0,2), (0, 2), (0, 2), (0, 2), (0, 2)]
        >>> result = optimize_function(rosenbrock, bounds)
        >>> result.x # Solution
        array([ 1.,  1.,  1.,  1.,  1.])
        >>> result.fun # Final value of the objective function
        0.0
        >>> result.success
        True

    """
    return rosen(x)


def ackley(x):
    """Custom function.
    Examples:
        >>> bounds = [(-5, 5), (-5, 5)]
        >>> result = optimize_function(ackley, bounds)
        >>> result.x # Solution
        array([ 0.,  0.])
        >>> result.fun # Final value of the objective function
        4.4408920985006262e-16
        >>> result.success
        True

    """
    arg1 = -0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2))
    arg2 = 0.5 * (np.cos(2. * np.pi * x[0]) + np.cos(2. * np.pi * x[1]))
    return -20. * np.exp(arg1) - np.exp(arg2) + 20. + np.e


def optimize_function(func, bounds):
    """Function optimization using Differential Evolution algorithm.
    Info: https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.optimize.differential_evolution.html
    Parameters:
        func (callable): The objective function to be minimized. In the form f(x, *args), where x is the argument in
                         the form of a 1-D array and args is a tuple of any additional parameters.
        bounds (array): Constraints (min, max) pairs for each element in x.
    Returns:
        result (object): Result of the optimization. For parameters see:
        https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.optimize.OptimizeResult.html#scipy.optimize.OptimizeResult
    """
    result = differential_evolution(func, bounds)
    return result

