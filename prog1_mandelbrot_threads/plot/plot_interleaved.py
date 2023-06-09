import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y1 = np.array([1.00, 1.97, 1.60, 2.39, 2.42, 3.10, 3.22, 3.46])
y2 = np.array([1.01, 1.67, 2.17, 2.54, 2.86, 3.26, 3.56, 3.58])
y3 = np.array([1.01, 1.93, 2.88, 3.75, 3.09, 3.61, 3.69, 3.45])
y4 = np.array([1.00, 1.96, 2.87, 3.67, 3.14, 3.42, 3.53, 3.62])

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
plt.savefig(fname="image/3.png")
plt.show()
