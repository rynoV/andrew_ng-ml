import numpy as np


def featureNormalize(X):
    """
    Normalizes the features in X. returns a normalized version of X where
    the mean value of each feature is 0 and the standard deviation
    is 1.

    Parameters
    ----------
    X : array_like
        The dataset of shape (m x n).

    Returns
    -------
    X_norm : array_like
        The normalized dataset of shape (m x n).
    """
    X_norm = X.copy()
    mu = np.zeros(X.shape[1])
    sigma = np.zeros(X.shape[1])
    for i in range(X.shape[1]):
        feature = X[:, i]
        mu[i] = np.mean(feature)
        sigma[i] = np.std(feature)
        X_norm[:, i] = (X_norm[:, i] - mu[i]) / sigma[i]

    return X_norm, mu, sigma
