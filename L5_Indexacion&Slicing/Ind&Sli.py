import numpy as np

array = np.array([10,20,30,40,50])

print(array[1])  # Accessing the second element (index 1)
print(array[-1])  # Accessing the last element using negative indexing

print(array[1:4])  # Slicing from index 1 to 3 (4 is exclusive)
print(array[:3])  # Slicing from the start to index 2 (3 is exclusive)
print(array[1:7])  # Slicing from index 1 to the end (7 exceeds length, so it goes to the end)
print(array[-1:-7])  # Slicing with negative indices (results in an empty array)

boolean_flag = array > 25  # Creating a boolean array where the condition is met
print(boolean_flag)  # Displaying the boolean array
print(type(boolean_flag))  # Displaying the type of the boolean array

index = [2,0,3]
print(array[index])  # Accessing elements at indices 2, 0, and 3

array = np.random.randint(1,10, size=(4,4)) # Creating a 4x4 array with random integers between 1 and 9
print(array)  # Displaying the 4x4 array
print(array[1,2])  # Accessing the element at row 1, column 2
print(array[:2,:2])  # Accessing all rows in column 2
