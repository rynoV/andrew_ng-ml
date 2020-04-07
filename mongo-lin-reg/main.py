import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(np.random.randn(500), np.random.randn(500), np.random.randn(500), marker='o')
fig, axes = plt.subplots(2,2, sharex=True, sharey=True)
color = (e for e in ['r', 'g', 'k', 'b'])
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color=color.__next__(), alpha=0.5)
