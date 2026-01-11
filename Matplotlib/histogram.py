import matplotlib.pyplot as plt

import numpy as np

data = np.random.normal(100, 20, 300)
plt.hist(data, bins = 20)
plt.title("Recharge Amount Distribution")
plt.show()