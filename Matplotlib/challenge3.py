import matplotlib.pyplot as plt

histogram1 = [
    10, 20, 20, 30, 30, 30, 50, 50, 50, 50,
      100, 100, 100, 150, 150, 200, 200, 200, 
      249, 249, 249, 300, 300, 399, 399, 399, 
      499, 599, 799
]

plt.hist(histogram1, histtype='step')
plt.show()