import numpy as np
import matplotlib.pyplot as plt

#Configurar el tamaño del grafico

plt.figure(figsize=(8,6))

categories = ['Producto A','Producto B','Producto C']
sales = [120,150,90]

#Anotación con flecha para destacar un punto en especifico
plt.annotate('Maximo de ventas',xy=('Producto B',150),xytext=('Producto C',160),
             arrowprops= dict(facecolor='black',shrink=0.05))


#Creacion del grafico de barras verticales
plt.bar(categories,sales,color='skyblue',label='Ventas Mensuales')
plt.title('Ventas de productos en 1 mes')
plt.xlabel('Productos')
plt.ylabel('Ventas')

plt.legend()
plt.show()