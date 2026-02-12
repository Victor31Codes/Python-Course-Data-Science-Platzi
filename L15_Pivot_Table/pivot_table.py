import pandas as pd

sales_data = pd.read_csv('C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\online_retail.csv')

pivot_table = pd.pivot_table(sales_data, values = 'Quantity', index = 'Country', columns = 'StockCode', aggfunc = 'sum')
print(pivot_table.head()) # Create a pivot table with 'Country' as index, 'StockCode' as columns, and the sum of 'Quantity' as values

pivot_table_2 = pd.pivot_table(sales_data, values = 'Quantity', index = 'Country', columns = ['StockCode', 'Description'], aggfunc = 'mean', fill_value=0)
print(pivot_table_2.head())

df = pd.DataFrame({
    'A': ['foo', 'bar', 'baz'],
    'B': [1, 2, 3],
    'C': [4, 5, 6]
})

print(df)

df_stack = df.stack()
print("\nStacked DataFrame:\n", df_stack) # Stack the DataFrame to create a Series with a MultiIndex

df_unstack = df_stack.unstack()
print("\nUnstacked DataFrame:\n", df_unstack) # Unstack the Series back to a DataFrame