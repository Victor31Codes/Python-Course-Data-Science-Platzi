import numpy as np
import pandas as pd

#Columns names of a DataFrame
data = 'C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\online_retail.csv'# We import the dataset pd.read_csv
retail_data = pd.read_csv(data)  

first_row = retail_data.iloc
print("First row using iloc:\n", first_row[0])  # First row
first_five_rows = retail_data.iloc
print("First five rows using iloc:\n", first_five_rows[:5])  # First five rows

subset = retail_data.iloc
print("Subset between first 8 rows and the first 4 columns using iloc:\n", subset[:8, :4]) # Subset between first 8 rows and first 4 columns

retail_value =retail_data.iloc
print("Specific value using iloc (row 3, column 2):\n", retail_value[3, 2])  # Specific value (row 3, column 2)

#Loc, specifiying labels

row_index_3 = retail_data.loc
print("Row with index label 3 using loc:\n", row_index_3[3])  # Row with index label 3

row_index_0_to_4 = retail_data.loc
print("Row with index label 3 using loc:\n", row_index_0_to_4[0:4])  # Row with index label 3

quantity_column = retail_data.loc[:, 'Quantity']
print("Quantity column using loc:\n", quantity_column)

quantity_unitprice_column = retail_data.loc[:,['Quantity', 'UnitPrice']]
print("Quantity and UnitPrice columns using loc:\n", quantity_unitprice_column)

#Check if there are missing values in the DataFrame
missing_data = retail_data.isna()
#print("Missing data in the DataFrame:\n", missing_data)
print("Missing data in the DataFrame:\n", missing_data.head())

#Count missing values in each column
missing_count = retail_data.isna().sum()
print("The missing data for each column:\n", missing_count)

no_missing_data = retail_data.dropna()
print("DataFrame after dropping rows with missing values:\n", no_missing_data.head())

no_columns_missing_data = retail_data.dropna(axis=1)
print("DataFrame after dropping columns with missing information:\n", no_columns_missing_data.head())

retail_data_filledf_zeros = retail_data.fillna(0)
print("DataFrame after filling missing values with 0_\n", retail_data_filledf_zeros)

retail_data_filledf_zeros_count = retail_data_filledf_zeros.isna().sum()
print("The missing data for each column after filling with 0:\n", retail_data_filledf_zeros_count)

mean_unit_price = retail_data['UnitPrice'].mean()
retail_data_filled_mean = retail_data['UnitPrice'].fillna(mean_unit_price)