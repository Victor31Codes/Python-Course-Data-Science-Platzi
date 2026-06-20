import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.dates import DateFormatter

dates = pd.date_range(start='2023-01-01', periods=12, freq='ME')
sales = np.random.randint(1000, 5000, size=12)
sales_data = pd.DataFrame({'Date':dates, 'Sales':sales})

#Crear grafico de lineas
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(sales_data['Date'],sales_data['Sales'], color='Blue',marker='o',label='Ventas Mensuales')

plt.gca().xaxis.set_major_formatter(DateFormatter('%b %Y'))

plt.xticks(rotation=45)
plt.title('Analisis Ventas Mensuales Totales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.tight_layout()
plt.show()