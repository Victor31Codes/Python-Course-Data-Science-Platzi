import numpy as np

array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(array[3]) # Accessing the fourth element (index 3)
print(array[-2]) # Accessing the second to last element using negative indexing

array =np.random.randint(1, 100, size=(1,20)) 
print(array) # Displaying the array with 20 random integers between 1 and 99
print(array[0, 3:7]) # Slicing from index 3 to 7 (7 is exclusive), The random function creates a 2D array with 1 row and 20 columns, so it changes completely the analisis of a conventional array, now I have to create or separate by coordinates [row, column] to access the elements
print(array[0, 14:]) # Slicing from the start to index 5 (5 is exclusive)

array = np.random.randint(1, 100, size=(1,100)) # Creating an array with 100 random integers between 1 and 99
boolean_flag = array > 50 # Creating a boolean array where the condition is met
print(array) # Displaying the array with 100 random integers
print(boolean_flag) # Displaying the boolean array

array = [10, 20, 30, 40, 50, 60, 70, 80]
index = [1, 4, 6]
print(array[index[0]], array[index[1]], array[index[2]]) # Accessing elements at indices 1, 4, and 6

array = np.random.randint(10, 50, size=(4, 4)) # Creating a 4x4 array with random integers between 10 and 49
print(array) # Displaying the 4x4 array
print(array[2:4,2:4]) # Accessing the element at row 1, column 1