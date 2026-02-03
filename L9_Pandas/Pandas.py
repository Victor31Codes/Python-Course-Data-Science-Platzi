import pandas as pd

path = 'C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\online_retail.csv'# We import the dataset pd.read_csv
retail_data = pd.read_csv(path)
#print(retail_data)
#print(type(retail_data))

#Excel
#retail_excel = pd.read_excel(path)
#JSON
#retail_json = pd.read_json(path)

#All of this is use to read data from different file formats into a pandas DataFrame for analysis. Print the basic data

path_gym = 'C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\daily_gym_attendance_workout_data.csv'
gym_data = pd.read_csv(path_gym)
print(gym_data.head())  # Display the first few rows of the DataFrame
print(gym_data.info())  # Get a summary of the DataFrame, including data types