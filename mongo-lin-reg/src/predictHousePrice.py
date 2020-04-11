import numpy as np

from featureNormalize import normalize, featureNormalize
from gradientDescent import gradientDescent
from loadData import loadData
from normalEquation import normalEquation


def predictHousePrice(sqFeet, numOfBedrooms):
    X, y = loadData()
    m = y.size
    if m > 10000:
        X_norm, mu, sigma = featureNormalize(X)
        X = prependOnesColumn(X_norm)
        alpha = 1
        num_iters = 400
        theta = np.zeros(3)
        theta, J_history = gradientDescent(X, y, theta, alpha, num_iters)
        # Normalize the new data in the same way we normalized the old
        newX = normalize([[sqFeet, numOfBedrooms]], mu, sigma)
        # Predict the price by calculating t1 + t2x2 + t3x3 (plugging the new values into our hypothesis)
        price = (np.c_[np.ones(1), newX] @ theta)[0]
        return 'Predicted price of a ${:.0f} sq-ft, ${:.0f} br house (using gradient descent): ${:.0f}' \
            .format(sqFeet, numOfBedrooms, price)
    else:
        X = prependOnesColumn(X)
        theta = normalEquation(X, y)
        price = np.array([1, sqFeet, numOfBedrooms]) @ theta
        return 'Predicted price of a ${:.0f} sq-ft, ${:.0f} br house (using normal equations): ${:.0f}' \
            .format(sqFeet, numOfBedrooms, price)


def prependOnesColumn(X):
    return np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)
