import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

escalar = np.array(42) #We are asigning to an escalar variable a np.array just one value
print(type(escalar))#It gonna show that the type is numpy.ndarray
print(escalar)#It gonna show the value of the escalar variable

vector = np.array([29,35,30,41,42,21]) #We are asigning to a vector variable a np.array with multiple values
print(vector)#It gonna show the value of the vector variable

#The np.array function is used to create arrays in NumPy, which can be one-dimensional (like vectors) or multi-dimensional (like matrices).
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]]) #We are asigning to a matrix variable a np.array with multiple values in a 2D structure
print(matrix)#It gonna show the value of the matrix variable
tensor = np.array([[[1,2],[3,4],[5,6],[7,8]]]) #We are asigning to a tensor variable a np.array with multiple values in a 3D structure
print(tensor)#It gonna show the value of the tensor variable 

array_arange = np.arange(10) + 1 #We are creating an array with values from 1 to 10 using np.arange function
print(array_arange) #It gonna show the values of the array from 1 to 10

eye_matrix = np.eye(4) #We are creating a 4x4 identity matrix using np.eye function
print(eye_matrix) #It gonna show the values of the 4x4 identity matrix

diag = np.diag([1,2,3,4]) #We are creating a diagonal matrix using np.diag function
print(diag) #It gonna show the values of the diagonal matrix

random = np.random.rand(3,3) #We are creating a 3x3 matrix with random values using np.random.rand function
print(random) #It gonna show the values of the 3x3 random matrix