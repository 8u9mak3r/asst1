import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y1 = np.array([1.00, 1.97, 1.60, 2.39, 2.42, 3.10, 3.22, 3.46])
y2 = np.array([1.01, 1.67, 2.17, 2.54, 2.86, 3.26, 3.56, 3.58])

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



y1 = np.array([399.093, 202.542, 247.810, 167.270, 165.356, 128.317, 125.007, 115.399])
y2 = np.array([232.856, 139.161, 107.736, 91.432, 80.849, 71.360, 65.435, 65.211])

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

plt.savefig(fname="image/2.png")
plt.show()
