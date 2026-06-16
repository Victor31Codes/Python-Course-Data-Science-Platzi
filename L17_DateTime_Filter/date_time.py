import pandas as pd

data = 'C:\\Users\\Manolo\\OneDrive\\Documentos\\PythonFullCourse\\online_retail.csv'# We import the dataset pd.read_csv
sales_data = pd.read_csv(data)
sales_data['InvoiceDate'] = pd.to_datetime(sales_data['InvoiceDate'])
sales_data.info()# We check the data types of the columns

sales_data.dropna(subset=['InvoiceDate'], inplace=True)
sales_data.set_index('InvoiceDate', inplace=True)

sales_data['Year'] = sales_data.index.year
print(sales_data['Year'])