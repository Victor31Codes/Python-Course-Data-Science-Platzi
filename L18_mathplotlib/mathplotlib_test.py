import numpy as np
import matplotlib.pyplot as plt

month = np.array(['E','F','M','Jun','Jul'])
sales = np.array([20,25,30,28,35])

#Configurar el tamaño del grafico

plt.figure(figsize=(8,6))

#Crear el grafico

plt.plot(month, sales, marker='o',color='blue')
plt.title('Ventas mensaules de un producto')
plt.xlabel('Meses')
plt.ylabel('Ventas en miles de unidades')
plt.show()
