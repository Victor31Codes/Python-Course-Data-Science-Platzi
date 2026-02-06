import numpy as np
import pandas as pd

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dt_from_array = pd.DataFrame(data, columns=['A', 'B', 'C'])
print("DataFrame from NumPy array:\n", dt_from_array)

data = [[1,'Jhon', 22], [2,'Jane', 24], [3,'Doe', 21]]
df_from_list = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])
print("\nDataFrame from list of lists:\n", df_from_list)

data = [{'ID': 1,
         'Name': 'Jhon',
         'Age': 22}]

df_from_dict_list = pd.DataFrame(data)
print("\nDataFrame from list of dictionaries:\n", df_from_dict_list)

data = {'ID': [1, 2, 3], 'Name': ['Jhon', 'Jane', 'Doe'], 'Age': [22, 24, 21]}
df_from_dict = pd.DataFrame(data)
print("\nDataFrame from dictionary of lists:\n", df_from_dict)

data = {'ID': pd.Series([1, 2, 3]),
        'Name': pd.Series(['Jhon', 'Jane', 'Doe']),
        'Age': pd.Series([22,24,29])}
df_from_series_dict = pd.DataFrame(data)
print("\nDataFrame from dictionary of Series:\n", df_from_series_dict)