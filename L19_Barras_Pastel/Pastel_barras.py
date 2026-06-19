import numpy as np
import matplotlib.pyplot as plt

#Configurar el tamaño del grafico

plt.figure(figsize=(8,6))

products = ['Producto A','Producto B','Producto C']
market_share = [50,30,15]

#Creacion diagrama de pastel
plt.pie(market_share, labels=products,autopct='%1.1f%%',startangle=140, colors=['gold','lightcoral','orange'])


plt.title('Ventas de productos en 1 mes')
plt.axis('equal')

plt.show()

#1. Cadenas de Formato (autopct):

# '%1.1f%%': Muestra el porcentaje con un decimal y el símbolo %. Ejemplo: 35.7%.
# '%1.0f%%': Muestra el porcentaje como un número entero sin decimales. Ejemplo: 36%.
# '%1.2f%%': Muestra el porcentaje con dos decimales. Ejemplo: 35.68%.
# '%2.0f%%': Similar a '%1.0f%%', pero reserva más espacio (dos dígitos enteros). Ejemplo: 35% se vería como 35%, pero 5% se vería como 5%.
# '%1.1f': Muestra el porcentaje con un decimal, pero sin el símbolo %. Ejemplo: 35.7.
# '%1.1f units': Personaliza el texto. En este caso, mostraría el porcentaje seguido de la palabra "units". Ejemplo: 35.7 units.