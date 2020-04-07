import numpy as np


def computeCost(X, y, theta):
    """
    Compute cost for linear regression with multiple variables.
    Computes the cost of using theta as the parameter for linear regression to fit the data points in X and y.

    Parameters
    ----------
    X : array_like
        The dataset of shape (m x n+1).

    y : array_like
        A vector of shape (m, ) for the values at a given data point.

    theta : array_like
        The linear regression parameters. A vector of shape (n+1, )

    Returns
    -------
    J : float
        The value of the cost function.
    """
    m = y.shape[0]  # number of training examples
    predictions = X @ theta
    differences = predictions - y
    J = (1/(2*m)) * np.sum(differences**2)
    return J
