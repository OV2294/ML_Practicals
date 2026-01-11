import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [199, 249, 579, 399, 299]
plt.plot(x, y)
plt.style.use("default")
plt.title("Recharge Over Time")
plt.xlabel("Days")
plt.ylabel("Amount")
plt.show()