from scipy.optimize import rosen
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plot


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


def plot_function2D(x, y, z):
    """Plot 2D function with matplotlib
    Args:
        x (array): X value.
        y (array): Y value.
        z (array): function value.
    Examples:
        >>> s = 0.05
        >>> X = np.arange(-2, 2.+s, s)
        >>> Y = np.arange(-2, 6.+s, s)
        >>> X, Y = np.meshgrid(X, Y)
        >>> f = rosenbrock([X, Y])
        >>> plot_function2D(X, Y, f)

    """
    fig = plot.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
             linewidth=0, antialiased=False)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plot.show()
