import numpy as np


# Two classes of activation functions: Saturated(tanh, sigmoid, softmax) and not saturated (RELU, ELU, Leaky-RELU)
# saturated: solve the so called “exploding/vanishing gradient”
# not saturated: accelerate the convergence speed
# More info on activation functions: http://cs231n.github.io/neural-networks-1/


def softmax(x):
    """Softmax of a vector. It is the normalized exponential function. Softmax is a generalization of the logistic
    function that squashes a vector z into another vector of real values in the range (0, 1) that add up to 1.
    Used for multiclass classification.
    Args:
        x (list or numpy array): Input list or array.
    Returns:
        result (numpy array): The softmax of the array.
    Examples:
        >>> scores = [12, 5, 1]
        >>> softmax(scores)
        array([9.99072278e-01, 9.11035992e-04, 1.66862063e-05])
        >>> sum(softmax(scores))
        1.0

    """
    return np.exp(x) / np.sum(np.exp(x), axis=0)


def tanh(x):
    """Hyperbolic tangent. Output between -1,1
    Args:
        x (list or numpy array): Input list or array.
    Returns:
        result (numpy array): The tanh of the array.
    Examples:
        >>> x = np.array([[1,1,-3],[0.5,-1,1]])
        >>> tanh(x)
        array([[ 0.76159416,  0.76159416, -0.99505475],
               [ 0.46211716, -0.76159416,  0.76159416]])

    """
    return np.tanh(x)


def sigmoid(x):
    """Sigmoid function. Output between 0,1
    Args:
        x (list or numpy array): Input list or array.
    Returns:
        result (numpy array): The sigmoid of the array.
    Examples:
        >>> x = np.array([[1,1,-3],[0.5,-1,1]])
        >>> sigmoid(x)
        array([[0.73105858, 0.73105858, 0.04742587],
               [0.62245933, 0.26894142, 0.73105858]])

    """
    return 1. / (1 + np.exp(-x))


def RELU(x, inplace=False):
    """Rectified Linear Unit, removing the negative parts of the input: max(x,0)
    Benchmark: https://stackoverflow.com/a/40013151/5620182
    Args:
        x (list or numpy array): Input list or array.
        inplace (bool): Inplace flag.
    Returns:
        result (numpy array): The RELU of the array (if inplace is True).
    Examples:
        >>> x = np.array([[1,1,-3],[0.5,-1,1]])
        >>> RELU(x)
        array([[ 1. ,  1. , -0. ],
               [ 0.5, -0. ,  1. ]])
        >>> RELU(x, inplace=True)
        >>> x
        array([[1. , 1. , 0. ],
               [0.5, 0. , 1. ]])

    """
    if inplace:
        np.maximum(x, 0, x)
    else:
        return x * (x > 0)


def LeakyRELU(x, alpha=0.3):
    """Leaky Rectified Linear Unit. It allows a small gradient when the unit is not active.
    `f(x) = alpha * x for x < 0, f(x) = x for x >= 0`
    Args:
        x (list or numpy array): Input list or array.
        alpha (float): Scale factor.
    Returns:
        result (numpy array): The LeakyRELU of the array .
    Examples:
        >>> x = np.array([[1,1,-3],[0.5,-1,1]])
        >>> LeakyRELU(x)
        array([[ 1. ,  1. , -0.9],
               [ 0.5, -0.3,  1. ]])

    """
    return (x >= 0)*x + (x < 0)*alpha*x


def ELU(x, alpha=1.0):
    """Exponential Linear Unit
    `f(x) =  alpha * (exp(x) - 1.) for x < 0`,
    `f(x) = x for x >= 0`.
    paper: http://arxiv.org/abs/1511.07289
    Args:
        x (list or numpy array): Input list or array.
        alpha (float): Scale factor.
    Returns:
        result (numpy array): The ELU of the array .
    Examples:
        >>> x = np.array([[1,1,-3],[0.5,-1,1]])
        >>> ELU(x)
        array([[ 1.        ,  1.        , -0.95021293],
               [ 0.5       , -0.63212056,  1.        ]])

    """
    return (x >= 0)*x + (x < 0)*(alpha * np.exp(x) - alpha)


def SELU(x):
    """Scaled Exponential Linear Unit
    paper: https://arxiv.org/abs/1706.02515
    Args:
        x (list or numpy array): Input list or array.
        alpha (float): Scale factor.
    Returns:
        result (numpy array): The SELU of the array .
    Examples:
        >>> x = np.array([[1,1,-3],[0.5,-1,1]])
        >>> SELU(x)
        array([[ 1.05070099,  1.05070099, -1.67056873],
               [ 0.52535049, -1.11133074,  1.05070099]])

    """
    alpha = 1.6732632423543772848170429916717
    scale = 1.0507009873554804934193349852946
    return scale * ((x >= 0)*x + (x < 0) * (alpha * np.exp(x) - alpha))
