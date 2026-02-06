import numpy as np
import pandas as pd

#Columns names of a DataFrame
data = 'C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\online_retail.csv'# We import the dataset pd.read_csv
retail_data = pd.read_csv(data)  
columns_names = retail_data.columns
print("Columns names of the DataFrame:\n", columns_names)

rows_num,columns_num = retail_data.shape
print(f"\nNumber of columns: {columns_num}, Number of rows: {rows_num}")

daily_sales = retail_data['Quantity']
print("\nDaily Sales (Quantity column):\n", daily_sales)
print("\nDaily Sales (Quantity column):\n", daily_sales[2])# Accessing a specific element

summary = retail_data.describe()
print("\nStatistical Summary of the DataFrame:\n", summary) # Statistical summary of numerical columns

mean_value = daily_sales.mean()
print("The mean of daily sales (Quantity):", mean_value)  # Mean of the Quantity column
import numpy as np
import pandas as pd

#Columns names of a DataFrame
data = 'C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\online_retail.csv'# We import the dataset pd.read_csv
retail_data = pd.read_csv(data)  
columns_names = retail_data.columns
print("Columns names of the DataFrame:\n", columns_names)

rows_num,columns_num = retail_data.shape
print(f"\nNumber of columns: {columns_num}, Number of rows: {rows_num}")

daily_sales = retail_data['Quantity']
print("\nDaily Sales (Quantity column):\n", daily_sales)
print("\nDaily Sales (Quantity column):\n", daily_sales[2])# Accessing a specific element

summary = retail_data.describe()
print("\nStatistical Summary of the DataFrame:\n", summary) # Statistical summary of numerical columns

mean_value = daily_sales.mean()
print("The mean of daily sales (Quantity):", mean_value)  # Mean of the Quantity column
median_value = daily_sales.median()
print("The median of daily sales (Quantity):", median_value)  # Median of the Quantity column

sum_value = daily_sales.sum()
print("The total summary of daily sales (Quantity):", sum_value)  # Sum of the Quantity column

count_values = daily_sales.count()
print("The count of daily sales (Quantity), excluding NaN values:", count_values)  # Count of non-NaN entries in the Quantity column

retail_data.head

std_dev = retail_data['Quantity'].std()
print("Desviación estándar de Quantity:", std_dev)

variance = retail_data['Quantity'].var()
print("Varianza de Quantity:", variance)


min_value = retail_data['Quantity'].min()
print("Mínimo de Quantity:", min_value)

max_value = retail_data['Quantity'].max()
print("Máximo de Quantity:", max_value)

prod_value = retail_data['Quantity'].prod()
print("Producto de Quantity:", prod_value)
