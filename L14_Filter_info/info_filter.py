import pandas as pd

data = 'C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\online_retail.csv'# We import the dataset pd.read_csv
sales_data = pd.read_csv(data)

sales_data['InvoiceDate'] = pd.to_datetime(sales_data['InvoiceDate'])  # Convert 'InvoiceDate' to datetime format

sales_data.dropna(subset=['CustomerID', 'InvoiceDate'], inplace=True)  # Drop rows with missing 'CustomerID' or 'InvoiceNo'

sales_data['TotalPrice'] = sales_data['Quantity'] * sales_data['UnitPrice']  # Create a new column 'TotalPrice'

print(sales_data.head())  # Display the first few rows of the DataFrame with the new 'TotalPrice' column

#Filtering data for United Kingdom
au_sales = sales_data[sales_data['Country'] == 'Australia']  # Filter rows where 'Country' is 'United Kingdom'
print("\nSales data for Australia", au_sales.head())  # Display the first few rows of the filtered DataFrame for Australia


high_quantity_sales = sales_data[sales_data['Quantity'] > 10]  # Filter rows where 'Quantity' is greater than 10
print("\nSales data with Quantity greater than 10:\n", high_quantity_sales.head())

uk_high_quantity_sales = sales_data[(sales_data['Country'] == 'United Kingdom') & (sales_data['Quantity'] > 40)]  # Filter rows where 'Country' is 'United Kingdom' and 'Quantity' is greater than 10
print("\nSales data for United Kingdom with Quantity greater than 10:\n", uk_high_quantity_sales.head())

sales_2011 = sales_data[sales_data['InvoiceDate'].dt.year == 2011]  # Filter rows where 'InvoiceDate' is in the year 2011
print("\nSales data for the year 2011:\n", sales_2011.head())

sales_december_2010 = sales_data[(sales_data['InvoiceDate'].dt.year == 2010) & (sales_data['InvoiceDate'].dt.month == 12)]  # Filter rows where 'InvoiceDate' is in December 2010
print("\nSales data for December 2010:\n", sales_december_2010.head())