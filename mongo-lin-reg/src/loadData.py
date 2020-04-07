import os

import numpy as np


def loadData():
    data = np.loadtxt(os.path.join('..', 'data', 'housing.txt'), delimiter=',')
    X = data[:, :2]
    y = data[:, 2]
    return X, y

