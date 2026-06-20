import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(170, 10, 200)#(Media, Desviacion Estandar, Datos que me dan)
print(data)

plt.hist(data,color='salmon',bins =20, edgecolor='black', alpha=0.6)#El alpha es la opacidad del color que se elija en color y el bins es la cantidad de datos que habran en el histograma
plt.title('Distribución de alturas')
plt.xlabel('Altura (cm)')
plt.ylabel('Densidad')
plt.show()