import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y1 = np.array([1.00, 1.95, 1.66, 2.41, 2.40, 3.15, 3.23, 3.88])
y2 = np.array([1.02, 1.67, 2.15, 2.45, 2.92, 3.34, 3.73, 4.09])

plt.plot(x, y1,
         color="red",
         linestyle="-",
         linewidth=2,
         marker="o",
         markersize=6,
         alpha=0.7,
         label="View 1"
         )

plt.plot(x, y2,
         color="blue",
         linestyle="-",
         linewidth=2,
         marker="*",
         markersize=6,
         alpha=0.7,
         label="View 2"
         )

plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.legend()
plt.savefig(fname="../image/1.png")
plt.show()
