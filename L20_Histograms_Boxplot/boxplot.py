import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
ages = [np.random.normal(30, 5, 100),
        np.random.normal(40, 5, 100),
        np.random.normal(35, 5, 100)]

plt.boxplot(ages, patch_artist=True, notch=True, vert=True, tick_labels=['Grupo 1','Grupo 2','Grupo 3']) #Las cajas se rellena de color con patch artist, y con Notch añade un recorte para estar conscientes del nivel de confianza en los datos
plt.title('Distribución de edades por grupo')
plt.xlabel('Grupo')
plt.ylabel('Edad')
plt.show()