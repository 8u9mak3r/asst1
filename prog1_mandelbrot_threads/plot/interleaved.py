import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y1 = np.array([1.00, 1.95, 1.66, 2.41, 2.40, 3.15, 3.23, 3.88])
y2 = np.array([1.02, 1.67, 2.15, 2.45, 2.92, 3.34, 3.73, 4.09])
y3 = np.array([1.00, 1.90, 2.86, 3.77, 4.65, 5.48, 6.31, 7.06])
y4 = np.array([1.01, 1.95, 2.83, 3.74, 4.65, 5.33, 5.98, 6.96])

plt.plot(x, y3,
         color="red",
         linestyle="-",
         linewidth=2,
         marker="o",
         markersize=6,
         alpha=0.7,
         label="View 1 Interleaved"
         )

plt.plot(x, y4,
         color="purple",
         linestyle="-",
         linewidth=2,
         marker="*",
         markersize=6,
         alpha=0.7,
         label="View 2 Interleaved"
         )

plt.plot(x, y1,
         color="blue",
         linestyle="-",
         linewidth=2,
         marker="o",
         markersize=6,
         alpha=0.7,
         label="View 1 Blocked"
         )

plt.plot(x, y2,
         color="green",
         linestyle="-",
         linewidth=2,
         marker="*",
         markersize=6,
         alpha=0.7,
         label="View 2 Blocked"
         )


plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.legend()
plt.savefig(fname="../image/3.png")
plt.show()
