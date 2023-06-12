import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y1 = np.array([1.00, 1.95, 1.66, 2.41, 2.40, 3.15, 3.23, 3.88])
y2 = np.array([1.02, 1.67, 2.15, 2.45, 2.92, 3.34, 3.73, 4.09])

plt.subplot(1, 2, 1)

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



y1 = np.array([388.157, 201.401, 244.727, 165.386, 163.694, 125.372, 121.973, 101.045])
y2 = np.array([228.161, 136.806, 106.972, 93.212, 78.228, 68.213, 61.393, 56.543])

plt.subplot(1, 2, 2)

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
plt.ylabel("Time")
plt.legend()

plt.savefig(fname="../image/2.png")
plt.show()
