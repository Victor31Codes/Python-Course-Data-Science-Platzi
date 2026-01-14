import numpy as np

survey_responses = np.array(["Bueno", "Excelente", "Malo", 
                             "Bueno", "Malo", "Excelente",
                             "Bueno","Bueno","Malo","Excelente"])
print(np.unique(survey_responses))  # Unique survey responses

unique_elements, counts = np.unique(survey_responses, return_counts=True)
print("Unique Elements:", unique_elements)  # Unique elements
print("Counts:", counts)  # Counts of each unique element

array_x = np.arange(10)
view_y = array_x[1:3]
print("Original Array X:", array_x)
print("View Y (slice of X):", view_y)

array_x[1:3] = [10,11]
print(array_x)  # Modified Array X
print("View Y after modifying X:", view_y)  # View Y reflects changes in Array X


array_x = np.arange(10)
copy_x = array_x[[1,2]]
print("Original Array X:", array_x)
print("Copy X (slice of X):", copy_x)

array_x[1:3] = [10,11]
print(array_x)  # Modified Array X
print("Copy X after modifying X:", copy_x)  # Copy X does not reflect changes in Array X
