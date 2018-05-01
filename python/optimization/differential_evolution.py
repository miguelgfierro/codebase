from scipy.optimize import differential_evolution


def optimize_function(func, bounds, **kargs):
    """Function optimization using Differential Evolution algorithm.
    https://en.wikipedia.org/wiki/Differential_evolution
    Info: https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.optimize.differential_evolution.html
    Args:
        func (callable): The objective function to be minimized. In the form f(x, *args), where x is the argument in
                         the form of a 1-D array and args is a tuple of any additional parameters.
        bounds (array): Constraints (min, max) pairs for each element in x.
    Returns:
        result (object): Result of the optimization. For parameters see:
        https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.optimize.OptimizeResult.html#scipy.optimize.OptimizeResult
    Examples:
        >>> from functions import rosenbrock
        >>> bounds = [(0,2), (0, 2), (0, 2), (0, 2), (0, 2)]
        >>> result = optimize_function(rosenbrock, bounds)
        >>> result.x # Solution
        array([1., 1., 1., 1., 1.])
        >>> result.fun # Final value of the objective function
        0.0
        >>> result.success
        True
        >>> from functions import ackley
        >>> bounds = [(-5, 5), (-5, 5)]
        >>> result = optimize_function(ackley, bounds, strategy='best2exp')
        >>> result.x # Solution
        array([0., 0.])
        >>> round(result.fun) # Final value of the objective function (around 4e-16)
        0.0
        >>> result.success
        True

    """
    result = differential_evolution(func, bounds, **kargs)
    return result

