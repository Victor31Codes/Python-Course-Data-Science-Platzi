import numpy as np
import matplotlib.pyplot as plt

#Configurar el tamaño del grafico

plt.figure(figsize=(8,6))

hours = [2,3,4,5,6,7,8,9]
exam = [55,60,65,65,70,75,80,85]

plt.scatter(hours, exam, color='green')


plt.title('Relación entre horas estudiadas y el puntaje')
plt.xlabel('Horas estudiadas')
plt.ylabel('Puntaje del examen')
plt.show()
