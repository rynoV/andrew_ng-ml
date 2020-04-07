import numpy as np
from matplotlib import pyplot

from src.featureNormalize import featureNormalize
from src.gradientDescent import gradientDescent
from src.loadData import loadData
from src.normalEquation import normalEquation

X, y = loadData()
X_norm, mu, sigma = featureNormalize(X)

print('Computed mean:', mu)
print('Computed standard deviation:', sigma)
m = y.size
# Add intercept term to X
X = np.concatenate([np.ones((m, 1)), X_norm], axis=1)

alpha = 1
num_iters = 400

theta = np.zeros(3)
theta, J_history = gradientDescent(X, y, theta, alpha, num_iters)

# Plot the convergence graph
pyplot.plot(np.arange(len(J_history)), J_history, lw=2)
pyplot.xlabel('Number of iterations')
pyplot.ylabel('Cost J')
pyplot.show()

print('theta computed from gradient descent: {:s}'.format(str(theta)))

# Estimate the price of a 1650 sq-ft, 3 br house
# Normalize the new data in the same way we normalized the old
newX = (np.array([[1650, 3]]) - mu) / sigma
# Predict the price by calculating t1 + t2x2 + t3x3 (plugging the new values into our hypothesis)
price = (np.c_[np.ones(1), newX] @ theta)[0]

print('Predicted price of a 1650 sq-ft, 3 br house (using gradient descent): ${:.0f}'.format(price))

X, y = loadData()
# Add intercept term to X
X = np.concatenate([np.ones((m, 1)), X], axis=1)

# Calculate the parameters from the normal equation
theta = normalEquation(X, y)

print('Theta computed from the normal equations: {:s}'.format(str(theta)))

# Estimate the price of a 1650 sq-ft, 3 br house
price = np.array([1, 1650, 3]) @ theta

print('Predicted price of a 1650 sq-ft, 3 br house (using normal equations): ${:.0f}'.format(price))
