import numpy as np

print(np.__version__)
print()

#creating arrays
arr = np.array([199, 299, 399, 499])
print(arr)

#2d array
data = np.array([[101, 202], [303, 404]])
print(data)
print() 

#array properties.
print(arr.shape)
print(arr.ndim)
print(data.ndim)
print(arr.dtype)

#basic math fns.
recharges = np.array([199, 249, 579])
print(recharges + 10)
print(recharges * 2)
print(np.mean(recharges))
print()

names = np.array(["saks", "jen", "swara", "om"])
print(names)
print(type(names))
print(names.dtype)
print() 

#useful functions
print(np.min(arr))
print(np.max(arr))
print(np.sum(arr))
print(np.std(arr))