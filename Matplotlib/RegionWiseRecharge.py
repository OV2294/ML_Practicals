import matplotlib.pyplot as plt

regions = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata']
totals = [45000, 50000, 30000, 25000]
target = [50000, 50000, 50000, 50000]

plt.plot(regions, totals, marker = 'o')
plt.plot(regions, target, marker = "x")
plt.title("Recharge Amount by Region")
plt.show()
