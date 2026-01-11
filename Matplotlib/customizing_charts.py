import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [199, 249, 579, 399, 299]
plt.style.use('bmh')
"""plt.plot(x, y, label = "Recharge")
plt.grid(True)
plt.legend()
plt.show()"""

plt.plot(x, y, color = "green", 
         linestyle = "--", marker='o')
plt.title("Recharge Trend")
plt.savefig("hello.jpg")
plt.show()