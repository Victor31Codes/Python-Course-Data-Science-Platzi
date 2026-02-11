import pandas as pd
import numpy as np

data = 'C:\\Users\\vtorr\\OneDrive\\Documentos\\PythonFullCourse\\online_retail.csv'# We import the dataset pd.read_csv
retail_data = pd.read_csv(data)

def total_revenue(group):
    return (group['Quantity'] * group['UnitPrice']).sum()

revenue_per_country = retail_data.groupby('Country').apply(total_revenue) #Applying a custom function to calculate total revenue for each 'Country' group
print("\nTotal revenue for each 'Country':\n", revenue_per_country)

#Top 3 countries with the highest number of sales
top_3_countries = revenue_per_country.sort_values(ascending=False).head(3)
print("Top 3 countries with the highest number of sales:\n", top_3_countries)

top_3_worst_countries = revenue_per_country.sort_values(ascending=True).head(3)
print("\nTop 3 countries with the lowest number of sales:\n", top_3_worst_countries)