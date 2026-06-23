import pandas as pd
import matplotlib.pyplot as plt

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

total_returns = data_cleaned[data_cleaned['Quantity'] < 0].shape[0]
print(total_returns) # Se esta imprimiendo las devoluciones, por eso se selecciona la columna Quantity, valores que sean negativos demuestran devoluciones.

total_non_returns = data_cleaned[data_cleaned['Quantity'] >= 0].shape[0]
print(total_non_returns) # Por el contrario aqui no se imprimen las devoluciones

labels = ['Devoluciones','No Devoluciones']
sizes = [total_returns,total_non_returns]
colors = ['lightcoral','lightblue']

plt.figure(figsize=(8,8))
plt.pie(sizes,labels =labels,colors =colors,startangle=140)

plt.title('Porcentaje de transacciones con y sin devolución')
plt.show()

#Crear una columna categórica basada en el monto total de la transaccion (ejemplo: 'Low', 'Medium','High')
def categorize_total_amount(amount):
    if amount < 20:
        return 'Low'
    elif 20 <= amount < 100:
        return 'Medium'
    else:
        return 'high'
    
data_cleaned['AmountCategory'] = data_cleaned['TotalAmount'].apply(categorize_total_amount)

#Mostrar las primeras filas de las nuevas columnas
print(data_cleaned.head())

plt.figure(figsize=(12,6))
data_cleaned.groupby(['Year','Month']['TotalAmount'].sum().plot(kind='bar'))
plt.title('Distribución de ventas por mes y por año')
plt.xlabel('Año','Mes')
plt.ylabel('Ventas Totales')
plt.show()

top_products = data_cleaned.groupby('StockCode')['Quantity'].sum().sort_values(ascending=False).head(10)
top_products = top_products.reset_index()
top_products = pd.merge(top_products,data_cleaned[['StockCode','Description']].drop_duplicates(),on='StockCode',how='left')

plt.figure(figsize=(12,6))
plt.barh(top_products['Description'],top_products['Quantity'])
plt.title('Top de productos')
plt.xlabel('Cantidad Vendida')
plt.ylabel('Producto')
plt.gca().invert_yaxis
plt.show()