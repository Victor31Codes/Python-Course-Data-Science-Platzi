import pandas as pd
import numpy as np

path = 'C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\online_retail.csv'# We import the dataset pd.read_csv
retail_data = pd.read_csv(path)
print(retail_data.head())
print(type(retail_data))

#Excel
#retail_excel = pd.read_excel(path)
#JSON
#retail_json = pd.read_json(path)

#All of this is use to read data from different file formats into a pandas DataFrame for analysis. Print the basic data

data = np.array([[1,2,3],[4,5,6],[7,8,9]])
dt_from_array = pd.DataFrame(data, columns=['A','B','C'])
print(dt_from_array)

data = [[1,'Victor', 22],[2,'Josue',20]]
dt_from_list = pd.DataFrame(data, columns=['ID','Name','Age'])
print(dt_from_list)

data = [{'ID': 1,
         'Name': 'Henry',
         'Age': 25}]
dt_from_dict_list = pd.DataFrame(data)
print(dt_from_dict_list)

data = {'ID': [1,2,3],'Name':['Santiago','Nicolas','Carlos'], 'Age': [21,23,21]}
dt_from_dict = pd.DataFrame(data)
print(dt_from_dict)

data = {
    'ID': pd.Series([3,4,5]),
    'Name': pd.Series(['Trinity','Lilly','Gabi']),
    'Age' : pd.Series([21,21,25])
}
dt_from_series_list = pd.DataFrame(data)
print(dt_from_series_list)
# path_gym = 'C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\daily_gym_attendance_workout_data.csv'
# gym_data = pd.read_csv(path_gym)
# print(gym_data.head())  # Display the first few rows of the DataFrame
# print(gym_data.info())  # Get a summary of the DataFrame, including data types