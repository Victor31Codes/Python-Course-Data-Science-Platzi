import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
transposed_matrix = np.transpose(matrix)
print("Original Matrix:\n", matrix) 
print(transposed_matrix)  # Transposed matrix

array = np.arange(1,17)
print("Original Array:", array)
reshaped_array = array.reshape(4,4)
print("Reshaped Array (4x4):\n", reshaped_array)

inverted_array = array[::-1]
print("Inverted Array:", inverted_array)  # Inverted array

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
flattened_array = matrix.flatten()
print("Original Matrix:\n", matrix)
print("Flattened Array:", flattened_array)  # Flattened array
#This is constantly used on AI and ML applications to convert matrices into single dimension arrays for easier processing