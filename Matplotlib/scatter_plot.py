import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y, color = "blue", alpha = 1)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()