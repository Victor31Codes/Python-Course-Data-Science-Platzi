import pandas as pd
import numpy as np

sales_data = pd.read_csv('C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\online_retail.csv')

sales_data['InvoiceDate'] = pd.to_datetime(sales_data['InvoiceDate'])
print(sales_data.info())

sales_data.dropna(subset=['InvoiceDate'], inplace=True) #Se selecciona un subset de InvoiceDate en donde se eliminan los nulos

sales_data.set_index('InvoiceDate', inplace=True)

sales_data['Year'] = sales_data.index.year
sales_data['Month'] = sales_data.index.month
sales_data['Day'] = sales_data.index.day
sales_data['Wekdy'] = sales_data.index.weekday #Error
sales_data['Hour'] = sales_data.index.hour

print(sales_data['Year'])
print(sales_data['Hour'])


sales_data = sales_data.drop(columns=['Wekdy'])
sales_data['Weekday'] = sales_data.index.weekday

df_2011 = sales_data.loc['2011']
print(df_2011.head)
df_2011_dec = sales_data.loc['2011-12']
print(df_2011_dec.head)

df_dec_ran = sales_data.loc['2010-12-01':'2010-12-15']
print(df_dec_ran.head)

date_range_new = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
print(date_range_new)

df_dates = pd.DataFrame(date_range_new, columns=['Date'])
print(df_dates.head)

print(sales_data)   