import numpy as np

#creating numpy arrays (in 4 ways)
# Using np.array
arr1 = np.array([1, 2, 3, 4, 5])

# Zeros
arr2 = np.zeros((2, 3))

# Ones
arr3 = np.ones((3, 3))

# Range
arr4 = np.arange(0, 10, 2)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Array 3:", arr3)
print("Array 4:", arr4)

#Reshaping arrays
arr5 = np.arange(12)
reshaped = arr5.reshape(3, 4)
print("Reshaped array:", reshaped)

#Slicing
print("Slicing example:",arr1[1:4])
print("Slicing example:",reshaped[:, 1])


#mathematical operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Dot product:", np.dot(a, b))

#Statistical operations
data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std:", np.std(data))
print("Variance:", np.var(data))
print("Sum:", np.sum(data))
print("Min:", np.min(data))

#Broadcasting
matrix = np.array([[1, 2], [3, 4]])
print("Broadcasting example:", matrix + 10)




