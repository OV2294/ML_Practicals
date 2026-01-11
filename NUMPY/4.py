import numpy as np

#slicing and indexing
arr = np.array([199, 299, 579, 399, 599, 699])
print(arr)
print(arr[0])
print(arr[1 : 3])
print()

#reshape
arr = np.array([199, 299, 579, 399, 599, 699])
print(arr)
reshape = arr.reshape(2, 3)
print(reshape)
print()

#conditional filtering.
arr = np.array([199, 249, 579, 149])
print(arr)
high = arr[arr > 200]
print(high)
low = arr[arr < 200]
print(low)
print()

#random and range 
print(np.arange(100, 600, 100))
print(np.random.randint(100, 500, size = 5))
print(np.arange(100, 110, 2))