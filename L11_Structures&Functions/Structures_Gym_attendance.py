import numpy as np
import pandas as pd

data = 'C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\daily_gym_attendance_workout_data.csv'# We import the dataset pd.read_csv
gym_data =pd.read_csv(data)
print(gym_data.head())  # Display the first few rows of the DataFrame

columns_names = gym_data.columns
print("Columns names of the DataFrame:\n", columns_names)

rows_num,columns_num = gym_data.shape
print(f"\nNumber of columns: {columns_num}, Number of rows: {rows_num}")

workout_duration = gym_data['workout_duration_minutes']
print("\nWorkout Duration (workout_duration_minutes column):\n", workout_duration)

summary = gym_data.describe()
print("\nSummary Statistics of the DataFrame:\n", summary) # Statistical summary of numerical columns

mean_value = workout_duration.mean()
print("The mean of workout duration (minutes):", mean_value)  # Mean of the workout_duration_minutes column

median_value = workout_duration.median()
print("The median of workout duration (minutes):", median_value)  # Median of the workout_duration_minutes column

sum_value = workout_duration.sum()
print("The total workout duration (minutes):", sum_value)  # Sum of the workout

count_values = workout_duration.count()
print("The count of workout duration entries, excluding NaN values:", count_values)  # Count of non-NaN entries in the workout_duration_minutes column

