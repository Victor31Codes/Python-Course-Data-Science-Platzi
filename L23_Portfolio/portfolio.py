import pandas as pd

# Cargar el dataset
file_path = 'online_retail.csv'
sales_data = pd.read_csv(file_path)
print(sales_data.info) #Verifica el tipo de dato de cada columna
print(sales_data.head()) #Da las primeras 5 filas
print(sales_data.describe()) #Me da datos estadisticos de cada columna
print(sales_data.isnull().sum())
print(sales_data.duplicated().sum())

#unique_values = {col: data[col].unique() for col in data.columns if col == 'Country'}
unique_values = {col: sales_data[col].unique() for col in sales_data.columns}

for col, values in unique_values.items():
    print(f"Column: {col}")
    print(f"Number of uniques values: {len(values)}")
    print(f"Unique values: {values[:10]}")
    print("-" * 50)


#Limpieza de datos
data_cleaned = sales_data.drop_duplicates()

data_cleaned = sales_data.dropna(subset=['CustomerID'])

data_cleaned.isna().sum()
data_cleaned.duplicated().sum()

data_cleaned['TotalAmount'] = data_cleaned['Quantity'] * data_cleaned['UnitPrice']
data_cleaned['InvoiceDate'] = pd.to_datetime(data_cleaned['InvoiceDate'])
print(data_cleaned.head())

data_cleaned['Year'] = data_cleaned['InvoiceDate'].dt.year
data_cleaned['Month'] = data_cleaned['InvoiceDate'].dt.month

sales_by_year =data_cleaned.groupby("Year")["TotalAmount"].sum()
print(sales_by_year)

# Extrayendo datos por semestre usando lambda. Los meses están del 1 al 12
# Devuelve 1 para los meses del primer semestre, y 2 para los meses del segundo semestre
data_cleaned["Semester"] = data_cleaned["Month"].apply(lambda x: 1 if x <= 6 else 2)

print(data_cleaned.head())

sales_by_semester = data_cleaned.groupby(["Year", "Semester"])["TotalAmount"].sum()
print(sales_by_semester)

# Ventas trimestrales usando una función
# Group es el DataFrame
def quarter(group):
    if group <= 3:
        x = 1
    elif group > 3 and group <= 6:
        x = 2
    elif group > 6 and group <= 9:
        x = 3
    else:
        x = 4
    return(x)

data_cleaned["Quarter"] = data_cleaned["Month"].apply(quarter)
data_cleaned

sales_by_quarter = data_cleaned.groupby(["Year", "Quarter"])["TotalAmount"].sum()
print(sales_by_quarter)

# Ventas trimestrales usando lambda
# Menos legible
df_cleaned_lambda = data_cleaned["Month"].apply(lambda x: 1 if x <= 3 else 2 if x <= 6 else 3 if x <= 9 else 4)

df_cleaned_lambda

sales_by_month = data_cleaned.groupby(["Year", "Month"])["TotalAmount"].sum()
print(sales_by_month)