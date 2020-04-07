import numpy as np

from src.computeCost import computeCost


def gradientDescent(X, y, theta, alpha, num_iters):
    """
    Performs gradient descent to learn theta.
    Updates theta by taking num_iters gradient steps with learning rate alpha.

    Parameters
    ----------
    X : array_like
        The dataset of shape (m x n+1).

    y : array_like
        A vector of shape (m, ) for the values at a given data point.

    theta : array_like
        The linear regression parameters. A vector of shape (n+1, )

    alpha : float
        The learning rate for gradient descent.

    num_iters : int
        The number of iterations to run gradient descent.

    Returns
    -------
    theta : array_like
        The learned linear regression parameters. A vector of shape (n+1, ).

    J_history : list
        A python list for the values of the cost function after each iteration.
    """
    # Initialize some useful values
    m = y.shape[0]  # number of training examples

    # make a copy of theta, to avoid changing the original array, since numpy arrays
    # are passed by reference to functions
    theta = theta.copy()

    J_history = []  # Use a python list to save cost in every iteration

    for i in range(num_iters):
        # ==================== YOUR CODE HERE =================================
        # Calculate theta_1 * X_1 + theta_2 * X_2 + ... using matrix multiplication.
        predictions = X @ theta
        # Calculate the differences between the expected values and the actual values
        differences = predictions - y
        # Multiply each column in X by the difference (this is from the formula for the derivative of the error
        # function)
        sum_inner = np.apply_along_axis(lambda feature: feature * differences.T, 0, X)
        # Calculate the derivative of the error function and apply alpha for each feature
        change_in_theta = alpha * (1 / m) * np.sum(sum_inner, 0)
        # Update each theta with its respective change
        theta = theta - change_in_theta

        # =====================================================================

        # save the cost J in every iteration
        J_history.append(computeCost(X, y, theta))

    return theta, J_history
