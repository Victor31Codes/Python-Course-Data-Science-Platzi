import pandas as pd

df = pd.read_csv('C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\online_retail.csv')

df['TotalPrice'] = df['Quantity'] * df['UnitPrice'] #Creating a new column 'TotalPrice' by multiplying 'Quantity' and 'UnitPrice'
print("DataFrame with new 'TotalPrice' column:\n", df.head())

df['HighValue'] = df['TotalPrice'] > 40 #Creating a new column 'HighValue' that indicates whether 'TotalPrice' is greater than 1000
print("\nDataFrame with new 'HighValue' column:\n",df.head())

print(df.info())  # Display DataFrame information to see the new columns and their data types

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate']) #Converting 'InvoiceDate' column to datetime format
print(df.info())  # Display DataFrame information to see the updated data type of 'InvoiceDate' column  

df['DiscountedPrice'] = df['UnitPrice'].apply(lambda x: x * 0.9 if x > 10 else x) #Creating a new column 'DiscountedPrice' that applies a 10% discount to 'UnitPrice' if it is greater than 10
print("\nDataFrame with new 'DiscountedPrice' column:\n", df.head())

def categorize_price(price):
    if price < 20:
        return 'Low'
    elif 20 <= price < 50:
        return 'Medium'
    else:
        return 'High'
    

df['PriceCategory'] = df['UnitPrice'].apply(categorize_price) #Creating a new column 'PriceCategory' that categorizes 'UnitPrice' into 'Low', 'Medium', or 'High'
print("\nDataFrame with new 'PriceCategory' column:\n", df.head(10))

country_count = df['Country'].value_counts() #Counting the number of occurrences of each unique value in the 'Country' column
print("\nCount of unique values in 'Country' column:\n", country_count)

country_groups = df.groupby('Country')['Quantity'].sum() #Grouping the DataFrame by 'Country' and calculating the sum of 'Quantity' for each group
print("\nSum of 'Quantity' for each 'Country':\n", country_groups)

country_stats = df.groupby('Country')['UnitPrice'].agg(['mean', 'sum']) #Grouping the DataFrame by 'Country' and calculating the mean, min, and max of 'UnitPrice' for each group
print("\nMean, sum of 'UnitPrice' for each 'Country':\n", country_stats)

country_stock_group = df.groupby(['Country', 'StockCode'])['Quantity'].sum() #Grouping the DataFrame by both 'Country' and 'StockCode' and calculating the sum of 'Quantity' for each group
print("\nSum of 'Quantity' for each combination of 'Country' and 'StockCode':\n", country_stock_group)

def total_revenue(group):
    return (group['Quantity'] * group['UnitPrice']).sum()

revenue_per_country = df.groupby('Country').apply(total_revenue) #Applying a custom function to calculate total revenue for each 'Country' group
print("\nTotal revenue for each 'Country':\n", revenue_per_country)