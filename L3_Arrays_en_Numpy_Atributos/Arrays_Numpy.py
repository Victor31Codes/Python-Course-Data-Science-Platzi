import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

array = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(array.ndim)  # It will show the number of dimensions of the array
print(array.shape)  # It will show the shape of the array (rows, columns)
print(array.dtype)  # It will show the data type of the elements in the array

z = np.array(3, dtype=np.uint8) # We are creating a scalar array with unsigned 8-bit integer type
print(z)  # It will show the data type of the scalar array

double_array = np.array([1, 2, 3], dtype='d') # We are creating an array with double precision floating point numbers
print(double_array)  # It will show the data type of the double precision array

z = z.astype(np.float64) # We are converting the data type of the scalar array to float64
print(z)  # It will show the data type of the converted scalar array

array = np.array([[1, 2, 3], [4, 5, 6]])
add = np.sum(array)  # We are calculating the sum of all elements in the array
print(add)  # It will show the sum of all elements

mean = np.mean(array)  # We are calculating the mean of all elements in the array
print(mean)  # It will show the mean of all elements

std = np.std(array)  # We are calculating the standard deviation of all elements in the array
print(std)  # It will show the standard deviation of all elements