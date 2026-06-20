import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.dates import DateFormatter

dates = pd.date_range(start='2023-01-01', periods=100)
values = np.random.rand(100).cumsum()
data = pd.DataFrame({'Date':dates, 'Value':values})

#Crear grafico de lineas
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(data['Date'],data['Value'], color='green')
plt.xticks(rotation=45)
plt.title('Serie de tiempo con formato en las fechas')
plt
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()